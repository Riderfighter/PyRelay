import enum
import json

import Datatypes
import Packet


# Client Packets
class AcceptTradePacket(Packet.Packet):
    def __init__(self):
        super(AcceptTradePacket, self).__init__()
        self.myOffers = []
        self.yourOffers = []

    def write(self):
        self.reset()
        self.write_booleanarray(self.myOffers)
        self.write_booleanarray(self.yourOffers)

    def read(self):
        self.myOffers = self.read_booleanarray()
        self.yourOffers = self.read_booleanarray()
        return self.myOffers, self.yourOffers


class AoEAckPacket(Packet.Packet):
    def __init__(self):
        super(AoEAckPacket, self).__init__()
        self.time = 0
        self.position = Datatypes.Location(self)

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.position.write()

    def read(self):
        self.time = self.read_int32()
        self.position.read()
        return self.time, self.position


class BuyPacket(Packet.Packet):
    def __init__(self):
        super(BuyPacket, self).__init__()
        self.objectId = 0
        self.quantitiy = 0

    def write(self):
        self.reset()
        self.write_int32(self.objectId)
        self.write_int32(self.quantitiy)

    def read(self):
        self.objectId = self.read_int32()
        self.quantitiy = self.read_int32()
        return self.objectId, self.quantitiy


class CancelTradePacket(Packet.Packet):
    def __init__(self):
        super(CancelTradePacket, self).__init__()

    def write(self):
        pass

    def read(self):
        pass


class ChangeGuildRankPacket(Packet.Packet):
    def __init__(self):
        super(ChangeGuildRankPacket, self).__init__()
        self.name = ''
        self.guildRank = 0

    def write(self):
        self.reset()
        self.write_string(self.name)
        self.write_int32(self.guildrank)

    def read(self):
        self.name = self.read_string()
        self.guildRank = self.read_int32()
        return self.name, self.guildRank


class ChangeTradePacket(Packet.Packet):
    def __init__(self):
        super(ChangeTradePacket, self).__init__()
        self.offers = []

    def write(self):
        self.reset()
        self.write_booleanarray(self.offers)

    def read(self):
        self.offers = self.read_booleanarray()
        return self.offers


class CheckCreditsPacket(Packet.Packet):
    def __init__(self):
        super(CheckCreditsPacket, self).__init__()

    def write(self):
        pass

    def read(self):
        pass


class ChooseNamePacket(Packet.Packet):
    def __init__(self):
        super(ChooseNamePacket, self).__init__()
        self.name = ''

    def write(self):
        self.reset()
        self.write_string(self.name)

    def read(self):
        self.name = self.read_string()
        return self.name


class CreateGuildPacket(Packet.Packet):
    def __init__(self):
        super(CreateGuildPacket, self).__init__()
        self.name = ''

    def write(self):
        self.reset()
        self.write_string(self.name)

    def read(self):
        self.name = self.read_string()


class CreatePacket(Packet.Packet):
    def __init__(self):
        super(CreatePacket, self).__init__()
        self.classType = 0
        self.skinType = 0

    def write(self):
        self.reset()
        self.write_uint16(self.classType)
        self.write_uint16(self.skinType)

    def read(self):
        self.classType = self.read_uint16()
        self.skinType = self.read_uint16()
        return self.classType, self.skinType


class EditAccountListPacket(Packet.Packet):
    def __init__(self):
        super(EditAccountListPacket, self).__init__()
        self.accountlistId = 0
        self.add = None
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_int32(self.accountlistId)
        self.write_boolean(self.add)
        self.write_int32(self.objectId)

    def read(self):
        self.accountlistId = self.read_int32()
        self.add = self.read_boolean()
        self.objectId = self.read_int32()
        return self.accountlistId, self.add, self.objectId


class EnemyHitPacket(Packet.Packet):
    def __init__(self):
        super(EnemyHitPacket, self).__init__()
        self.time = 0
        self.bulletid = ''
        self.targetid = 0
        self.killed = None

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.write_byte(self.bulletid)
        self.write_int32(self.targetid)
        self.write_boolean(self.killed)

    def read(self):
        self.time = self.read_int32()
        self.bulletid = self.read_byte()
        self.targetid = self.read_int32()
        self.killed = self.read_boolean()
        return self.time, self.bulletid, self.targetid, self.killed


class EnterArenaPacket(Packet.Packet):
    def __init__(self):
        super(EnterArenaPacket, self).__init__()
        self.currency = 0

    def write(self):
        self.reset()
        self.write_int32(self.currency)

    def read(self):
        self.currency = self.read_int32()
        return self.currency


