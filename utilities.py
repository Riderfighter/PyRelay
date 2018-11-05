import struct
import binascii
import byteio
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4
from Crypto.Cipher import PKCS1_OAEP
import base64

class utils:
    def __init__(self):
        self.email = bytearray()
        self.password = bytearray()
        self.OutgoingKey = bytearray()
        self.IncomingKey = bytearray()
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
        cipher = ARC4.new(binascii.unhexlify(self.IncomingKey))
        return cipher.decrypt(data)
    
    def ARC4Encryptin(self, data):
        cipher = ARC4.new(binascii.unhexlify(self.IncomingKey))
        return cipher.encrypt(data)
    
    def ARC4Decryptout(self, data):
        cipher = ARC4.new(binascii.unhexlify(self.OutgoingKey))
        return cipher.decrypt(data)
    
    def ARC4Encryptout(self, data):
        cipher = ARC4.new(binascii.unhexlify(self.OutgoingKey))
        return cipher.encrypt(data)

class packetsetup:
    def __init__(self):
        tree = ET.parse('/Volumes/SCRIPTSPY/Projects/PyRelay/xmls/Packets.xml')
        self.root = tree.getroot()
        self.output = {}
    
    def setupPacket(self):
        d = {}
        for child in self.root:
            # print(child[0].text, child[1].text)
            d[child[0].text] = int(child[1].text)
        return d
    
# test = packetsetup()
# test.setupPacket()