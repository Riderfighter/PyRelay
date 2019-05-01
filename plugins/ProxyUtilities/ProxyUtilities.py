import threading
import uuid

import Client
import Packets
import Proxy
import State


# Basic plugin just to test the callback system
class ProxyUtilities:
    # TODO: Handle joining realms
    def __init__(self, proxy: Proxy.Proxy, client: Client.Client):
        self._client = client
        self._proxy = proxy
        self.objectId = 0
        client.hookPacket(Packets.HelloPacket, self.onHello)
        client.hookPacket(Packets.CreateSuccessPacket, self.onCreateSuccess)
        client.hookPacket(Packets.ReconnectPacket, self.onReconnect)
        client.hookPacket(Packets.FailurePacket, self.onFailure)
        client.hookCommand("reload", self.reloadPlugins)
        client.hookCommand("plugintest", self.sendTest)

    def sendTest(self, args):
        packet = Packets.NotificationPacket()
        packet.write(self.objectId, "Ran plugin test.", 0x8B00FF)
        self._client.sendToClient(packet)

    def reloadPlugins(self, args):
        self._proxy.loadPlugins()
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Plugins reloaded.", 0x8B00FF)
        self._client.sendToClient(newPacket)

    def onFailure(self, packet: Packets.FailurePacket):
        data = packet.read()
        print(data)

    def onHello(self, packet: Packets.HelloPacket):
        print(packet.data)
        data = packet.read()
        # print(packet.data[packet.index:])

        if len(packet.key) != 0:
            packet.send = False
            state = self._proxy.states[packet.key.decode("utf8")]
            self._client.state = state
            new_packet = Packets.HelloPacket()
            new_packet.write(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                             state.realConKey, data[9], data[10], data[11], data[12], data[13], data[14], data[15])
            state.realConKey = b''
            self._client.sendToServer(new_packet)
        else:
            print("Generating new state")
            guid = uuid.uuid4().hex
            s = State.State(guid)
            self._client.state = s
            self._proxy.states[guid] = s

    def onReconnect(self, packet: Packets.ReconnectPacket):
        packet.send = False
        packet.read()
        new_packet = Packets.ReconnectPacket()
        if packet.host:
            self._client.state.lastServer = packet.host
        if packet.port != -1:
            self._client.state.lastPort = packet.port
        if packet.key:
            self._client.state.realConKey = packet.key
        new_packet.write(packet.name, "localhost", packet.stats, 2050, packet.gameid, packet.keytime,
                         packet.isfromarena, self._client.state.guid.encode("utf8"))
        self._client.sendToClient(new_packet)
        self._client.restartClient()

    def onCreateSuccess(self, packet: Packets.CreateSuccessPacket):
        data = packet.read()
        self.objectId = data[0]
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Welcome to PyRelay!", 0x8B00FF)
        threading.Timer(1.5, self._client.sendToClient, args=(newPacket,)).start()
