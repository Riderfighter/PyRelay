import socket
import Utilities
import struct
import Packet
import Packets
import select
import binascii
import threading
import time

import WelcomeMessage
# 6a39570cc9de4ec71d64821894c79332b197f92ba85ed281a023
# client to proxy only
class Proxy(object):
    def __init__(self):
        # Constant variables/classes
        self.defaultServer = "54.241.208.244"
        self.packetPointers = Utilities.Packetsetup().setupPacket()
        self.crypto = Utilities.CryptoUtils(b'6a39570cc9de4ec71d64821894',b'c79332b197f92ba85ed281a023')

        # commonly mutated variables/classes
        # Dont access _packetHooks directly, its considered a private variable.
        self._packetHooks = {}
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = None

    def enableSWFPROXY(self):
        Adobepolicy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Adobepolicy.bind(('127.0.0.1', 843))
        Adobepolicy.listen(1)
        policy, addr = Adobepolicy.accept()
        policy.sendall(b'<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
        policy.close()

    def hookPacket(self, Packet: Packet.Packet, callback):
        """
        :param Packet: The non-initialized packet you'd like to hook.
        :param callback: The non-initialized callback function.
        """
        if self._packetHooks.get(Packet.__name__):
            self._packetHooks[Packet.__name__].append(callback)
        else:
            self._packetHooks[Packet.__name__] = [callback]

    def sendPacket(self, packet, forClient):
        data = bytes(packet.data)
        for key, value in self.packetPointers.items():
            if value:
                if value.__name__ == packet.__class__.__name__:
                    packetId = key
                    break
        if packetId == "":
            return
        if forClient:
            header = struct.pack(">ib", len(data)+5, packetId) + self.crypto.serverIn(data)
            self.client.send(header)
        else:
            header = struct.pack(">ib", len(data)+5, packetId) + self.crypto.clientIn(data)
            self.server.send(header)

    def sendToClient(self, packet):
        self.sendPacket(packet, True)
    
    def sendToServer(self, packet):
        self.sendPacket(packet, False)

    def processClientPacket(self, client, packet):
        # Implement command hooks later
        # if (packet.__class__.__name__ == "PLAYERTEXT"):
        #     playerText = packet.read()
        #     if playerText.text.startswith("/"):
        #         text = playerText.text.replace("/","").lower()
        
        # Should call a hooked function
        for packetName in self._packetHooks:
            if packetName == packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    threading.Thread(target=callback, args=(client, packet)).start()

    def processServerPacket(self, server, packet):
        for packetName in self._packetHooks:
            if packetName == packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    threading.Thread(target=callback, args=(server, packet)).start()

    def readRemote(self, socket, socket2, fromClient=True):
        """
        sends data from socket2 to socket 1
        """
        header = socket2.recv(5) # Receives data from socket2
        if len(header) > 0:
            packetid = header[4]
            datalength = struct.unpack(">i", header[:4])[0] - 5 # minus 5 to remove the length of the header per packet
            if datalength > 0:
                header += socket2.recv(datalength)
                # This is to make sure we receive all parts of the data we want to decode/send to the server.
                while len(header[5:]) != datalength:
                    header += socket2.recv(datalength-len(header[5:]))
                if fromClient:
                    dedata = self.crypto.clientOut(header[5:])
                    if self.packetPointers.get(packetid):
                        Packet = self.packetPointers.get(packetid)()
                        Packet.data.extend(dedata)
                        self.processClientPacket(socket2, Packet)

                    header = header[:5]+self.crypto.clientIn(dedata)
                else:
                    dedata = self.crypto.serverOut(header[5:])
                    if self.packetPointers.get(packetid):
                        Packet = self.packetPointers.get(packetid)()
                        Packet.data.extend(dedata)
                        self.processServerPacket(socket2, Packet)
                    header = header[:5]+self.crypto.serverIn(dedata)
            socket.send(header) # Sends data from sockt2 to socket1

    def Route(self):
        # Adobe Policy setter
        self.enableSWFPROXY()
        self.listener.bind(('127.0.0.1', 2050))
        self.listener.listen(1)
        
        self.client, caddr = self.listener.accept()

        self.server.connect(('52.47.150.186', 2050))
        # Figure out how to rebind this socket to the reconnect packets ip thing.
        running = True

        while running:
            try:
                rlist = select.select([self.client, self.server], [], [])[0]

                if self.client in rlist:
                    self.readRemote( self.server, self.client, True)
                if self.server in rlist and running:
                    # server.send(client.recv(10000))
                    self.readRemote(self.client,  self.server, False)
                
            except KeyboardInterrupt:
                self.client.close()
                self.server.close()
                self.listener.close()

if __name__ == '__main__':
    proxy = Proxy()
    WelcomeMessage.WelcomeMessage(proxy)
    threading.Thread(target=proxy.Route).start()