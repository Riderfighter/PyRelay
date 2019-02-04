import socket
import utilities
import struct
import byteio
import packets
import select
# 6a39570cc9de4ec71d64821894c79332b197f92ba85ed281a023
# client to proxy only
packetPointers = utilities.packetsetup().setupPacket()
crypto = utilities.utils()
crypto.IncomingKey = b'c79332b197f92ba85ed281a023'
crypto.OutgoingKey = b'6a39570cc9de4ec71d64821894'

def sendSocket(socket, socket2, debug=True):
    """
    sends data from socket2 to socket 1
    """
    buf = socket2.recv(1048576) # Receives data from socket2
    if debug:
        if len(buf) > 0 and struct.unpack(">b", buf[4:5])[0] not in (102,74,80,) and packetPointers.get(struct.unpack(">b", buf[4:5])[0]):
            if struct.unpack(">b", buf[4:5])[0] == 100:
                Packet = packetPointers.get(struct.unpack(">b", buf[4:5])[0])
                Packet.packet.data.extend(crypto.ARC4Decryptout(buf[5:]))
                HelloData = Packet.read()
                print(HelloData)
                # Packet.packet.reset()
                # Packet.write('X31.1.2',HelloData[1],HelloData[2],HelloData[3],HelloData[4],HelloData[5],HelloData[6],HelloData[7],HelloData[8],HelloData[9],HelloData[10],HelloData[11],HelloData[12],HelloData[13],HelloData[14],HelloData[15])
                # buf = (struct.pack(">i", struct.calcsize(">ib")+len(Packet.packet.data))+struct.pack(">b",100)+crypto.ARC4Encryptout(bytes(Packet.packet.data)))
            else:
                if struct.unpack(">b", buf[4:5])[0] in (59,20, 0):
                    Packet = packetPointers.get(struct.unpack(">b", buf[4:5])[0])
                    Packet.packet.reset()
                    Packet.packet.data.extend(crypto.ARC4Decryptout(buf[5:]))
                    print('DATA IN', bytes(Packet.packet.data))
                    # if Packet.ErrorId == 4:
                    #     print(Packet.ErrorMessage)
    
    socket.send(buf) # Sends data from sockt2 to socket1

def Route():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(('127.0.0.1', 2050))
    listener.listen(1)
    client, caddr = listener.accept()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('54.183.179.205', 2050))
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