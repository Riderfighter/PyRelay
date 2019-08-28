import random
import socket
import threading

import Packets
import Proxy


# Basic plugin just to test the callback system
class ProxyUtilities:
    # TODO: Handle joining realms
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        # self.objectId = 0
        proxy.hookPacket(Packets.HelloPacket, self.onHello)
        proxy.hookPacket(Packets.CreateSuccessPacket, self.onCreateSuccess)
        proxy.hookPacket(Packets.ReconnectPacket, self.onReconnect)
        proxy.hookPacket(Packets.FailurePacket, self.onFailure)
        proxy.hookCommand("reload", self.reloadPlugins)
        proxy.hookCommand("plugintest", self.sendTest)

    def sendTest(self, args):
        packet = Packets.NotificationPacket()
        packet.objectId = self._proxy.playerid
        packet.message = "Ran plugin test."
        packet.color = 0x8B00FF
        packet.write()
        self._proxy.sendToClient(packet)

    def reloadPlugins(self, args):
        threading.Thread(target=self._proxy.loadPlugins).start()
        newPacket = Packets.NotificationPacket()
        newPacket.objectId = self._proxy.playerid
        newPacket.message = "Plugins hotloaded!"
        newPacket.color = 0x8B00FF
        newPacket.write()
        self._proxy.sendToClient(newPacket)

    def onFailure(self, packet: Packets.FailurePacket):
        print(packet.errorId, packet.errorMessage)

    def onHello(self, packet: Packets.HelloPacket):
        # data = packet.read()
        if packet.gameId == -2 and self._proxy.lastServer != self._proxy.defaultServer:
            self._proxy.lastServer = self._proxy.defaultServer
            self._proxy.lastPort = self._proxy.defaultPort
        self._proxy.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._proxy.server.connect((self._proxy.lastServer, self._proxy.lastPort))

    def onReconnect(self, packet: Packets.ReconnectPacket):
        packet.send = False
        # packet.read()
        # packet.host = "localhost"
        # packet.port = 2050
        newPacket = Packets.ReconnectPacket()
        newPacket.name = packet.name
        newPacket.host = "localhost"
        newPacket.stats = packet.stats
        newPacket.port = 2050
        newPacket.gameId = packet.gameId
        newPacket.keyTime = packet.keyTime
        newPacket.isFromArena = packet.isFromArena
        newPacket.key = packet.key
        newPacket.write()
        # newPacket.write(packet.name, "localhost", packet.stats, 2050, packet.gameId, packet.keyTime, packet.isFromArena,
        #                 packet.key)
        if packet.host != "":
            self._proxy.lastServer = packet.host
        if packet.port != -1:
            self._proxy.lastPort = packet.port
        self._proxy.sendToClient(newPacket)
        self._proxy.restartProxy()

    def onCreateSuccess(self, packet: Packets.CreateSuccessPacket):
        # data = packet.read()
        self._proxy.playerid = packet.objectId
        newPacket = Packets.NotificationPacket()
        newPacket.objectId = self._proxy.playerid
        newPacket.message = "Welcome to PyRelay!"
        rcolor = lambda: random.randint(0, 255)
        newPacket.color = int('%02X%02X%02X' % (rcolor(), rcolor(), rcolor()), 16)
        newPacket.write()
        threading.Timer(1.5, self._proxy.sendToClient, args=(newPacket,)).start() # I need to implement a dispatch loop