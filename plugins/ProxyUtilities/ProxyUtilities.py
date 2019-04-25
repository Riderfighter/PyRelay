import threading
import uuid

import Packets
import Proxy
import State


# Basic plugin just to test the callback system
class ProxyUtilities:
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
        new_packet = Packets.NotificationPacket()
        new_packet.write(self.objectId, "Plugins reloaded.", 0x8B00FF)
        self._proxy.sendToClient(client, new_packet)

    def onFailure(self, client, packet: Packets.FailurePacket):
        data = packet.read()
        print(data)

    def onHello(self, client, packet: Packets.HelloPacket):
        data = packet.read()
        print(data)
        # print(packet.data[packet.index:])

        if len(packet.key) != 0:
            packet.send = False
            state = self._proxy.states[packet.key.decode("utf8")]
            client.state = state
            new_packet = Packets.HelloPacket()
            new_packet.write(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                             state.realConKey, data[9], data[10], data[11], data[12], data[13], data[14], data[15])
            state.realConKey = b''
            self._proxy.sendToServer(client, new_packet)
        else:
            print("Generating new state")
            guid = uuid.uuid4().hex
            s = State.State(guid)
            client.state = s
            self._proxy.states[guid] = s

    def onReconnect(self, client, packet: Packets.ReconnectPacket):
        packet.send = False
        packet.read()
        new_packet = Packets.ReconnectPacket()
        if packet.host:
            client.state.lastServer = packet.host
        if packet.port != -1:
            client.state.lastPort = packet.port
        if packet.key:
            client.state.realConKey = packet.key
        new_packet.write(packet.name, "localhost", packet.stats, 2050, packet.gameid, packet.keytime,
                         packet.isfromarena, client.state.guid.encode("utf8"))
        self._proxy.sendToClient(client, new_packet)
        client.restartClient()

    def onCreateSuccess(self, client, packet: Packets.CreateSuccessPacket):
        data = packet.read()
        self.objectId = data[0]
        new_packet = Packets.NotificationPacket()
        new_packet.write(self.objectId, "Welcome to PyRelay!", 0x8B00FF)
        threading.Timer(1.5, self._proxy.sendToClient, args=(client, new_packet,)).start()
