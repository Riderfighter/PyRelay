import struct
import binascii
import Packet
import Packets
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4
from Crypto.Cipher import PKCS1_OAEP
import os
import base64

class CryptoUtils:
    """
    Takes the client -> server key and the server -> client key in the constructer.
    """
    def __init__(self, outgoing, incoming):
        self.outgoing = outgoing
        self.incoming = incoming
        # self.email = bytearray()
        # self.password = bytearray()
        self.ARC4DecryptinCipher = ARC4.new(binascii.unhexlify(incoming))
        self.ARC4EncryptinCipher = ARC4.new(binascii.unhexlify(incoming))
        self.ARC4DecryptoutCipher = ARC4.new(binascii.unhexlify(outgoing))
        self.ARC4EncryptoutCipher = ARC4.new(binascii.unhexlify(outgoing))
        # self.rsakey = None
    
    # def RSAEncrypt(self, data):
    #     key = RSA.importKey(self.rsakey)
    #     cipher = PKCS1_OAEP.new(key)
    #     return base64.b64encode(cipher.encrypt(data))
    
    # def RSADecrypt(self, data):
    #     key = RSA.importKey(self.rsakey)
    #     cipher = PKCS1_OAEP.new(key)
    #     return cipher.decrypt(base64.b64decode(bytes(data,'utf8')))

    def resetCiphers(self):
        self.ARC4DecryptinCipher = ARC4.new(binascii.unhexlify(self.incoming))
        self.ARC4EncryptinCipher = ARC4.new(binascii.unhexlify(self.incoming))
        self.ARC4DecryptoutCipher = ARC4.new(binascii.unhexlify(self.outgoing))
        self.ARC4EncryptoutCipher = ARC4.new(binascii.unhexlify(self.outgoing))
    
    def serverOut(self, data):
        """Decrypt server Packets"""
        return self.ARC4DecryptinCipher.decrypt(data)
    
    def serverIn(self, data):
        """Encrypt server Packets"""
        return self.ARC4EncryptinCipher.encrypt(data)
    
    def clientOut(self, data):
        """Decrypt client Packets"""
        return self.ARC4DecryptoutCipher.decrypt(data)
    
    def clientIn(self, data):
        """Encrypt client Packets"""
        return self.ARC4EncryptoutCipher.encrypt(data)

class Packetsetup:
    def __init__(self):
        tree = ET.parse(f'{os.path.dirname(os.path.realpath(__file__))}/xmls/Packets.xml')
        self.root = tree.getroot()
        self.output = {}
    
    def setupPacket(self):
        constantpacketpointers = {'FAILURE': Packets.FailurePacket, 'CREATESUCCESS': Packets.CreateSuccessPacket, 'CREATE': Packets.CreatePacket, 'PLAYERSHOOT': Packets.PlayerShootPacket, 'MOVE': Packets.MovePacket, 'PLAYERTEXT': Packets.PlayerTextPacket, 'TEXT': Packets.TextPacket, 'SERVERPLAYERSHOOT': None, 'DAMAGE': None, 'UPDATE': None, 'UPDATEACK': Packets.UpdateAckPacket, 'NOTIFICATION': Packets.NotificationPacket, 'NEWTICK': Packets.NewTickPacket, 'INVSWAP': Packets.InvSwapPacket, 'USEITEM': Packets.UseItemPacket, 'SHOWEFFECT': None, 'HELLO': Packets.HelloPacket, 'GOTO': Packets.GotoPacket, 'INVDROP': Packets.InvDropPacket, 'INVRESULT': Packets.InvResultPacket, 'RECONNECT': Packets.ReconnectPacket, 'PING': None, 'PONG': Packets.PongPacket, 'MAPINFO': None, 'LOAD': Packets.LoadPacket, 'PIC': None, 'SETCONDITION': Packets.SetConditionPacket, 'TELEPORT': Packets.TeleportPacket, 'USEPORTAL': Packets.UsePortal, 'DEATH': None, 'BUY': Packets.BuyPacket, 'BUYRESULT': Packets.BuyResultPacket, 'AOE': Packets.AoEPacket, 'GROUNDDAMAGE': Packets.GroundDamagePacket, 'PLAYERHIT': Packets.PlayerHitPacket, 'ENEMYHIT': Packets.EnemyHitPacket, 'AOEACK': Packets.AoEAckPacket, 'SHOOTACK': Packets.ShootAckPacket, 'OTHERHIT': Packets.OtherHitPacket, 'SQUAREHIT': Packets.SquareHitPacket, 'GOTOACK': Packets.GotoAckPacket, 'EDITACCOUNTLIST': Packets.EditAccountListPacket, 'ACCOUNTLIST': Packets.AccountListPacket, 'QUESTOBJID': None, 'CHOOSENAME': Packets.ChooseNamePacket, 'NAMERESULT': None, 'CREATEGUILD': Packets.CreateGuildPacket, 'GUILDRESULT': None, 'GUILDREMOVE': Packets.GuildRemovePacket, 'GUILDINVITE': Packets.GuildInvitePacket, 'ALLYSHOOT': None, 'ENEMYSHOOT': None, 'REQUESTTRADE': Packets.RequestTradePacket, 'TRADEREQUESTED': None, 'TRADESTART': None, 'CHANGETRADE': Packets.ChangeTradePacket, 'TRADECHANGED': None, 'ACCEPTTRADE': Packets.AcceptTradePacket, 'CANCELTRADE': Packets.CancelTradePacket, 'TRADEDONE': None, 'TRADEACCEPTED': None, 'CLIENTSTAT': Packets.ClientStatPacket, 'CHECKCREDITS': Packets.CheckCreditsPacket, 'ESCAPE': Packets.EscapePacket, 'FILE': Packets.FilePacket, 'INVITEDTOGUILD': Packets.InvitedToGuildPacket, 'JOINGUILD': Packets.JoinGuildPacket, 'CHANGEGUILDRANK': Packets.ChangeGuildRankPacket, 'PLAYSOUND': None, 'GLOBALNOTIFICATION': Packets.GlobalNotificationPacket, 'RESKIN': Packets.ReskinPacket, 'PETUPGRADEREQUEST': None, 'ACTIVEPETUPDATEREQUEST': None, 'ACTIVEPETUPDATE': None, 'NEWABILITY': None, 'PETYARDUPDATE': None, 'EVOLVEPET': None, 'DELETEPET': None, 'HATCHPET': Packets.HatchEggPacket, 'ENTERARENA': Packets.EnterArenaPacket, 'IMMINENTARENAWAVE': None, 'ARENADEATH': None, 'ACCEPTARENADEATH': None, 'VERIFYEMAIL': None, 'RESKINUNLOCK': None, 'PASSWORDPROMPT': None, 'QUESTFETCHASK': None, 'QUESTREDEEM': None, 'QUESTFETCHRESPONSE': None, 'QUESTREDEEMRESPONSE': None, 'PETCHANGEFORMMSG': None, 'KEYINFOREQUEST': Packets.KeyInfoRequestPacket, 'KEYINFORESPONSE': Packets.KeyInfoResponsePacket, 'CLAIMLOGINREWARDMSG': None, 'LOGINREWARDMSG': None, 'QUESTROOMMSG': None}
        thing1 = {}
        output = {}
        for child in self.root:
            thing1[child[0].text] = int(child[1].text)
        for packet in thing1:
            output[thing1.get(packet)] = constantpacketpointers[packet]
        
        return output