class EscapePacket(Packet.Packet):
    def __init__(self):
        super(EscapePacket, self).__init__()

    def write(self):
        pass

    def read(self):
        pass


class GotoAckPacket(Packet.Packet):
    def __init__(self):
        super(GotoAckPacket, self).__init__()
        self.time = 0

    def write(self):
        self.reset()
        self.write_int32(self.time)

    def read(self):
        self.time = self.read_int32()
        return self.time


class GroundDamagePacket(Packet.Packet):
    def __init__(self):
        super(GroundDamagePacket, self).__init__()
        self.time = 0
        self.position: Datatypes.Location = None

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.position.write()

    def read(self):
        self.time = self.read_int32()
        self.position = Datatypes.Location(self)
        self.position.read()
        return self.time, self.position


class GuildInvitePacket(Packet.Packet):
    def __init__(self):
        super(GuildInvitePacket, self).__init__()
        self.name = ''

    def write(self):
        self.reset()
        self.write_string(self.name)

    def read(self):
        self.name = self.read_string()
        return self.name


class GuildRemovePacket(Packet.Packet):
    def __init__(self):
        super(GuildRemovePacket, self).__init__()
        self.name = ''

    def write(self):
        self.reset()
        self.write_string(self.name)

    def read(self):
        self.name = self.read_string()
        return self.name


class HelloPacket(Packet.Packet):
    def __init__(self):
        super(HelloPacket, self).__init__()
        self.buildVersion = ''
        self.gameId = 0
        self.GUID = ''
        self.random1 = 0
        self.password = ''
        self.random2 = 0
        self.secret = ''
        self.keyTime = 0
        self.key = []
        self.mapjsonlen = 0
        self.mapjson = ''
        self.entryTag = ''
        self.gameNet = ''
        self.gamenetuserId = ''
        self.playPlatform = ''
        self.platformToken = ''
        self.userToken = ''

    def write(self):
        self.reset()
        self.write_string(self.buildVersion)
        self.write_int32(self.gameId)
        self.write_string(self.GUID)
        self.write_int32(self.random1)
        self.write_string(self.password)
        self.write_int32(self.random2)
        self.write_string(self.secret)
        self.write_int32(self.keyTime)
        self.write_bytestring(self.key)
        self.write_int32(self.mapjsonlen)
        self.data[self.index:self.advance(self.mapjsonlen)] = self.mapjson
        self.write_string(self.entryTag)
        self.write_string(self.gameNet)
        self.write_string(self.gamenetuserId)
        self.write_string(self.playPlatform)
        self.write_string(self.platformToken)
        self.write_string(self.userToken)
        self.write_string("XTeP7hERdchV5jrBZEYNebAqDPU6tKU6")

    def read(self):
        self.buildVersion = self.read_string()
        self.gameId = self.read_int32()
        self.GUID = self.read_string()
        self.random1 = self.read_int32()
        self.password = self.read_string()
        self.random2 = self.read_int32()
        self.secret = self.read_string()
        self.keyTime = self.read_int32()
        self.key = self.read_bytestring()
        self.mapjsonlen = self.read_int32()
        self.mapjson = self.data[self.index:self.advance(self.mapjsonlen)]
        self.entryTag = self.read_string()
        self.gameNet = self.read_string()
        self.gamenetuserId = self.read_string()
        self.playPlatform = self.read_string()
        self.platformToken = self.read_string()
        self.userToken = self.read_string()
        return self.buildVersion, self.gameId, self.GUID, self.random1, self.password, self.random2, self.secret, self.keyTime, self.key, self.mapjson, self.entryTag, self.gameNet, self.gamenetuserId, self.playPlatform, self.platformToken, self.userToken


class InvDropPacket(Packet.Packet):
    def __init__(self):
        super(InvDropPacket, self).__init__()
        self.slot: Datatypes.SlotObject = None

    def write(self):
        self.reset()
        self.slot.write()

    def read(self):
        self.slot = Datatypes.SlotObject(self)
        self.slot.read()
        return self.slot


class InvSwapPacket(Packet.Packet):
    def __init__(self):
        super(InvSwapPacket, self).__init__()
        self.time = 0
        self.location: Datatypes.Location = None
        self.slotobject1: Datatypes.SlotObject = None
        self.slotobject2: Datatypes.SlotObject = None

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.location.write()
        self.slotobject1.write()
        self.slotobject2.write()

    def read(self):
        self.time = self.read_int32()
        self.location = Datatypes.Location(self)
        self.location.read()
        self.slotobject1 = Datatypes.SlotObject(self)
        self.slotobject1.read()
        self.slotobject2 = Datatypes.SlotObject(self)
        self.slotobject2.read()
        return self.time, self.location, self.slotobject1, self.slotobject2


