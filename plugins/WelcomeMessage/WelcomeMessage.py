import threading

import Packets

import Proxy


# Basic plugin just to test the callback system
class WelcomeMessage(object):
    # TODO: Handle joining realms
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self.objectId = 0
        proxy.hookPacket(Packets.HelloPacket, self.onHello)
        proxy.hookPacket(Packets.CreateSuccessPacket, self.onCreateSuccess)
        proxy.hookPacket(Packets.ReconnectPacket, self.onReconnect)
        proxy.hookPacket(Packets.FailurePacket, self.onFailure)
        proxy.hookCommand("reload", self.reloadPlugins)

    def reloadPlugins(self, args):
        self._proxy.loadPlugins()
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Plugins reloaded.", 0x8B00FF)
        self._proxy.sendToClient(newPacket)

    def onFailure(self, packet: Packets.FailurePacket):
        data = packet.read()
        print(data)

    def onHello(self, packet: Packets.HelloPacket):
        data = packet.read()
        print(data)

    def onReconnect(self, packet: Packets.ReconnectPacket):
        packet.send = False
        data = packet.read()
        print(data[7])
        newPacket = Packets.ReconnectPacket()
        newPacket.write(data[0], "localhost", data[2], 2050, data[4], data[5], data[6], data[7])
        self._proxy.lastServer = packet.host if self._proxy.lastServer != packet.host else ""
        self._proxy.sendToClient(newPacket)

    def onCreateSuccess(self, packet: Packets.CreateSuccessPacket):
        data = packet.read()
        self.objectId = data[0]
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Welcome to PyRelay!", 0x8B00FF)
        threading.Timer(1.5, self._proxy.sendToClient, args=(newPacket,)).start()
