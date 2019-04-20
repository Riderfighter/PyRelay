import threading

import Packets
import Proxy


# Basic plugin just to test the callback system
class ProxyUtilities(object):
    # TODO: Handle joining realms
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self.objectId = 0
        proxy.hookPacket(Packets.HelloPacket, self.onHello)
        proxy.hookPacket(Packets.CreateSuccessPacket, self.onCreateSuccess)
        proxy.hookPacket(Packets.ReconnectPacket, self.onReconnect)
        proxy.hookPacket(Packets.FailurePacket, self.onFailure)
        proxy.hookCommand("reload", self.reloadPlugins)
        proxy.hookCommand("plugintest", self.sendTest)

    def sendTest(self, client, args):
        packet = Packets.NotificationPacket()
        packet.write(self.objectId, "Ran plugin test.", 0x8B00FF)
        self._proxy.sendToClient(client, packet)

    def reloadPlugins(self, client, args):
        self._proxy.loadPlugins()
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Plugins reloaded.", 0x8B00FF)
        self._proxy.sendToClient(client, newPacket)

    def onFailure(self, client, packet: Packets.FailurePacket):
        data = packet.read()
        print(data)

    def onHello(self, client, packet: Packets.HelloPacket):
        data = packet.read()
        print(data)

        # print(packet.data[packet.index:])

        if len(packet.key) != 0:
            packet.send = False
            print("trying to shift clients")
            oldClient = client
            client = self._proxy._clients[packet.key.decode("utf8")]
            client.client = oldClient.client
            client.crypto = oldClient.crypto
            newpacket = Packets.HelloPacket()
            newpacket.write(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                            client.realConKey, data[9], data[10], data[11], data[12], data[13], data[14], data[15])
            client.realConKey = b''
            client.start()
            self._proxy.sendToServer(client, newpacket)

    def onReconnect(self, client, packet: Packets.ReconnectPacket):
        packet.send = False
        packet.read()
        newPacket = Packets.ReconnectPacket()
        if packet.host != "":
            client.lastServer = packet.host
        if packet.port != -1:
            client.lastPort = packet.port
        if len(packet.key) != 0:
            client.realConKey = packet.key
        newPacket.write(packet.name, "localhost", packet.stats, 2050, packet.gameid, packet.keytime,
                        packet.isfromarena, client.guid.encode("utf8"))
        self._proxy.sendToClient(client, newPacket)
        client.restartClient()

    def onCreateSuccess(self, client, packet: Packets.CreateSuccessPacket):
        data = packet.read()
        self.objectId = data[0]
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Welcome to PyRelay!", 0x8B00FF)
        threading.Timer(1.5, self._proxy.sendToClient, args=(client, newPacket,)).start()