class JoinGuildPacket(Packet.Packet):
    def __init__(self):
        super(JoinGuildPacket, self).__init__()
        self.guildName = ''

    def write(self):
        self.reset()
        self.write_string(self.guildName)

    def read(self):
        self.guildName = self.read_string()
        return self.guildName


class KeyInfoRequestPacket(Packet.Packet):
    def __init__(self):
        super(KeyInfoRequestPacket, self).__init__()
        self.request = []

    def write(self):
        self.reset()
        self.write_bytestring(self.request)

    def read(self):
        self.request = self.read_bytestring()


class LeaveArenaPacket(Packet.Packet):
    def __init__(self):
        super(LeaveArenaPacket, self).__init__()
        self.time = 0

    def write(self):
        self.reset()
        self.write_int32(self.time)

    def read(self):
        self.time = self.read_int32()
        return self.time


class LoadPacket(Packet.Packet):
    def __init__(self):
        super(LoadPacket, self).__init__()
        self.characterId = 0
        self.isfromArena = False

    def write(self):
        self.reset()
        self.write_int32(self.characterId)
        self.write_boolean(self.isfromArena)

    def read(self):
        self.characterId = self.read_int32()
        self.isfromArena = self.read_boolean()
        return self.characterId, self.isfromArena


class MovePacket(Packet.Packet):
    def __init__(self):
        super(MovePacket, self).__init__()
        self.tickId = 0
        self.time = 0
        self.new_position: Datatypes.Location = None
        self.records = []

    def write(self):
        self.reset()
        self.write_int32(self.tickId)
        self.write_int32(self.time)
        self.new_position.write()
        self.write_int16(len(self.records))
        for record in self.records:
            record.write()

    def read(self):
        self.tickId = self.read_int32()
        self.time = self.read_int32()
        self.new_position = Datatypes.Location(self)
        self.new_position.read()
        self.records = [None] * self.read_int16()
        for _ in range(len(self.records)):
            moverec = Datatypes.MoveRecord(self)
            moverec.read()
            self.records[_] = moverec
        return self.tickId, self.time, self.new_position, self.records


class OtherHitPacket(Packet.Packet):
    def __init__(self):
        super(OtherHitPacket, self).__init__()
        self.time = 0
        self.bulletId = ''
        self.objectId = 0
        self.targetId = 0

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.write_byte(self.bulletId)
        self.write_int32(self.objectId)
        self.write_int32(self.targetId)

    def read(self):
        self.time = self.read_int32()
        self.bulletId = self.read_byte()
        self.objectId = self.read_int32()
        self.targetId = self.read_int32()
        return self.time, self.bulletId, self.objectId, self.targetId


class PetCommandPacket(Packet.Packet):
    def __init__(self):
        super(PetCommandPacket, self).__init__()
        self.commands = {'FOLLOW_PET': 1, 'UNFOLLOW_PET': 2, 'RELEASE_PET': 3}
        self.commandId = 0
        self.petId = 0

    def write(self):
        self.reset()
        self.write_byte(self.commandId)
        self.write_int32(self.petId)

    def read(self):
        self.commandId = self.read_byte()
        self.petId = self.read_int32()
        return self.commandId, self.petId


class PetYardCommandPacket(Packet.Packet):
    def __init__(self):
        super(PetYardCommandPacket, self).__init__()
        self.commands = {'UPGRADE_PET_YARD': 1, 'FEED_PET': 2, 'FUSE_PET': 3}
        self.commandId = 0
        self.petId1 = 0
        self.petId2 = 0
        self.objectId = 0
        self.slotobject: Datatypes.SlotObject = None
        self.currency = 0

    def write(self):
        self.reset()
        self.write_byte(self.commandId)
        self.write_int32(self.petId1)
        self.write_int32(self.petId2)
        self.write_int32(self.objectId)
        self.slotobject.write()
        self.write_byte(self.currency)

    def read(self):
        self.commandId = self.read_byte()
        self.petId1 = self.read_int32()
        self.petId2 = self.read_int32()
        self.objectId = self.read_int32()
        self.slotobject = Datatypes.SlotObject(self)
        self.slotobject.read()
        self.currency = self.read_byte()
        return self.commandId, self.petId1, self.petId2, self.objectId, self.slotobject, self.currency


