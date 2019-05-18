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
    arc4_decrypt_in_cipher = None
    arc4_encrypt_in_cipher = None
    arc4_decrypt_out_cipher = None
    arc4_encrypt_out_cipher = None
    _state: State = None
    packetPointers = Utilities.Packetsetup().setupPacket()
    server = None
    running = False
    plugins = []
    _packetHooks = {}
    _commandHooks = {}

    def __init__(self, proxy, client):
        self._proxy = proxy
        self.client = client
        self.arc4_decrypt_in_cipher = ARC4.new(binascii.unhexlify(self.incoming))
        self.arc4_encrypt_in_cipher = ARC4.new(binascii.unhexlify(self.incoming))
        self.arc4_decrypt_out_cipher = ARC4.new(binascii.unhexlify(self.outgoing))
        self.arc4_encrypt_out_cipher = ARC4.new(binascii.unhexlify(self.outgoing))
        self.load_plugins()

    def hook_packet(self, hooked_packet: Packet.Packet, callback):
        """
        :param hooked_packet: The non-initialized packet you'd like to hook.
        :param callback: The non-initialized callback function.
        """
        if self._packetHooks.get(hooked_packet.__name__):
            self._packetHooks[hooked_packet.__name__].append(callback)
        else:
            self._packetHooks[hooked_packet.__name__] = [callback]

    def hook_command(self, command, callback):
        if command in self._commandHooks:
            print("Command already registered. Ignoring...")
        else:
            self._commandHooks[command] = callback

    def load_plugins(self):
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
    def state(self, new_state: state):
        self._state = new_state
        if not self.server:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.connect((new_state.lastServer, new_state.lastPort))
            print(new_state.guid, "starting up: ", self)

    def start(self):
        self.running = True
        self.route()

    def restart_client(self):
        """
        Restarts client by closing the client socket, server socket.
        """
        print("Disposing of client sockets")
        self.server.shutdown(1)
        self.server.close()
        self.client.shutdown(1)
        self.client.close()
        self.running = False

    def read_remote(self, from_client=True):
        """
        sends data from socket2 to socket 1
        """
        sender = self.client if from_client else self.server
        try:
            header = sender.recv(5)  # Receives data from socket2
            if header == b'\xff':
                self.restart_client()
                print("Kill byte received, all hell will break loose.")
                return
            while len(header) != 5:
                header += sender.recv(5 - len(header))
            packet_id = header[4]
            data_length = struct.unpack(">i", header[:4])[
                              0] - 5  # minus 5 to remove the length of the header per new_packet
            # This is to make sure we receive all parts of the data we want to decode/send to the server.
            while len(header[5:]) != data_length:
                header += sender.recv(data_length - len(header[5:]))
            if from_client:
                decoded_data = self.arc4_decrypt_out_cipher.decrypt(header[5:])
                if self.packetPointers.get(packet_id):
                    new_packet = self.packetPointers.get(packet_id)()
                    new_packet.data.extend(decoded_data)
                    self.process_client_packet(new_packet)
                    if not new_packet.send:
                        return
                header = header[:5] + self.arc4_encrypt_out_cipher.encrypt(decoded_data)
            else:
                decoded_data = self.arc4_decrypt_in_cipher.decrypt(header[5:])
                if self.packetPointers.get(packet_id):
                    new_packet = self.packetPointers.get(packet_id)()
                    new_packet.data.extend(decoded_data)
                    self.process_server_packet(new_packet)
                    if not new_packet.send:
                        return
                header = header[:5] + self.arc4_encrypt_in_cipher.encrypt(decoded_data)
            receiver = self.server if from_client else self.client
            receiver.send(header)  # Sends data from socket2 to socket1
        except OSError as e:
            print(e)

    def send_packet(self, packet_to_process, for_client):
        data = bytes(packet_to_process.data)
        packet_id = None
        for key, value in self.packetPointers.items():
            if value and value.__name__ == packet_to_process.__class__.__name__:
                packet_id = key
                break
        if packet_id:
            if for_client:
                header = struct.pack(">ib", len(data) + 5, packet_id) + self.arc4_encrypt_in_cipher.encrypt(data)
                self.client.send(header)
            else:
                header = struct.pack(">ib", len(data) + 5, packet_id) + self.arc4_encrypt_out_cipher.encrypt(data)
                self.server.send(header)
        else:
            print("No packet_to_process id for:", packet_to_process.__class__.__name__)

    def send_to_client(self, new_packet):
        self.send_packet(new_packet, True)

    def send_to_server(self, new_packet):
        self.send_packet(new_packet, False)

    def process_client_packet(self, hooked_packet):
        # Implement command hooks later
        if hooked_packet.__class__.__name__ == "PlayerTextPacket":
            player_text = hooked_packet.read()
            if player_text.startswith("/"):
                command_text = player_text.replace("/", "").split(" ")
                for command in self._commandHooks:
                    if command == command_text[0]:
                        self._commandHooks[command](command_text[1:])
                        hooked_packet.send = False

        # Should call a hooked function
        for packetName in self._packetHooks:
            if packetName == hooked_packet.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    callback(hooked_packet)

    def process_server_packet(self, packet_to_process):
        for packetName in self._packetHooks:
            if packetName == packet_to_process.__class__.__name__:
                for callback in self._packetHooks[packetName]:
                    callback(packet_to_process)

    def route(self):
        # Figure out how to rebind this socket to the reconnect packets ip thing.
        try:
            while self.running:
                if not self.server:
                    read_list = select.select([self.client], [], [])[0]
                else:
                    read_list = select.select([self.client, self.server], [], [])[0]

                if self.client in read_list:
                    self.read_remote(True)
                if self.server in read_list:
                    self.read_remote(False)

        except KeyboardInterrupt:
            self.client.close()
            self.server.close()
        print("Loop successfully exited")
