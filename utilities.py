import struct
import binascii
import byteio
import packets
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4
from Crypto.Cipher import PKCS1_OAEP
import os
import base64

class utils:
    def __init__(self, outgoing, incoming):
        self.email = bytearray()
        self.password = bytearray()
        self.ARC4DecryptinCipher = ARC4.new(binascii.unhexlify(incoming))
        self.ARC4EncryptinCipher = ARC4.new(binascii.unhexlify(incoming))
        self.ARC4DecryptoutCipher = ARC4.new(binascii.unhexlify(outgoing))
        self.ARC4EncryptoutCipher = ARC4.new(binascii.unhexlify(outgoing))
        self.rsakey = None
    
    def RSAEncrypt(self, data):
        key = RSA.importKey(self.rsakey)
        cipher = PKCS1_OAEP.new(key)
        return base64.b64encode(cipher.encrypt(data))
    
    def RSADecrypt(self, data):
        key = RSA.importKey(self.rsakey)
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(base64.b64decode(bytes(data,'utf8')))

    def ARC4Decryptin(self, data):
        return self.ARC4DecryptinCipher.decrypt(data)
    
    def ARC4Encryptin(self, data):
        return self.ARC4EncryptinCipher.encrypt(data)
    
    def ARC4Decryptout(self, data):
        return self.ARC4DecryptoutCipher.decrypt(data)
    
    def ARC4Encryptout(self, data):
        return self.ARC4EncryptoutCipher.encrypt(data)

class packetsetup:
    def __init__(self):
        tree = ET.parse(f'{os.path.dirname(os.path.realpath(__file__))}/xmls/Packets.xml')
        self.root = tree.getroot()
        self.output = {}
    
    def setupPacket(self):
        constantpacketpointers = {'FAILURE': packets.FailurePacket(), 'CREATESUCCESS': packets.CreateSuccessPacket(), 'CREATE': packets.CreatePacket(), 'PLAYERSHOOT': packets.PlayerShootPacket(), 'MOVE': packets.MovePacket(), 'PLAYERTEXT': packets.PlayerTextPacket(), 'TEXT': packets.TextPacket(), 'SERVERPLAYERSHOOT': None, 'DAMAGE': None, 'UPDATE': None, 'UPDATEACK': packets.UpdateAckPacket(), 'NOTIFICATION': None, 'NEWTICK': packets.NewTickPacket(), 'INVSWAP': packets.InvSwapPacket(), 'USEITEM': packets.UseItemPacket(), 'SHOWEFFECT': None, 'HELLO': packets.HelloPacket(), 'GOTO': None, 'INVDROP': packets.InvDropPacket(), 'INVRESULT': None, 'RECONNECT': None, 'PING': None, 'PONG': packets.PongPacket(), 'MAPINFO': None, 'LOAD': packets.LoadPacket(), 'PIC': None, 'SETCONDITION': packets.SetConditionPacket(), 'TELEPORT': packets.TeleportPacket(), 'USEPORTAL': packets.UsePortal(), 'DEATH': None, 'BUY': packets.BuyPacket(), 'BUYRESULT': None, 'AOE': None, 'GROUNDDAMAGE': packets.GroundDamagePacket(), 'PLAYERHIT': packets.PlayerHitPacket(), 'ENEMYHIT': packets.EnemyHitPacket(), 'AOEACK': packets.AoEAckPacket(), 'SHOOTACK': packets.ShootAckPacket(), 'OTHERHIT': packets.OtherHitPacket(), 'SQUAREHIT': packets.SquareHitPacket(), 'GOTOACK': packets.GotoAckPacket(), 'EDITACCOUNTLIST': packets.EditAccountListPacket(), 'ACCOUNTLIST': None, 'QUESTOBJID': None, 'CHOOSENAME': packets.ChooseNamePacket(), 'NAMERESULT': None, 'CREATEGUILD': packets.CreateGuildPacket(), 'GUILDRESULT': None, 'GUILDREMOVE': packets.GuildRemovePacket(), 'GUILDINVITE': packets.GuildInvitePacket(), 'ALLYSHOOT': None, 'ENEMYSHOOT': None, 'REQUESTTRADE': packets.RequestTradePacket(), 'TRADEREQUESTED': None, 'TRADESTART': None, 'CHANGETRADE': packets.ChangeTradePacket(), 'TRADECHANGED': None, 'ACCEPTTRADE': packets.AcceptTradePacket(), 'CANCELTRADE': packets.CancelTradePacket(), 'TRADEDONE': None, 'TRADEACCEPTED': None, 'CLIENTSTAT': None, 'CHECKCREDITS': packets.CheckCreditsPacket(), 'ESCAPE': packets.EscapePacket(), 'FILE': None, 'INVITEDTOGUILD': None, 'JOINGUILD': packets.JoinGuildPacket(), 'CHANGEGUILDRANK': packets.ChangeGuildRankPacket(), 'PLAYSOUND': None, 'GLOBALNOTIFICATION': None, 'RESKIN': packets.ReskinPacket(), 'PETUPGRADEREQUEST': None, 'ACTIVEPETUPDATEREQUEST': None, 'ACTIVEPETUPDATE': None, 'NEWABILITY': None, 'PETYARDUPDATE': None, 'EVOLVEPET': None, 'DELETEPET': None, 'HATCHPET': None, 'ENTERARENA': packets.EnterArenaPacket(), 'IMMINENTARENAWAVE': None, 'ARENADEATH': None, 'ACCEPTARENADEATH': None, 'VERIFYEMAIL': None, 'RESKINUNLOCK': None, 'PASSWORDPROMPT': None, 'QUESTFETCHASK': None, 'QUESTREDEEM': None, 'QUESTFETCHRESPONSE': None, 'QUESTREDEEMRESPONSE': None, 'PETCHANGEFORMMSG': None, 'KEYINFOREQUEST': packets.KeyInfoRequestPacket(), 'KEYINFORESPONSE': None, 'CLAIMLOGINREWARDMSG': None, 'LOGINREWARDMSG': None, 'QUESTROOMMSG': None}
        thing1 = {}
        output = {}
        for child in self.root:
            thing1[child[0].text] = int(child[1].text)
        for packet in thing1:
            output[thing1.get(packet)] = constantpacketpointers[packet]
        
        return output
    