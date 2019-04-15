import Packets
import Proxy
import time
import threading
import socket

# Basic plugin just to test the callback system
class WelcomeMessage(object):
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self.objectId = 0
        proxy.hookPacket(Packets.HelloPacket, self.onHello)
        proxy.hookPacket(Packets.CreateSuccessPacket, self.onCreateSuccess)
        proxy.hookPacket(Packets.ReconnectPacket, self.onReconnect)
        proxy.hookPacket(Packets.FailurePacket, self.onFailure)

    def onFailure(self, packet: Packets.FailurePacket):
        data = packet.read()
        print(data)

    def onHello(self, packet: Packets.HelloPacket):
        data = packet.read()
        print(packet.data)

    def onReconnect(self, packet: Packets.ReconnectPacket):
        packet.send = False
        data = packet.read()
        newPacket = Packets.ReconnectPacket()
        newPacket.write(data[0], "localhost", data[2], -1, data[4],data[5],data[6],data[7])
        self._proxy.lastServer = packet.host if self._proxy.lastServer != packet.host else ""
        self._proxy.server.close()
        self._proxy.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self._proxy.lastServer != "":
            self._proxy.server.connect((self._proxy.lastServer, self._proxy.lastPort))
        else:
            self._proxy.server.connect((self._proxy.defaultServer, self._proxy.defaultPort))
        self._proxy.sendToClient(newPacket)
        # self._proxy.crypto.resetCiphers()

    def onCreateSuccess(self, packet: Packets.CreateSuccessPacket):
        data = packet.read()
        self.objectId = data[0]
        newPacket = Packets.NotificationPacket()
        newPacket.write(self.objectId, "Welcome to PyRelay!", 0x8B00FF)
        threading.Timer(1.5,self._proxy.sendToClient, args=(newPacket,)).start()