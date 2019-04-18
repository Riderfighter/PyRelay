import importlib
import os
import select
import socket
import struct
import threading
import time

import Packet
import Utilities


# 6a39570cc9de4ec71d64821894 c79332b197f92ba85ed281a023
# client to proxy only

class Proxy(object):
    def __init__(self):
        # Constant variables/classes
        self.defaultServer = "54.183.236.213"
        self.lastServer = self.defaultServer
        self.defaultPort = 2050
        self.lastPort = 2050
        self.packetPointers = Utilities.Packetsetup().setupPacket()
        self.crypto = Utilities.CryptoUtils(b'6a39570cc9de4ec71d64821894', b'c79332b197f92ba85ed281a023')

        # commonly mutated variables/classes
        # Dont access _packetHooks/_commandHooks directly, they are considered private variables.
        self.plugins = []
        self._packetHooks = {}
        self._commandHooks = {}
        self.running = True
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = None
        self.client = None

    def loadPlugins(self):
        if self._packetHooks or self._commandHooks:
            self._packetHooks.clear()
            self._commandHooks.clear()
        pluginDIR = "./plugins"
        possibleplugins = os.listdir(pluginDIR)
        for i in [file for file in possibleplugins if not file.startswith(".")]:  # removing all files that start with a "." on mac
            plugin = importlib.import_module(f"plugins.{i}.{i}")
            if plugin not in self.plugins:
                self.plugins.append(plugin)
            getattr(plugin, i)(self)
        print(self._commandHooks)
        print(self._packetHooks)

    def enableSWFPROXY(self):
        Adobepolicy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Adobepolicy.bind(('127.0.0.1', 843))
        Adobepolicy.listen(1)
        while True:
            policy, addr = Adobepolicy.accept()
            print("sending xml")
            policy.sendall(
                b'<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            policy.close()

    def enableClients(self):
        # TODO: Allow multiple clients connected to the proxy and handle each individually
        self.listener.bind(('127.0.0.1', 2050))
        self.listener.listen(5)
        while True:
            if not self.client:
                self.client, _ = self.listener.accept()
            time.sleep(0.005) # Don't touch this, if you do your cpu usage rises to like 99.8%

    def hookPacket(self, Packet: Packet.Packet, callback):
        """
        :param Packet: The non-initialized packet you'd like to hook.
        :param callback: The non-initialized callback function.
        """
        if self._packetHooks.get(Packet.__name__):
            self._packetHooks[Packet.__name__].append(callback)
        else:
            self._packetHooks[Packet.__name__] = [callback]

    def hookCommand(self, command, callback):
        if command in self._commandHooks:
            print("Command already registered. Ignoring...")
        else:
            self._commandHooks[command] = callback

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
            header = struct.pack(">ib", len(data) + 5, packetId) + self.crypto.serverIn(data)
            self.client.send(header)
        else:
            header = struct.pack(">ib", len(data) + 5, packetId) + self.crypto.clientIn(data)
            self.server.send(header)

    def sendToClient(self, packet):
        self.sendPacket(packet, True)

    def sendToServer(self, packet):
        self.sendPacket(packet, False)

    def processClientPacket(self, packet):
        # Implement command hooks later
        if packet.__class__.__name__ == "PlayerTextPacket":
            playerText = packet.read()
            if playerText.startswith("/"):
                commandText = playerText.replace("/", "").split(" ")
                for command in self._commandHooks:
                    if command == commandText[0]:
                        self._commandHooks[command](commandText[1:])
                        packet.send = False

        # Should call a hooked function
        for packetName in self._packetHooks:
            if packetName == packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    callback(packet)

    def processServerPacket(self, packet):
        for packetName in self._packetHooks:
            if packetName == packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    callback(packet)

    def readRemote(self, socket, socket2, fromClient=True):
        """
        sends data from socket2 to socket 1
        """
        header = socket2.recv(5)  # Receives data from socket2
        if len(header) == 0:
            self.restartProxy()
        if header == b'\xff':
            print("Kill byte received, all hell will break loose.")
            self.listener.close()
            self.server.close()
            self.client.close()
            self.running = False
            return
        while len(header) != 5:
            header += socket2.recv(5 - len(header))
        packetid = header[4]
        datalength = struct.unpack(">i", header[:4])[0] - 5  # minus 5 to remove the length of the header per packet
        # This is to make sure we receive all parts of the data we want to decode/send to the server.
        while len(header[5:]) != datalength:
            header += socket2.recv(datalength - len(header[5:]))
        if fromClient:
            dedata = self.crypto.clientOut(header[5:])
            if self.packetPointers.get(packetid):
                Packet = self.packetPointers.get(packetid)()
                Packet.data.extend(dedata)
                self.processClientPacket(Packet)
                if not Packet.send:
                    return
            header = header[:5] + self.crypto.clientIn(dedata)
        else:
            dedata = self.crypto.serverOut(header[5:])
            if self.packetPointers.get(packetid):
                Packet = self.packetPointers.get(packetid)()
                Packet.data.extend(dedata)
                self.processServerPacket(Packet)
                if not Packet.send:
                    return
            header = header[:5] + self.crypto.serverIn(dedata)
        socket.send(header)  # Sends data from socket2 to socket1

    def startUpProxy(self):
        self.crypto.reset()
        while True:
            if not self.client:
                time.sleep(0.005)  # Don't touch this, otherwise 100% CPU
                continue
            break
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.lastServer, self.lastPort))
        self.running = True
        self.Route()
        # threading.Thread(target=self.Route).start()

    def restartProxy(self):
        """
        Restarts proxy by closing the client connection, server connection and then starting up the proxy.
        """
        print("restarting proxy")
        self.client.close()
        self.server.close()
        self.running = False
        self.client = None
        self.startUpProxy()

    def start(self):
        threading.Thread(target=self.enableSWFPROXY).start()
        threading.Thread(target=self.enableClients).start()
        self.startUpProxy()

    def Route(self):
        # Figure out how to rebind this socket to the reconnect packets ip thing.
        try:
            while True:
                if not self.running:
                    break
                rlist = select.select([self.client, self.server], [], [])[0]

                if self.client in rlist:
                    self.readRemote(self.server, self.client, True)
                if self.server in rlist:
                    self.readRemote(self.client, self.server, False)

        except KeyboardInterrupt:
            self.client.close()
            self.server.close()
            self.listener.close()
        print("Loop successfully exited")


if __name__ == '__main__':
    proxy = Proxy()
    proxy.loadPlugins()
    proxy.start()
