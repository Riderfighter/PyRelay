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

class Proxy:
    def __init__(self):
        # Constant variables/classes
        self.defaultServer = "54.183.179.205"
        self.lastServer = self.defaultServer
        self.defaultPort = 2050
        self.lastPort = 2050
        self.packetPointers = Utilities.Packetsetup().setup_packet()
        self.crypto = Utilities.CryptoUtils('6a39570cc9de4ec71d64821894', 'c79332b197f92ba85ed281a023')
        self.playerid = 0
        # commonly mutated variables/classes
        # Dont access _packetHooks/_commandHooks directly, they are considered private variables.
        self.plugins = []
        self.reloading_plugins = False
        self.processing = False
        self._packetHooks = {}
        self._commandHooks = {}
        self.running = True
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = None
        self.client = None

    def loadPlugins(self):
        while self.processing:
            time.sleep(0.005)
            continue
        self.reloading_plugins = True
        if self._packetHooks or self._commandHooks:
            self._packetHooks.clear()
            self._commandHooks.clear()
        pluginDIR = "./plugins"
        possibleplugins = os.listdir(pluginDIR)
        testset = set()
        for i in [file for file in possibleplugins if not file.startswith(".")]:  # removing all files that start with a "." on mac
            plugin = importlib.import_module(f"plugins.{i}.{i}")
            testset.add(plugin)
            if plugin not in self.plugins:
                self.plugins.append(plugin)
            else:
                importlib.reload(plugin)
        for oldplugin in list(set(self.plugins) - testset):
            self.plugins.remove(oldplugin)
        for plugin in self.plugins:
            getattr(plugin, plugin.__name__.split(".")[2])(self)
        self.reloading_plugins = False

    def enableSWFPROXY(self):
        Adobepolicy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Adobepolicy.bind(('127.0.0.1', 843))
        Adobepolicy.listen(1)
        while True:
            policy, addr = Adobepolicy.accept()
            print("[!] Client is asking for privacy policy!")
            policy.sendall(
                b'<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            time.sleep(1)
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
        if self.client or self.server:
            data = bytes(packet.data)
            for key, value in self.packetPointers.items():
                if value:
                    if value.__name__ == type(packet).__name__:
                        packetId = key
                        break
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
        if type(packet).__name__ == "PlayerTextPacket":
            # playerText = packet.read()
            if packet.text.startswith("/"):
                commandText = packet.text.replace("/", "").split(" ")
                for command in self._commandHooks:
                    if command == commandText[0]:
                        self._commandHooks[command](commandText[1:])
                        packet.send = False

        # Should call a hooked function
        self.process_packet(packet)

    def process_packet(self, packet):
        for packetName in self._packetHooks:
            if packetName == type(packet).__name__:
                for callback in self._packetHooks[packetName]:
                    callback(packet)

    def readRemote(self, fromClient=True):
        """
        sends data from socket2 to socket 1
        """
        socket2 = self.client if fromClient else self.server
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
            if not self.reloading_plugins:
                if self.packetPointers.get(packetid):
                    Packet = self.packetPointers.get(packetid)()
                    Packet.data.extend(dedata)
                    Packet.read()
                    self.processing = True
                    self.processClientPacket(Packet)
                    self.processing = False
                    if not Packet.send:
                        return
                    Packet.write()
                    if dedata != bytes(Packet.data):
                        print(packetid, dedata, bytes(Packet.data))
            header = header[:5] + self.crypto.clientIn(dedata)
        else:
            dedata = self.crypto.serverOut(header[5:])
            if not self.reloading_plugins:
                if self.packetPointers.get(packetid):
                    Packet = self.packetPointers.get(packetid)()
                    Packet.data.extend(dedata)
                    Packet.read()
                    self.processing = True
                    self.process_packet(Packet)
                    self.processing = False
                    if not Packet.send:
                        return
                    Packet.write()
                    if packetid == 62:
                        Packet.data = Packet.data[:int(Packet.index / 2)]
                    if dedata != bytes(Packet.data):
                        print(packetid, dedata, bytes(Packet.data))
            header = header[:5] + self.crypto.serverIn(dedata)
        socket = self.server if fromClient else self.client
        socket.send(header)  # Sends data from socket2 to socket1

    def startUpProxy(self):
        self.crypto.reset()
        while True:
            if not self.client:
                time.sleep(0.005)  # Don't touch this, otherwise 100% CPU
                continue
            break
        self.running = True
        self.Route()

    def restartProxy(self):
        """
        Restarts proxy by closing the client connection, server connection and then starting up the proxy.
        """
        print("[!] Restarting proxy!")
        self.client.close()
        self.server.close()
        self.running = False
        self.client = None
        self.server = None
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

                rlist = select.select([self.client, self.server], [], [])[0] if self.server else \
                select.select([self.client], [], [])[0]
                if self.client in rlist:
                    self.readRemote()
                if self.server in rlist:
                    self.readRemote(False)

        except KeyboardInterrupt:
            self.client.close()
            self.server.close()
            self.listener.close()
        except Exception as e:
            print(e)

        print("Loop successfully exited")


if __name__ == '__main__':
    proxy = Proxy()
    proxy.loadPlugins()
    proxy.start()
