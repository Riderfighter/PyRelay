import select
import socket
import struct
import threading

import State
import Utilities


class Client:
    _state: State = None
    crypto = Utilities.CryptoUtils(b'6a39570cc9de4ec71d64821894', b'c79332b197f92ba85ed281a023')
    packetPointers = Utilities.Packetsetup().setupPacket()
    server = None
    running = True

    def __init__(self, proxy, client):
        self._proxy = proxy
        self.client = client
        self.start()

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
        threading.Thread(target=self.Route).start()

    def restartClient(self):
        """
        Restarts client by closing the client socket, server socket.
        """
        print("Disposing of client sockets")
        self.running = False
        self.client.close()
        self.server.close()
        self.crypto.reset()

    def readRemote(self, fromClient=True):
        """
        sends data from socket2 to socket 1
        """
        socket2 = self.client if fromClient else self.server
        try:
            header = socket2.recv(5)  # Receives data from socket2
            if header == b'\xff':
                print("Kill byte received, all hell will break loose.")
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
                    self._proxy.processClientPacket(self, Packet)
                    if not Packet.send:
                        return
                header = header[:5] + self.crypto.clientIn(dedata)
            else:
                dedata = self.crypto.serverOut(header[5:])
                if self.packetPointers.get(packetid):
                    Packet = self.packetPointers.get(packetid)()
                    Packet.data.extend(dedata)
                    self._proxy.processServerPacket(self, Packet)
                    if not Packet.send:
                        return
                header = header[:5] + self.crypto.serverIn(dedata)
            socket1 = self.server if fromClient else self.client
            socket1.send(header)  # Sends data from socket2 to socket1
        except OSError as e:
            print(e)
            print("Client disconnected.")

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
