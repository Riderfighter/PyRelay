import importlib
import os
import socket
import struct
import threading
import time

import Client
import Packet
import Utilities


# 6a39570cc9de4ec71d64821894 c79332b197f92ba85ed281a023
# client to proxy only

class Proxy(object):
    def __init__(self):
        # Constant variables/classes
        self.defaultServer = "54.183.236.213"
        self.defaultPort = 2050
        # self.lastServer = self.defaultServer
        # self.lastPort = 2050
        self.packetPointers = Utilities.Packetsetup().setupPacket()
        # self.crypto = Utilities.CryptoUtils(b'6a39570cc9de4ec71d64821894', b'c79332b197f92ba85ed281a023')

        # commonly mutated variables/classes
        # Dont access _packetHooks/_commandHooks directly, they are considered private variables.
        self.plugins = []
        self.states = {}
        self._clients = []
        self._packetHooks = {}
        self._commandHooks = {}
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def loadPlugins(self):
        if self._packetHooks or self._commandHooks:
            self._packetHooks.clear()
            self._commandHooks.clear()
        plugin_dir = "./plugins"
        possible_plugins = os.listdir(plugin_dir)
        for i in [file for file in possible_plugins if
                  not file.startswith(".")]:  # removing all files that start with a "." on mac
            plugin = importlib.import_module(f"plugins.{i}.{i}")
            if plugin not in self.plugins:
                self.plugins.append(plugin)
            getattr(plugin, i)(self)

    def enableSWFPROXY(self):
        adobe_policy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        adobe_policy.bind(('127.0.0.1', 843))
        adobe_policy.listen(1)
        while True:
            policy, addr = adobe_policy.accept()
            print("sending xml")
            policy.sendall(
                b'<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            policy.close()

    def enableClients(self):
        # TODO: Allow multiple clients connected to the proxy and handle each individually
        self.listener.bind(('127.0.0.1', 2050))
        self.listener.listen(5)
        while True:
            client, _ = self.listener.accept()
            self._clients.append(Client.Client(self, client))
            time.sleep(0.005)  # Don't touch this, if you do your cpu usage rises to like 99.8%

    def hookPacket(self, packet: Packet.Packet, callback):
        """
        :param packet: The non-initialized packet you'd like to hook.
        :param callback: The non-initialized callback function.
        """
        if self._packetHooks.get(packet.__name__):
            self._packetHooks[packet.__name__].append(callback)
        else:
            self._packetHooks[packet.__name__] = [callback]

    def hookCommand(self, command, callback):
        if command in self._commandHooks:
            print("Command already registered. Ignoring...")
        else:
            self._commandHooks[command] = callback

    def sendPacket(self, client, packet, for_client):
        data = bytes(packet.data)
        for key, value in self.packetPointers.items():
            if value and value.__name__ == packet.__class__.__name__:
                packet_id = key
                print(packet_id)
                break
        if for_client:
            header = struct.pack(">ib", len(data) + 5, packet_id) + client.crypto.serverIn(data)
            client.client.send(header)
        else:
            header = struct.pack(">ib", len(data) + 5, packet_id) + client.crypto.clientIn(data)
            client.server.send(header)

    def sendToClient(self, client, packet):
        self.sendPacket(client, packet, True)

    def sendToServer(self, client, packet):
        self.sendPacket(client, packet, False)

    def processClientPacket(self, client, packet):
        # Implement command hooks later
        if packet.__class__.__name__ == "PlayerTextPacket":
            player_text = packet.read()
            if player_text.startswith("/"):
                command_text = player_text.replace("/", "").split(" ")
                for command in self._commandHooks:
                    if command == command_text[0]:
                        self._commandHooks[command](client, command_text[1:])
                        packet.send = False

        # Should call a hooked function
        for packetName in self._packetHooks:
            if packetName == packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    callback(client, packet)

    def processServerPacket(self, client, packet):
        for packetName in self._packetHooks:
            if packetName == packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    callback(client, packet)

    def start(self):
        threading.Thread(target=self.enableSWFPROXY).start()
        threading.Thread(target=self.enableClients).start()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.loadPlugins()
    proxy.start()
