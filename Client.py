import socket
# import Packets
import select
import struct
import Utilities
import threading


class Client(object):
    def __init__(self, proxy, client, guid, defaultserver="54.183.236.213"):
        self._proxy = proxy
        self.client = client
        self.guid = guid
        self.lock = threading.Lock()
        self.realConKey = b''
        self.running = True
        self.closed = False
        self.server = None
        self.defaultServer = defaultserver
        self.lastServer = self.defaultServer
        self.defaultPort = 2050
        self.lastPort = self.defaultPort
        self.packetPointers = Utilities.Packetsetup().setupPacket()
        self.crypto = Utilities.CryptoUtils(b'6a39570cc9de4ec71d64821894', b'c79332b197f92ba85ed281a023')
        self.start()

    def start(self):
        self.running = True
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.lastServer, self.lastPort))
        print(self.guid, "starting up")
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

    def readRemote(self, socket, socket2, fromClient=True):
        """
        sends data from socket2 to socket 1
        """
        try:
            header = socket2.recv(5)  # Receives data from socket2
            if len(header) == 0:
                self.restartClient()
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
            socket.send(header)  # Sends data from socket2 to socket1
        except OSError:
            print("Client disconnected.")

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
        print("Loop successfully exited")