class PlayerHitPacket(Packet.Packet):
    def __init__(self):
        super(PlayerHitPacket, self).__init__()
        self.bulletId = ''
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_byte(self.bulletId)
        self.write_int32(self.objectId)

    def read(self):
        self.bulletId = self.read_byte()
        self.objectId = self.read_int32()
        return self.bulletId, self.objectId


class PlayerShootPacket(Packet.Packet):
    def __init__(self):
        super(PlayerShootPacket, self).__init__()
        self.time = 0
        self.bulletId = 0
        self.containerType = 0
        self.position: Datatypes.Location = None
        self.angle = 0.0

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.write_byte(self.bulletId)
        self.write_int16(self.containerType)
        self.position.write()
        self.write_float(self.angle)

    def read(self):
        self.time = self.read_int32()
        self.bulletId = self.read_byte()
        self.containerType = self.read_int16()
        self.position = Datatypes.Location(self)
        self.position.read()
        self.angle = self.read_float()
        return self.time, self.bulletId, self.containerType, self.position, self.angle


class PlayerTextPacket(Packet.Packet):
    def __init__(self):
        super(PlayerTextPacket, self).__init__()
        self.text = ''

    def write(self):
        self.reset()
        self.write_string(self.text)

    def read(self):
        self.text = self.read_string()
        return self.text


class PongPacket(Packet.Packet):
    def __init__(self):
        super(PongPacket, self).__init__()
        self.time = 0
        self.serial = 0

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.write_int32(self.serial)

    def read(self):
        self.time = self.read_int32()
        self.serial = self.read_int32()
        return self.time, self.serial


class RequestTradePacket(Packet.Packet):
    def __init__(self):
        super(RequestTradePacket, self).__init__()
        self.name = ''

    def write(self):
        self.reset()
        self.write_string(self.name)

    def read(self):
        self.name = self.read_string()
        return self.name


class ReskinPacket(Packet.Packet):
    def __init__(self):
        super(ReskinPacket, self).__init__()
        self.skinId = 0

    def write(self):
        self.reset()
        self.write_int32(self.skinId)

    def read(self):
        self.skinId = self.read_int32()
        return self.skinId


class ReskinPetPacket(Packet.Packet):
    def __init__(self):
        super(ReskinPetPacket, self).__init__()
        self.newpetType = 0
        self.item: Datatypes.Item = None

    def write(self):
        self.reset()
        self.write_int32(self.newpetType)
        self.item.write()

    def read(self):
        self.newpetType = self.read_int32()
        self.item = Datatypes.Item(self)
        self.item.read()
        return self.newpetType, self.item


class SetConditionPacket(Packet.Packet):
    def __init__(self):
        super(SetConditionPacket, self).__init__()
        self.conditionEffect = ''
        self.conditionDuration = 0.0

    def write(self):
        self.reset()
        self.write_byte(self.conditionEffect)
        self.write_int16(self.conditionDuration)

    def read(self):
        self.conditionEffect = self.read_byte()
        self.conditionDuration = self.read_int16()
        return self.conditionEffect, self.conditionDuration


class ShootAckPacket(Packet.Packet):
    def __init__(self):
        super(ShootAckPacket, self).__init__()
        self.time = 0

    def write(self):
        self.reset()
        self.write_int32(self.time)

    def read(self):
        self.time = self.read_int32()
        return self.time


class SquareHitPacket(Packet.Packet):
    def __init__(self):
        super(SquareHitPacket, self).__init__()
        self.time = 0
        self.bulletId = ''
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.write_byte(self.bulletId)
        self.write_int32(self.objectId)

    def read(self):
        self.time = self.read_int32()
        self.bulletId = self.read_byte()
        self.objectId = self.read_int32()
        return self.time, self.bulletId, self.objectId


class TeleportPacket(Packet.Packet):
    def __init__(self):
        super(TeleportPacket, self).__init__()
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_int32(self.objectId)

    def read(self):
        self.objectId = self.read_int32()
        return self.objectId


class TinkerQuestPacket(Packet.Packet):
    def __init__(self):
        super(TinkerQuestPacket, self).__init__()
        self.slot: Datatypes.SlotObject = None

    def write(self):
        self.reset()
        self.slot.write()

    def read(self):
        self.slot = Datatypes.SlotObject(self)
        self.slot.read()
        return self.slot


