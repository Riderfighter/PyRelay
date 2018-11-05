import socket
import utilities
import struct
import byteio
import packets
import select
# 6a39570cc9de4ec71d64821894c79332b197f92ba85ed281a023
# client to proxy only
crypto = utilities.utils()
crypto.IncomingKey = b'c79332b197f92ba85ed281a023'
crypto.OutgoingKey = b'6a39570cc9de4ec71d64821894'
def formatPackets():
    constantpacketpointers = {'FAILURE': packets.FailurePacket(), 'CREATESUCCESS': packets.CreateSuccessPacket(), 'CREATE': packets.CreatePacket(), 'PLAYERSHOOT': packets.PlayerShootPacket(), 'MOVE': packets.MovePacket(), 'PLAYERTEXT': packets.PlayerTextPacket(), 'TEXT': None, 'SERVERPLAYERSHOOT': None, 'DAMAGE': None, 'UPDATE': None, 'UPDATEACK': packets.UpdateAckPacket(), 'NOTIFICATION': None, 'NEWTICK': packets.NewTickPacket(), 'INVSWAP': packets.InvSwapPacket(), 'USEITEM': packets.UseItemPacket(), 'SHOWEFFECT': None, 'HELLO': packets.HelloPacket(), 'GOTO': None, 'INVDROP': packets.InvDropPacket(), 'INVRESULT': None, 'RECONNECT': None, 'PING': None, 'PONG': packets.PongPacket(), 'MAPINFO': None, 'LOAD': packets.LoadPacket(), 'PIC': None, 'SETCONDITION': packets.SetConditionPacket(), 'TELEPORT': packets.TeleportPacket(), 'USEPORTAL': packets.UsePortal(), 'DEATH': None, 'BUY': packets.BuyPacket(), 'BUYRESULT': None, 'AOE': None, 'GROUNDDAMAGE': packets.GroundDamagePacket(), 'PLAYERHIT': packets.PlayerHitPacket(), 'ENEMYHIT': packets.EnemyHitPacket(), 'AOEACK': packets.AoEAckPacket(), 'SHOOTACK': packets.ShootAckPacket(), 'OTHERHIT': packets.OtherHitPacket(), 'SQUAREHIT': packets.SquareHitPacket(), 'GOTOACK': packets.GotoAckPacket(), 'EDITACCOUNTLIST': packets.EditAccountListPacket(), 'ACCOUNTLIST': None, 'QUESTOBJID': None, 'CHOOSENAME': packets.ChooseNamePacket(), 'NAMERESULT': None, 'CREATEGUILD': packets.CreateGuildPacket(), 'GUILDRESULT': None, 'GUILDREMOVE': packets.GuildRemovePacket(), 'GUILDINVITE': packets.GuildInvitePacket(), 'ALLYSHOOT': None, 'ENEMYSHOOT': None, 'REQUESTTRADE': packets.RequestTradePacket(), 'TRADEREQUESTED': None, 'TRADESTART': None, 'CHANGETRADE': packets.ChangeTradePacket(), 'TRADECHANGED': None, 'ACCEPTTRADE': packets.AcceptTradePacket(), 'CANCELTRADE': packets.CancelTradePacket(), 'TRADEDONE': None, 'TRADEACCEPTED': None, 'CLIENTSTAT': None, 'CHECKCREDITS': packets.CheckCreditsPacket(), 'ESCAPE': packets.EscapePacket(), 'FILE': None, 'INVITEDTOGUILD': None, 'JOINGUILD': packets.JoinGuildPacket(), 'CHANGEGUILDRANK': packets.ChangeGuildRankPacket(), 'PLAYSOUND': None, 'GLOBALNOTIFICATION': None, 'RESKIN': packets.ReskinPacket(), 'PETUPGRADEREQUEST': None, 'ACTIVEPETUPDATEREQUEST': None, 'ACTIVEPETUPDATE': None, 'NEWABILITY': None, 'PETYARDUPDATE': None, 'EVOLVEPET': None, 'DELETEPET': None, 'HATCHPET': None, 'ENTERARENA': packets.EnterArenaPacket(), 'IMMINENTARENAWAVE': None, 'ARENADEATH': None, 'ACCEPTARENADEATH': None, 'VERIFYEMAIL': None, 'RESKINUNLOCK': None, 'PASSWORDPROMPT': None, 'QUESTFETCHASK': None, 'QUESTREDEEM': None, 'QUESTFETCHRESPONSE': None, 'QUESTREDEEMRESPONSE': None, 'PETCHANGEFORMMSG': None, 'KEYINFOREQUEST': packets.KeyInfoRequestPacket(), 'KEYINFORESPONSE': None, 'CLAIMLOGINREWARDMSG': None, 'LOGINREWARDMSG': None, 'QUESTROOMMSG': None}
    newpacketvalues = {}
    d = utilities.packetsetup().setupPacket()
    for packet in d:
        newpacketvalues[d.get(packet)] = constantpacketpointers[packet]
    return newpacketvalues
packetshit = formatPackets()

def sendSocket(socket, socket2, debug=True):
    """
    sends data from socket2 to socket 1
    """
    buf = socket2.recv(1048576) # Receives data from socket2
    if debug:
        if ord(struct.unpack(">c", buf[4:5])[0]) != 74 and packetshit.get(ord(struct.unpack(">c", buf[4:5])[0])):
            newPacket = packetshit.get(ord(struct.unpack(">c", buf[4:5])[0]))
            newPacket.packet.data.extend(crypto.ARC4Decryptout(buf[5:]))
            print(newPacket.packet.data)
            test = newPacket.read()
            print(test)
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
            try:
                client.close()
                server.close()
                listener.close()
            except AttributeError:
                pass

if __name__ == '__main__':
    Route()
# test = packets.PlayerTextPacket()
# test.packet.data.extend(b'\x00\x04test')
# print(test.read())