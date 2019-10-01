import base64

from Crypto.Cipher import ARC4
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import Packets


class CryptoUtils:
    """
    Takes the client -> server key and the server -> client key in the constructer.
    """

    def __init__(self, outgoing, incoming):
        self.email = bytearray()
        self.password = bytearray()
        self.outgoing = outgoing
        self.incoming = incoming
        self.ARC4DecryptinCipher = ARC4.new(bytes.fromhex(incoming))
        self.ARC4EncryptinCipher = ARC4.new(bytes.fromhex(incoming))
        self.ARC4DecryptoutCipher = ARC4.new(bytes.fromhex(outgoing))
        self.ARC4EncryptoutCipher = ARC4.new(bytes.fromhex(outgoing))
        self.rsakey = None

    def reset(self):
        self.ARC4DecryptinCipher = ARC4.new(bytes.fromhex(self.incoming))
        self.ARC4EncryptinCipher = ARC4.new(bytes.fromhex(self.incoming))
        self.ARC4DecryptoutCipher = ARC4.new(bytes.fromhex(self.outgoing))
        self.ARC4EncryptoutCipher = ARC4.new(bytes.fromhex(self.outgoing))

    def RSAEncrypt(self, data):
        key = RSA.importKey(self.rsakey)
        cipher = PKCS1_OAEP.new(key)
        return base64.b64encode(cipher.encrypt(data))

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
    def setup_packet(self):
        output = {
            0: Packets.FailurePacket,
            101: Packets.CreateSuccessPacket,
            61: Packets.CreatePacket,
            30: Packets.PlayerShootPacket,
            42: Packets.MovePacket,
            10: Packets.PlayerTextPacket,
            44: Packets.TextPacket,
            12: None,  # ServerPlayerShoot
            75: Packets.DamagePacket,
            62: Packets.UpdatePacket,
            81: Packets.UpdateAckPacket,
            67: Packets.NotificationPacket,
            9: Packets.NewTickPacket,
            19: Packets.InvSwapPacket,
            11: Packets.UseItemPacket,
            13: None,  # ShowEffect
            1: Packets.HelloPacket,
            18: Packets.GotoPacket,
            55: Packets.InvDropPacket,
            95: Packets.InvResultPacket,
            45: Packets.ReconnectPacket,
            8: None,  # Ping
            31: Packets.PongPacket,
            92: Packets.MapInfoPacket,
            57: Packets.LoadPacket,
            83: None,  # Pic
            60: Packets.SetConditionPacket,
            74: Packets.TeleportPacket,
            47: Packets.UsePortal,
            46: Packets.DeathPacket,
            85: Packets.BuyPacket,
            22: Packets.BuyResultPacket,
            64: Packets.AoEPacket,
            103: Packets.GroundDamagePacket,
            90: Packets.PlayerHitPacket,
            25: Packets.EnemyHitPacket,
            89: Packets.AoEAckPacket,
            100: Packets.ShootAckPacket,
            20: Packets.OtherHitPacket,
            40: Packets.SquareHitPacket,
            65: Packets.GotoAckPacket,
            27: Packets.EditAccountListPacket,
            99: Packets.AccountListPacket,
            82: None,  # QuestObjID
            97: Packets.ChooseNamePacket,
            21: None,  # NameResult
            59: Packets.CreateGuildPacket,
            26: Packets.CreateGuildResultPacket,
            15: Packets.GuildRemovePacket,
            104: Packets.GuildInvitePacket,
            49: Packets.AllyShootPacket,
            35: Packets.EnemyShootPacket,
            5: Packets.RequestTradePacket,
            88: None,  # TradeRequested
            86: None,  # TradeStart
            56: Packets.ChangeTradePacket,
            28: None,  # TradeChanged
            36: Packets.AcceptTradePacket,
            91: Packets.CancelTradePacket,
            34: None,  # TradeDone
            14: None,  # TradeAccepted
            69: Packets.ClientStatPacket,
            102: Packets.CheckCreditsPacket,
            105: Packets.EscapePacket,
            106: Packets.FilePacket,
            77: Packets.InvitedToGuildPacket,
            7: Packets.JoinGuildPacket,
            37: Packets.ChangeGuildRankPacket,
            38: None,  # PlaySound
            66: Packets.GlobalNotificationPacket,
            51: Packets.ReskinPacket,
            16: Packets.PetYardCommandPacket,
            24: None,  # ActivePetUpdateRequest
            76: None,  # ActivePetUpdate
            41: None,  # NewAbility
            78: None,  # PetYardUpdate
            87: Packets.PetCommandPacket,
            4: Packets.PetCommandPacket,
            23: Packets.PetCommandPacket,
            17: Packets.EnterArenaPacket,
            50: Packets.ArenaNextWavePacket,
            68: Packets.ArenaDeathPacket,
            80: None,  # AcceptArenaDeath
            39: None,  # VerifyEmail
            107: None,  # ReskinUnlock
            79: None,  # PasswordPrompt
            98: None,  # QuestFetchAsk
            58: None,  # QuestRedeem
            6: None,  # QuestFetchResponse
            96: None,  # QuestRedeemResponse
            53: None,  # PetChangeForm
            94: Packets.KeyInfoRequestPacket,
            63: Packets.KeyInfoResponsePacket,
            3: None,  # ClaimLoginReward
            93: None,  # LoginRewardMsg
            48: None,  # QuestRoomMsg
            33: None,  # PetChangeSkin
            84: None,  # RealmHeroLeft
            52: None,  # ResetDailyQuests
            106: None,  # ChatHelloMSG
            107: None,  # ChatTokenMSG
            108: None  # ChatLogoutMSG
        }
        return output