class UpdateAckPacket(Packet.Packet):
    def __init__(self):
        super(UpdateAckPacket, self).__init__()

    def write(self):
        pass

    def read(self):
        pass
    # return self.data


class UseItemPacket(Packet.Packet):
    def __init__(self):
        super(UseItemPacket, self).__init__()
        self.time = 0
        self.slotObject: Datatypes.SlotObject = None
        self.itemUsePos: Datatypes.Location = None
        self.useType = ''

    def write(self):
        self.reset()
        self.write_int32(self.time)
        self.slotObject.write()
        self.itemUsePos.write()
        self.write_byte(self.useType)

    def read(self):
        self.time = self.read_int32()
        self.slotObject = Datatypes.SlotObject(self)
        self.slotObject.read()
        self.itemUsePos = Datatypes.Location(self)
        self.itemUsePos.read()
        self.useType = self.read_byte()
        return self.time, self.slotObject, self.itemUsePos, self.useType


class UsePortal(Packet.Packet):
    def __init__(self):
        super(UsePortal, self).__init__()
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_int32(self.objectId)

    def read(self):
        self.objectId = self.read_int32()


class ViewQuestsPacket(Packet.Packet):
    def __init__(self):
        super(ViewQuestsPacket, self).__init__()

    def write(self):
        pass

    def read(self):
        pass


# Server packets?

class UpdatePacket(Packet.Packet):
    tiles = []
    newobjs = []
    drops = []

    def __init__(self):
        super(UpdatePacket, self).__init__()

    def read(self):
        self.tiles = [None] * self.read_int16()
        for _ in range(len(self.tiles)):
            tile = Datatypes.Tile(self)
            tile.read()
            self.tiles[_] = tile
        self.newobjs = [None] * self.read_int16()
        for _ in range(len(self.newobjs)):
            entity = Datatypes.Entity(self)
            entity.read()
            self.newobjs[_] = entity
        self.drops = [None] * self.read_int16()
        for _ in range(len(self.drops)):
            self.drops[_] = self.read_int32()

    def write(self):
        self.reset()
        self.write_int16(len(self.tiles))
        for tile in self.tiles:
            tile.write()
        self.write_int16(len(self.newobjs))
        for entity in self.newobjs:
            entity.write()
        self.write_int16(len(self.drops))
        for drop in self.drops:
            self.write_int32(drop)


class TextPacket(Packet.Packet):
    def __init__(self):
        super(TextPacket, self).__init__()
        self.name = ""
        self.objectid = 0
        self.numstars = 0
        self.bubbletime = 0
        self.recipient = ""
        self.text = ""
        self.cleantext = ""
        self.isSupporter = False

    def write(self):
        self.reset()
        self.write_string(self.name)
        self.write_int32(self.objectid)
        self.write_int32(self.numstars)
        self.write_byte(self.bubbletime)
        self.write_string(self.recipient)
        self.write_string(self.text)
        self.write_string(self.cleantext)
        self.write_boolean(self.isSupporter)

    def read(self):
        self.name = self.read_string()
        self.objectid = self.read_int32()
        self.numstars = self.read_int32()
        self.bubbletime = self.read_byte()
        self.recipient = self.read_string()
        self.text = self.read_string()
        self.cleantext = self.read_string()
        self.isSupporter = self.read_boolean()
        return self.name, self.objectid, self.numstars, self.bubbletime, self.recipient, self.text, self.cleantext


class AccountListPacket(Packet.Packet):
    def __init__(self):
        super(AccountListPacket, self).__init__()
        self.accountlistId = 0
        self.accountIds = []
        self.lockAction = 0

    def write(self):
        self.reset()
        self.write_int32(self.accountlistId)
        self.write_int16(len(self.accountIds))
        for x in self.accountIds:
            self.write_string(x)
        self.write_int32(self.lockAction)

    def read(self):
        self.accountlistId = self.read_int32()
        self.accountIds = [None] * self.read_int16()
        for x in range(len(self.accountIds)):
            self.accountIds[x] = self.read_string()
        self.lockAction = self.read_int32()
        return self.accountlistId, self.accountIds, self.lockAction


class AllyShootPacket(Packet.Packet):
    def __init__(self):
        super(AllyShootPacket, self).__init__()
        self.bulletId = ''
        self.ownerId = 0
        self.containerType = 0
        self.angle = 0.0

    def write(self):
        self.reset()
        self.write_byte(self.bulletId)
        self.write_int32(self.ownerId)
        self.write_int16(self.containerType)
        self.write_float(self.angle)

    def read(self):
        self.bulletId = self.read_byte()
        self.ownerId = self.read_int32()
        self.containerType = self.read_int16()
        self.angle = self.read_float()
        return self.bulletId, self.ownerId, self.containerType, self.angle


