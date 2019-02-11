import socket
import utilities
import struct
import byteio
import packets
import select
import binascii
# 6a39570cc9de4ec71d64821894c79332b197f92ba85ed281a023
# client to proxy only
packetPointers = utilities.packetsetup().setupPacket()
crypto = utilities.utils(b'6a39570cc9de4ec71d64821894',b'c79332b197f92ba85ed281a023')

def sendSocket(socket, socket2, debug=True):
    """
    sends data from socket2 to socket 1
    """
    header = socket2.recv(5) # Receives data from socket2
    if len(header) > 0:
        packetid = header[4]
        datalength = struct.unpack(">i", header[:4])[0] - 5
        if datalength > 0:
            header += socket2.recv(datalength)
            if debug:
                dedata = crypto.ARC4Decryptout(header[5:])
                if packetPointers.get(packetid):
                    if packetid == 100:
                        Packet = packetPointers.get(packetid)
                        Packet.packet.data.extend(dedata)
                        HelloData = Packet.read()
                        print(HelloData)
                    elif packetid == 59:
                        Packet = packetPointers.get(packetid)
                        Packet.packet.data.extend(dedata)
                        TextData = Packet.read()
                        print(TextData)
        socket.send(header) # Sends data from sockt2 to socket1

def Route():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(('127.0.0.1', 2050))
    listener.listen(1)
    
    client, caddr = listener.accept()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('52.47.150.186', 2050))
    # Figure out how to rebind this socket to the reconnect packets ip thing.
    running = True

    while running:
        try:
            rlist = select.select([client, server], [], [])[0]

            if client in rlist:
                sendSocket(server, client, True)
            if server in rlist and running:
                sendSocket(client, server, False)
        except KeyboardInterrupt:
            client.close()
            server.close()
            listener.close()

if __name__ == '__main__':
    Route()