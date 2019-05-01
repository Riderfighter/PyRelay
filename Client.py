import binascii
import importlib
import os
import select
import socket
import struct

from Crypto.Cipher import ARC4

import Packet
import State
import Utilities


class Client:
    incoming = b'c79332b197f92ba85ed281a023'
    outgoing = b'6a39570cc9de4ec71d64821894'
    ARC4DecryptinCipher = ARC4.new(binascii.unhexlify(incoming))
    ARC4EncryptinCipher = ARC4.new(binascii.unhexlify(incoming))
    ARC4DecryptoutCipher = ARC4.new(binascii.unhexlify(outgoing))
    ARC4EncryptoutCipher = ARC4.new(binascii.unhexlify(outgoing))
    _state: State = None
    # crypto = Utilities.CryptoUtils(b'6a39570cc9de4ec71d64821894', b'c79332b197f92ba85ed281a023')
    packetPointers = Utilities.Packetsetup().setupPacket()
    server = None
    running = False
    plugins = []
    _packetHooks = {}
    _commandHooks = {}

    def __init__(self, proxy, client):
        self._proxy = proxy
        self.client = client
        self.loadPlugins()

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
            getattr(plugin, i)(self._proxy, self)

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, value: State) -> None:
        if not self.server:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.connect((value.lastServer, value.lastPort))
            print(value.guid, "starting up")
        self._state = value

    def start(self):
        self.running = True
        self.Route()

    def restartClient(self):
        """
        Restarts client by closing the client socket, server socket.
        """
        print("Disposing of client sockets")
        self.running = False
        self.client.close()
        self.server.close()

    def readRemote(self, fromClient=True):
        """
        sends data from socket2 to socket 1
        """
        socket2 = self.client if fromClient else self.server
        try:
            header = socket2.recv(5)  # Receives data from socket2
            if header == b'\xff':
                print("Kill byte received, all hell will break loose.")
                self.restartClient()
                return
            while len(header) != 5:
                header += socket2.recv(5 - len(header))
            packetid = header[4]
            datalength = struct.unpack(">i", header[:4])[0] - 5  # minus 5 to remove the length of the header per packet
            # This is to make sure we receive all parts of the data we want to decode/send to the server.
            while len(header[5:]) != datalength:
                header += socket2.recv(datalength - len(header[5:]))
            if fromClient:
                dedata = self.ARC4DecryptoutCipher.decrypt(header[5:])
                if self.packetPointers.get(packetid):
                    Packet = self.packetPointers.get(packetid)()
                    Packet.data.extend(dedata)
                    self.processClientPacket(Packet)
                    if not Packet.send:
                        return
                header = header[:5] + self.ARC4EncryptoutCipher.encrypt(dedata)
            else:
                dedata = self.ARC4DecryptinCipher.decrypt(header[5:])
                if self.packetPointers.get(packetid):
                    Packet = self.packetPointers.get(packetid)()
                    Packet.data.extend(dedata)
                    self.processServerPacket(Packet)
                    if not Packet.send:
                        return
                header = header[:5] + self.ARC4EncryptinCipher.encrypt(dedata)
            socket1 = self.server if fromClient else self.client
            socket1.send(header)  # Sends data from socket2 to socket1
        except OSError as e:
            print(e)
            print("Client disconnected.")

    def sendPacket(self, packet, for_client):
        data = bytes(packet.data)
        for key, value in self.packetPointers.items():
            if value and value.__name__ == packet.__class__.__name__:
                packet_id = key
                break
        if for_client:
            header = struct.pack(">ib", len(data) + 5, packet_id) + self.ARC4EncryptinCipher.encrypt(data)
            self.client.send(header)
        else:
            header = struct.pack(">ib", len(data) + 5, packet_id) + self.ARC4EncryptoutCipher.encrypt(data)
            self.server.send(header)

    def sendToClient(self, packet):
        self.sendPacket(packet, True)

    def sendToServer(self, packet):
        self.sendPacket(packet, False)

    def processClientPacket(self, packet):
        # Implement command hooks later
        if packet.__class__.__name__ == "PlayerTextPacket":
            player_text = packet.read()
            if player_text.startswith("/"):
                command_text = player_text.replace("/", "").split(" ")
                for command in self._proxy._commandHooks:
                    if command == command_text[0]:
                        self._proxy._commandHooks[command](command_text[1:])
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

    def Route(self):
        # Figure out how to rebind this socket to the reconnect packets ip thing.
        try:
            while self.running:
                if not self.server:
                    rlist = select.select([self.client], [], [])[0]
                else:
                    rlist = select.select([self.client, self.server], [], [])[0]

                if self.client in rlist:
                    self.readRemote(True)
                if self.server in rlist:
                    self.readRemote(False)

        except KeyboardInterrupt:
            self.client.close()
            self.server.close()
        print("Loop successfully exited")