class AoEPacket(Packet.Packet):
    def __init__(self):
        super(AoEPacket, self).__init__()
        self.location: Datatypes.Location = None
        self.radius = 0.0
        self.damage = 0
        self.effects = 0
        self.effectDuration = 0.0
        self.originType = 0
        self.color = 0
        self.armorPierce = False

    def write(self):
        self.reset()
        self.location.write()
        self.write_float(self.radius)
        self.write_uint16(self.damage)
        self.write_unsignedbyte(self.effects)
        self.write_float(self.effectDuration)
        self.write_uint16(self.originType)
        self.write_int32(self.color)
        self.write_boolean(self.armorPierce)

    def read(self):
        self.location = Datatypes.Location(self)
        self.location.read()
        self.radius = self.read_float()
        self.damage = self.read_uint16()
        self.effects = self.read_unsignedbyte()
        self.effectDuration = self.read_float()
        self.originType = self.read_uint16()
        self.color = self.read_int32()
        self.armorPierce = self.read_boolean()
        return self.location, self.radius, self.damage, self.effects, self.effectDuration, self.originType, self.color, self.armorPierce


class ArenaDeathPacket(Packet.Packet):
    def __init__(self):
        super(ArenaDeathPacket, self).__init__()
        self.restartPrice = 0

    def write(self):
        self.reset()
        self.write_int32(self.restartPrice)

    def read(self):
        self.restartPrice = self.read_int32()


class ArenaNextWavePacket(Packet.Packet):
    def __init__(self):
        super(ArenaNextWavePacket, self).__init__()
        self.typeId = 0

    def write(self):
        self.reset()
        self.write_int32(self.typeId)

    def read(self):
        self.typeId = self.read_int32()
        return self.typeId


class BuyResultPacket(Packet.Packet):
    def __init__(self):
        super(BuyResultPacket, self).__init__()
        self.result = 0
        self.message = ''

    def write(self):
        self.reset()
        self.write_int32(self.result)
        self.write_string(self.message)

    def read(self):
        self.result = self.read_int32()
        self.message = self.read_string()
        return self.result, self.message


class ClientStatPacket(Packet.Packet):
    def __init__(self):
        super(ClientStatPacket, self).__init__()
        self.name = ''
        self.value = 0

    def write(self):
        self.reset()
        self.write_string(self.name)
        self.write_int32(self.value)

    def read(self):
        self.name = self.read_string()
        self.value = self.read_int32()
        return self.name, self.value


class CreateGuildResultPacket(Packet.Packet):
    def __init__(self):
        super(CreateGuildResultPacket, self).__init__()
        self.success = False
        self.errorText = ''

    def write(self):
        self.reset()
        self.write_boolean(self.success)
        self.write_string(self.errorText)

    def read(self):
        self.success = self.read_boolean()
        self.errorText = self.read_string()
        return self.success, self.errorText


class CreateSuccessPacket(Packet.Packet):
    def __init__(self):
        super(CreateSuccessPacket, self).__init__()
        self.charId = 0
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_int32(self.objectId)
        self.write_int32(self.charId)

    def read(self):
        self.objectId = self.read_int32()
        self.charId = self.read_int32()
        return self.objectId, self.charId


class DamagePacket(Packet.Packet):
    def __init__(self):
        super(DamagePacket, self).__init__()
        self.targetId = 0
        self.effects = []
        self.damage = 0.0
        self.killed = False
        self.armorPierce = False
        self.bulletId = 0
        self.objectId = 0

    def write(self):
        self.reset()
        self.write_int32(self.targetId)
        self.write_unsignedbyte(len(self.effects))
        for effect in self.effects:
            self.write_unsignedbyte(effect)
        self.write_uint16(self.damage)
        self.write_boolean(self.killed)
        self.write_boolean(self.armorPierce)
        self.write_unsignedbyte(self.bulletId)
        self.write_int32(self.objectId)

    def read(self):
        self.targetId = self.read_int32()
        for _ in range(self.read_unsignedbyte()):
            self.effects.append(self.read_unsignedbyte())
        self.damage = self.read_uint16()
        self.killed = self.read_boolean()
        self.armorPierce = self.read_boolean()
        self.bulletId = self.read_unsignedbyte()
        self.objectId = self.read_int32()

class DeathPacket(Packet.Packet):
    def __init__(self):
        super(DeathPacket, self).__init__()
        self.accountId = ''
        self.charId = 0
        self.killedBy = ''
        self.zombieType = 0
        self.zombieId = 0

    def write(self):
        self.reset()
        self.write_string(self.accountId)
        self.write_int32(self.charId)
        self.write_string(self.killedBy)
        self.write_int32(self.zombieType)
        self.write_int32(self.zombieId)

    def read(self):
        self.accountId = self.read_string()
        self.charId = self.read_int32()
        self.killedBy = self.read_string()
        self.zombieType = self.read_int32()
        self.zombieId = self.read_int32()
        return self.accountId, self.charId, self.killedBy, self.zombieType, self.zombieId


class EnemyShootPacket(Packet.Packet):
    def __init__(self):
        super(EnemyShootPacket, self).__init__()
        self.bulletId = 0
        self.ownerId = 0
        self.bulletType = 0
        self.startingPos: Datatypes.Location = None
        self.angle = 0.0
        self.damage = 0
        self.numShots = 1
        self.angleInc = 0

    def write(self):
        self.reset()
        self.write_unsignedbyte(self.bulletId)
        self.write_int32(self.ownerId)
        self.write_unsignedbyte(self.bulletType)
        self.startingPos.write()
        self.write_float(self.angle)
        self.write_int16(self.damage)
        if self.numShots != 1:
            self.write_unsignedbyte(self.numShots)
            self.write_float(self.angleInc)

    def read(self):
        self.bulletId = self.read_unsignedbyte()
        self.ownerId = self.read_int32()
        self.bulletType = self.read_unsignedbyte()
        self.startingPos = Datatypes.Location(self)
        self.startingPos.read()
        self.angle = self.read_float()
        self.damage = self.read_int16()
        if len(self.data[self.index:]) > 0:
            self.numShots = self.read_unsignedbyte()
            self.angleInc = self.read_float()
        return self.bulletType, self.ownerId, self.bulletType, self.startingPos, self.angle, self.damage, self.numShots, self.angleInc


class FailurePacket(Packet.Packet):
    class failures(enum.IntEnum):
        portal_error = 0
        incorrect_version = 4
        bad_key = 5
        invalid_teleport_target = 6
        email_verification_needed = 7
        teleport_realm_block = 9

    def __init__(self):
        super(FailurePacket, self).__init__()
        self.errorId = 0
        self.errorMessage = ''

    def write(self):
        self.reset()
        self.write_int32(self.errorId)
        self.write_string(self.errorMessage)

    def read(self):
        self.errorId = self.read_int32()
        self.errorMessage = self.read_string()
        return self.errorId, self.errorMessage


class NewTickPacket(Packet.Packet):
    def __init__(self):
        super(NewTickPacket, self).__init__()
        self.tickId = 0
        self.tickTime = 0
        self.statuses = []

    def write(self):
        self.reset()
        self.write_int32(self.tickId)
        self.write_int32(self.tickTime)
        self.write_int16(len(self.statuses))
        for status in self.statuses:
            status.write()

    def read(self):
        self.tickId = self.read_int32()
        self.tickTime = self.read_int32()
        self.statuses = [None] * self.read_int16()
        for _ in range(len(self.statuses)):
            status = Datatypes.Status(self)
            status.read()
            self.statuses[_] = status
        return self.tickId, self.tickTime, self.statuses


class FilePacket(Packet.Packet):
    def __init__(self):
        super(FilePacket, self).__init__()
        self.name = ''
        self.bytes = b''

    def write(self):
        self.reset()
        self.write_string(self.name)
        self.write_bytestring(self.bytes)

    def read(self):
        self.name = self.read_string()
        self.bytes = self.read_bytestring()
        return self.name, self.bytes


class GlobalNotificationPacket(Packet.Packet):
    def __init__(self):
        super(GlobalNotificationPacket, self).__init__()
        self.typeId = 0
        self.text = ''

    def write(self):
        self.reset()
        self.write_int32(self.typeId)
        self.write_string(self.text)

    def read(self):
        self.typeId = self.read_int32()
        self.text = self.read_string()
        return self.typeId, self.text


class NotificationPacket(Packet.Packet):
    def __init__(self):
        super(NotificationPacket, self).__init__()
        self.objectId = 0
        self.message = {"key": "blank", "tokens": {"data": ""}}
        self.color = 0

    def write(self):
        self.reset()
        self.write_int32(self.objectId)
        self.write_string(json.dumps(self.message, separators=(',', ':')))
        self.write_int32(self.color)

    def read(self):
        self.objectId = self.read_int32()
        self.message = json.loads(self.read_string())
        self.color = self.read_int32()
        return self.objectId, self.message, self.color


class GotoPacket(Packet.Packet):
    def __init__(self):
        super(GotoPacket, self).__init__()
        self.objectId = 0
        self.location: Datatypes.Location = None

    def write(self):
        self.reset()
        self.write_int32(self.objectId)
        self.location.write()

    def read(self):
        self.objectId = self.read_int32()
        self.location = Datatypes.Location(self)
        self.location.read()
        return self.objectId, self.location


class HatchEggPacket(Packet.Packet):
    def __init__(self):
        super(HatchEggPacket, self).__init__()
        self.petName = ''
        self.petSkinId = 0

    def write(self):
        self.reset()
        self.write_string(self.petName)
        self.write_int32(self.petSkinId)

    def read(self):
        self.petName = self.read_string()
        self.petSkinId = self.read_int32()
        return self.petName, self.petSkinId


class InvResultPacket(Packet.Packet):
    def __init__(self):
        super(InvResultPacket, self).__init__()
        self.result = 0

    def write(self):
        self.reset()
        self.write_int32(self.result)

    def read(self):
        self.result = self.read_int32()
        return self.result


class InvitedToGuildPacket(Packet.Packet):
    def __init__(self):
        super(InvitedToGuildPacket, self).__init__()
        self.name = ''
        self.guildName = ''

    def write(self):
        self.reset()
        self.write_string(self.name)
        self.write_string(self.guildName)

    def read(self):
        self.name = self.read_string()
        self.guildName = self.read_string()
        return self.name, self.guildName


class KeyInfoResponsePacket(Packet.Packet):
    def __init__(self):
        super(KeyInfoResponsePacket, self).__init__()
        self.response = b''

    def write(self):
        self.reset()
        self.write_bytestring(self.response)

    def read(self):
        self.response = self.read_bytestring()
        return self.response


class ReconnectPacket(Packet.Packet):
    def __init__(self):
        super(ReconnectPacket, self).__init__()
        self.name = ''
        self.host = ''
        self.stats = ''
        self.port = 0
        self.gameId = 0
        self.keyTime = 0
        self.isFromArena = None
        self.key = b''

    def write(self):
        self.reset()
        self.write_string(self.name)
        self.write_string(self.host)
        self.write_string(self.stats)
        self.write_int32(self.port)
        self.write_int32(self.gameId)
        self.write_int32(self.keyTime)
        self.write_boolean(self.isFromArena)
        self.write_bytestring(self.key)

    def read(self):
        self.name = self.read_string()
        self.host = self.read_string()
        self.stats = self.read_string()
        self.port = self.read_int32()
        self.gameId = self.read_int32()
        self.keyTime = self.read_int32()
        self.isFromArena = self.read_boolean()
        self.key = self.read_bytestring()
        return self.name, self.host, self.stats, self.port, self.gameId, self.keyTime, self.isFromArena, self.key


class MapInfoPacket(Packet.Packet):
    def __init__(self):
        super(MapInfoPacket, self).__init__()
        self.width = 0
        self.height = 0
        self.name = ""
        self.displayName = ""
        self.fp = 0
        self.background = 0
        self.difficulty = 0
        self.allowPlayerTeleport = False
        self.showDisplays = False
        self.clientXML = ""
        self.extraXML = ""

    def write(self):
        self.reset()
        self.write_int32(self.width)
        self.write_int32(self.height)
        self.write_string(self.name)
        self.write_string(self.displayName)
        self.write_uint32(self.fp)
        self.write_int32(self.background)
        self.write_int32(self.difficulty)
        self.write_boolean(self.allowPlayerTeleport)
        self.write_boolean(self.showDisplays)
        self.write_string(self.clientXML)
        self.write_string(self.extraXML)

    def read(self):
        self.width = self.read_int32()
        self.height = self.read_int32()
        self.name = self.read_string()
        self.displayName = self.read_string()
        self.fp = self.read_uint32()
        self.background = self.read_int32()
        self.difficulty = self.read_int32()
        self.allowPlayerTeleport = self.read_boolean()
        self.showDisplays = self.read_boolean()
        self.clientXML = self.read_string()
        self.extraXML = self.read_string()
        return self.width, self.height, self.name, self.displayName, self.fp, self.background, self.difficulty, self.allowPlayerTeleport, self.showDisplays, self.clientXML, self.extraXML