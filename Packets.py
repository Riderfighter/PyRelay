import json

import Datatypes
import Packet


# Client Packets
class AcceptTradePacket(Packet.Packet):
    def __init__(self):
        super(AcceptTradePacket, self).__init__()
        self.myOffers = []
        self.yourOffers = []

    def write(self, myOffers, yourOffers):
        self.write_booleanarray(myOffers)
        self.write_booleanarray(yourOffers)

    def read(self):
        self.myOffers = self.read_booleanarray()
        self.yourOffers = self.read_booleanarray()
        return self.myOffers, self.yourOffers


class AoEAckPacket(Packet.Packet):
    def __init__(self):
        super(AoEAckPacket, self).__init__()
        self.Time = 0
        self.X = 0.0
        self.Y = 0.0

    def write(self, time, x, y):
        self.write_int32(time)
        self.write_float(x)
        self.write_float(y)

    def read(self):
        self.Time = self.read_int32()
        self.X = self.read_float()
        self.Y = self.read_float()
        return self.Time, (self.X, self.Y)


class BuyPacket(Packet.Packet):
    def __init__(self):
        super(BuyPacket, self).__init__()
        self.objectId = 0
        self.quantitiy = 0

    def write(self, objectId, quantitiy):
        self.write_int32(objectId)
        self.write_int32(quantitiy)

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

    def write(self, name, guildrank):
        self.write_string(name)
        self.write_int32(guildrank)

    def read(self):
        self.name = self.read_string()
        self.guildRank = self.read_int32()
        return self.name, self.guildRank


class ChangeTradePacket(Packet.Packet):
    def __init__(self):
        super(ChangeTradePacket, self).__init__()
        self.offers = []

    def write(self, offers):
        self.write_booleanarray(offers)

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

    def write(self, name):
        self.write_string(name)

    def read(self):
        self.name = self.read_string()
        return self.name


class CreateGuildPacket(Packet.Packet):
    def __init__(self):
        super(CreateGuildPacket, self).__init__()
        self.name = ''

    def write(self, name):
        self.write_string(name)

    def read(self):
        self.name = self.read_string()


class CreatePacket(Packet.Packet):
    def __init__(self):
        super(CreatePacket, self).__init__()
        self.classType = 0
        self.skinType = 0

    def write(self, classType, skinType):
        self.write_uint16(classType)
        self.write_uint16(skinType)

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

    def write(self, accountlistId, add, objectid):
        self.write_int32(accountlistId)
        self.write_boolean(add)
        self.write_int32(objectid)

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

    def write(self, time, bulletid, targetid, killed):
        self.write_int32(time)
        self.write_byte(bulletid)
        self.write_int32(targetid)
        self.write_boolean(killed)

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

    def write(self, currency):
        self.write_int32(currency)

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

    def write(self, time):
        self.write_int16(time)

    def read(self):
        self.time = self.read_int32()
        return self.time


class GroundDamagePacket(Packet.Packet):
    def __init__(self):
        super(GroundDamagePacket, self).__init__()
        self.time = 0
        self.X = 0.0
        self.Y = 0.0

    def write(self, time, x, y):
        self.write_int32(time)
        self.write_float(x)
        self.write_float(y)

    def read(self):
        self.time = self.read_int32()
        self.X = self.read_float()
        self.Y = self.read_float()
        return self.time, self.X, self.Y


class GuildInvitePacket(Packet.Packet):
    def __init__(self):
        super(GuildInvitePacket, self).__init__()
        self.name = ''

    def write(self, name):
        self.write_string(name)

    def read(self):
        self.name = self.read_string()
        return self.name


class GuildRemovePacket(Packet.Packet):
    def __init__(self):
        super(GuildRemovePacket, self).__init__()
        self.name = ''

    def write(self, name):
        self.write_string(name)

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
        self.MapJSON = 0
        self.entryTag = ''
        self.gameNet = ''
        self.gamenetuserId = ''
        self.playPlatform = ''
        self.platformToken = ''
        self.userToken = ''

    def write(self, buildVersion, gameId, GUID, random1, password, random2, secret, keyTime, key, mapjson, entrytag,
              gamenet, gamenetuserId, playplatform, platformtoken, usertoken):
        self.write_string(buildVersion)
        self.write_int32(gameId)
        self.write_string(GUID)
        self.write_int32(random1)
        self.write_string(password)
        self.write_int32(random2)
        self.write_string(secret)
        self.write_int32(keyTime)
        self.write_bytestring(key)
        self.write_string(mapjson)
        self.write_string(entrytag)
        self.write_string(gamenet)
        self.write_string(gamenetuserId)
        self.write_string(playplatform)
        self.write_string(platformtoken)
        self.write_string(usertoken)

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
        self.MapJSON = self.read_string()
        self.entryTag = self.read_string()
        self.gameNet = self.read_string()
        self.gamenetuserId = self.read_string()
        self.playPlatform = self.read_string()
        self.platformToken = self.read_string()
        self.userToken = self.read_string()
        return self.buildVersion, self.gameId, self.GUID, self.random1, self.password, self.random2, self.secret, self.keyTime, self.key, self.MapJSON, self.entryTag, self.gameNet, self.gamenetuserId, self.playPlatform, self.platformToken, self.userToken


class InvDropPacket(Packet.Packet):
    def __init__(self):
        super(InvDropPacket, self).__init__()
        self.slot = ()

    def write(self, objectid, slotid, objecttype):
        self.write_int32(objectid)
        self.write_byte(slotid)
        self.write_int32(objecttype)

    def read(self):
        self.slot = (self.read_int32(), self.read_byte(), self.read_int32())
        return self.slot


class InvSwapPacket(Packet.Packet):
    def __init__(self):
        super(InvSwapPacket, self).__init__()
        self.time = 0
        self.location = ()
        self.slotobject1 = ()
        self.slotobject2 = ()

    def write(self, time, location, slotobject1, slotobject2):
        self.write_int32(time)
        self.write_float(location[0])
        self.write_float(location[1])
        self.write_int32(slotobject1[0])
        self.write_byte(slotobject1[1])
        self.write_int32(slotobject1[2])
        self.write_int32(slotobject2[0])
        self.write_byte(slotobject2[1])
        self.write_int32(slotobject2[2])

    def read(self):
        self.time = self.read_int32()
        self.location = (self.read_float(), self.read_float())
        self.slotobject1 = (self.read_int32(), self.read_byte(), self.read_int32())
        self.slotobject2 = (self.read_int32(), self.read_byte(), self.read_int32())
        return self.time, self.location, self.slotobject1, self.slotobject2


class JoinGuildPacket(Packet.Packet):
    def __init__(self):
        super(JoinGuildPacket, self).__init__()
        self.guildName = ''

    def write(self, guildName):
        self.write_string(guildName)

    def read(self):
        self.guildName = self.read_string()
        return self.guildName


class KeyInfoRequestPacket(Packet.Packet):
    def __init__(self):
        super(KeyInfoRequestPacket, self).__init__()
        self.Request = []

    def write(self, request):
        self.write_bytestring(request)

    def read(self):
        self.Request = self.read_bytestring()


class LeaveArenaPacket(Packet.Packet):
    def __init__(self):
        super(LeaveArenaPacket, self).__init__()
        self.time = 0

    def write(self, time):
        self.write_int32(time)

    def read(self):
        self.time = self.read_int32()
        return self.time


class LoadPacket(Packet.Packet):
    def __init__(self):
        super(LoadPacket, self).__init__()
        self.characterId = 0
        self.isfromArena = None

    def write(self, characterid, isfromarena):
        self.write_int32(characterid)
        self.write_boolean(isfromarena)

    def read(self):
        self.characterId = self.read_int32()
        self.isfromArena = self.read_boolean()
        return self.characterId, self.isfromArena


class MovePacket(Packet.Packet):
    def __init__(self):
        super(MovePacket, self).__init__()
        self.tickId = 0
        self.time = 0
        self.NewPostion = ()
        self.Records = []

    def write(self, tickid, time, newposition, records):
        self.write_int32(tickid)
        self.write_int32(time)
        self.write_float(newposition[0])
        self.write_float(newposition[1])
        length = 0
        self.write_int16(0)
        if length == 0:
            return
        else:
            for record in records:
                self.write_int32(record)

    def read(self):
        self.tickId = self.read_int32()
        self.time = self.read_int32()
        self.NewPostion = (self.read_float(), self.read_float())
        length = self.read_int16()
        if length == 0:
            self.Records = []
        else:
            try:
                for _ in range(length):
                    self.Records.append(self.read_int32())
            except Exception as e:
                print(e)
        return self.tickId, self.time, self.NewPostion,


class OtherHitPacket(Packet.Packet):
    def __init__(self):
        super(OtherHitPacket, self).__init__()
        self.time = 0
        self.bulletId = ''
        self.objectId = 0
        self.targetId = 0

    def write(self, time, bulletid, objectid, targetid):
        self.write_int32(time)
        self.write_byte(bulletid)
        self.write_int32(objectid)
        self.write_int32(targetid)

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

    def write(self, command, petid):
        self.write_byte(self.commands.get(command))
        self.write_int32(petid)

    def read(self):
        self.commandId = self.read_byte()
        self.petId = self.read_int32()
        return self.commandId, self.petId


class PetYardCommandPacket(Packet.Packet):
    def __init__(self):
        super(PetYardCommandPacket, self).__init__()
        self.commands = {'UPGRADE_PET_YARD': 1, 'FEED_PET': 2, 'FUSE_PET': 3}
        self.commandId = ''
        self.petId1 = 0
        self.petId2 = 0
        self.objectId = 0
        self.slotobject = ()
        self.currency = ''

    def write(self, command, petId1, petId2, objectId, slotobject, currency):
        self.write_byte(self.commands.get(command))
        self.write_int32(petId1)
        self.write_int32(petId2)
        self.write_int32(objectId)
        self.write_int32(slotobject[0])
        self.write_byte(slotobject[1])
        self.write_int32(slotobject[2])
        self.write_byte(currency)

    def read(self):
        self.commandId = self.read_byte()
        self.petId1 = self.read_int32()
        self.petId2 = self.read_int32()
        self.objectId = self.read_int32()
        self.slotobject = (self.read_int32(), self.read_byte(), self.read_int32())
        self.currency = self.read_byte()
        return self.commandId, self.petId1, self.petId2, self.objectId, self.slotobject, self.currency


class PlayerHitPacket(Packet.Packet):
    def __init__(self):
        super(PlayerHitPacket, self).__init__()
        self.bulletId = ''
        self.objectId = 0

    def write(self, bulletid, objectid):
        self.write_byte(bulletid)
        self.write_int32(objectid)

    def read(self):
        self.bulletId = self.read_byte()
        self.objectId = self.read_int32()
        return self.bulletId, self.objectId


class PlayerShootPacket(Packet.Packet):
    def __init__(self):
        super(PlayerShootPacket, self).__init__()
        self.time = 0
        self.bulletId = ''
        self.containerType = 0
        self.position = ()
        self.angle = 0.0

    def write(self, time, bulletId, containerType, position, angle):
        self.write_int32(time)
        self.write_byte(bulletId)
        self.write_int16(containerType)
        self.write_float(position[0])
        self.write_float(position[1])
        self.write_float(angle)

    def read(self):
        self.time = self.read_int32()
        self.bulletId = self.read_byte()
        self.containerType = self.read_int16()
        self.position = (self.read_float(), self.read_float())
        self.angle = self.read_float()
        return self.time, self.bulletId, self.containerType, self.position, self.angle


class PlayerTextPacket(Packet.Packet):
    def __init__(self):
        super(PlayerTextPacket, self).__init__()
        self.text = ''

    def write(self, text):
        self.write_string(text)

    def read(self):
        self.text = self.read_string()
        return self.text


class PongPacket(Packet.Packet):
    def __init__(self):
        super(PongPacket, self).__init__()
        self.time = 0
        self.serial = 0

    def write(self, time, serial):
        self.write_int32(time)
        self.write_int32(serial)

    def read(self):
        self.time = self.read_int32()
        self.serial = self.read_int32()
        return self.time, self.serial


class RequestTradePacket(Packet.Packet):
    def __init__(self):
        super(RequestTradePacket, self).__init__()
        self.name = ''

    def write(self, name):
        self.write_string(name)

    def read(self):
        self.name = self.read_string()
        return self.name


class ReskinPacket(Packet.Packet):
    def __init__(self):
        super(ReskinPacket, self).__init__()
        self.skinId = 0

    def write(self, skinid):
        self.write_int32(skinid)

    def read(self):
        self.skinId = self.read_int32()
        return self.skinId


class ReskinPetPacket(Packet.Packet):
    def __init__(self):
        super(ReskinPetPacket, self).__init__()
        self.newpetType = 0
        self.item = ()

    def write(self, newpettype, item):
        self.write_int32(newpettype)
        self.write_int32(item[0])
        self.write_byte(item[1])
        self.write_int32(item[2])

    def read(self):
        self.newpetType = self.read_int32()
        self.item = (self.read_int32(), self.read_byte(), self.read_int32())
        return self.newpetType, self.item


class SetConditionPacket(Packet.Packet):
    def __init__(self):
        super(SetConditionPacket, self).__init__()
        self.conditionEffect = ''
        self.conditionDuration = 0.0

    def write(self, effect, duration):
        self.write_byte(effect)
        self.write_int16(duration)

    def read(self):
        self.conditionEffect = self.read_byte()
        self.conditionDuration = self.read_int16()
        return self.conditionEffect, self.conditionDuration


class ShootAckPacket(Packet.Packet):
    def __init__(self):
        super(ShootAckPacket, self).__init__()
        self.time = 0

    def write(self, time):
        self.write_int32(time)

    def read(self):
        self.time = self.read_int32()
        return self.time


class SquareHitPacket(Packet.Packet):
    def __init__(self):
        super(SquareHitPacket, self).__init__()
        self.time = 0
        self.bulletId = ''
        self.objectId = 0

    def write(self, time, bulletid, objectid):
        self.write_int32(time)
        self.write_byte(bulletid)
        self.write_int32(objectid)

    def read(self):
        self.time = self.read_int32()
        self.bulletid = self.read_byte()
        self.objectid = self.read_int32()
        return self.time, self.bulletid, self.objectid


class TeleportPacket(Packet.Packet):
    def __init__(self):
        super(TeleportPacket, self).__init__()
        self.objectId = 0

    def write(self, objectid):
        self.write_int32(objectid)

    def read(self):
        self.objectId = self.read_int32()
        return self.objectId


class TinkerQuestPacket(Packet.Packet):
    def __init__(self):
        super(TinkerQuestPacket, self).__init__()
        self.slot = ()

    def write(self, slot):
        self.write_int32(slot[0])
        self.write_byte(slot[1])
        self.write_int32(slot[2])

    def read(self):
        self.slot = (self.read_int32(), self.read_byte(), self.read_int32())
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
        self.slotObject = ()
        self.itemUsePos = ()
        self.useType = ''

    def write(self, time, slotObject, itemUsePos, useType):
        self.write_int32(time)
        self.write_int32(slotObject[0])
        self.write_byte(slotObject[1])
        self.write_int32(slotObject[2])
        self.write_float(itemUsePos[0])
        self.write_float(itemUsePos[1])
        self.write_byte(useType)

    def read(self):
        self.time = self.read_int32()
        self.slotObject = (self.read_int32(), self.read_byte(), self.read_int32())
        self.itemUsePos = (self.read_float(), self.read_float())
        self.useType = self.read_byte()
        return self.time, self.slotObject, self.itemUsePos, self.useType


class UsePortal(Packet.Packet):
    def __init__(self):
        super(UsePortal, self).__init__()
        self.objectid = 0

    def write(self, objectid):
        self.write_int32(objectid)

    def read(self):
        self.objectid = self.read_int32()


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
        for _ in range(self.read_int16()):
            tile = Datatypes.Tile(self)
            tile.read()
            self.tiles.append(tile)
        for _ in range(self.read_int16()):
            entity = Datatypes.Entity(self)
            entity.read()
            self.newobjs.append(entity)
        for _ in range(self.read_int16()):
            self.drops.append(self.read_int32())


class TextPacket(Packet.Packet):
    def __init__(self):
        self.name = ""
        self.objectid = 0
        self.numstars = 0
        self.bubbletime = 0
        self.recipient = ""
        self.text = ""
        self.cleantext = ""
        super(TextPacket, self).__init__()

    def write(self, name, objectid, numstars, bubbletime, recipient, text, cleantext):
        self.write_string(name)
        self.write_int32(objectid)
        self.write_int32(numstars)
        self.write_byte(bubbletime)
        self.write_string(recipient)
        self.write_string(text)
        self.write_string(cleantext)

    def read(self):
        self.name = self.read_string()
        self.objectid = self.read_int32()
        self.numstars = self.read_int32()
        self.bubbletime = self.read_byte()
        self.recipient = self.read_string()
        self.text = self.read_string()
        self.cleantext = self.read_string()
        return self.name, self.objectid, self.numstars, self.bubbletime, self.recipient, self.text, self.cleantext


class AccountListPacket(Packet.Packet):
    def __init__(self):
        super(AccountListPacket, self).__init__()
        self.AccountListId = 0
        self.AccountIds = []
        self.LockAction = 0

    def write(self, accountlistid, accountids, lockaction):
        self.write_int32(accountlistid)
        self.write_string(accountids)
        self.write_int32(lockaction)

    def read(self):
        self.AccountListId = self.read_int32()
        self.AccountIds = self.read_string()
        self.LockAction = self.read_int32()
        return self.AccountListId, self.AccountIds, self.LockAction


class AllyShootPacket(Packet.Packet):
    def __init__(self):
        super(AllyShootPacket, self).__init__()
        self.BulletId = ''
        self.OwnerId = 0
        self.ContainerType = 0
        self.Angle = 0.0

    def write(self, bulletid, ownerid, containertype, angle):
        self.write_byte(bulletid)
        self.write_int32(ownerid)
        self.write_int16(containertype)
        self.write_float(angle)

    def read(self):
        self.BulletId = self.read_byte()
        self.OwnerId = self.read_int32()
        self.ContainerType = self.read_int16()
        self.Angle = self.read_float()
        return self.BulletId, self.OwnerId, self.ContainerType, self.Angle


class AoEPacket(Packet.Packet):
    def __init__(self):
        super(AoEPacket, self).__init__()
        self.location = ()
        self.radius = 0.0
        self.damage = 0
        self.effects = ''
        self.effectduration = 0.0
        self.origintype = 0
        self.color = 0

    def write(self, location, radius, damage, effects, effectduration, orgintype, color):
        self.write_float(location[0])
        self.write_float(location[1])
        self.write_float(radius)
        self.write_uint16(damage)
        self.write_byte(effects)
        self.write_float(effectduration)
        self.write_int16(orgintype)
        self.write_int32(color)

    def read(self):
        self.location = (self.read_float(), self.read_float())
        self.radius = self.read_float()
        self.damage = self.read_uint16()
        self.effects = self.read_byte()
        self.effectduration = self.read_float()
        self.origintype = self.read_int16()
        self.color = self.read_int32()
        return self.location, self.radius, self.damage, self.effects, self.effectduration, self.origintype, self.color


class ArenaDeathPacket(Packet.Packet):
    def __init__(self):
        super(ArenaDeathPacket, self).__init__()
        self.restartprice = 0

    def write(self, restartprice):
        self.write_int32(restartprice)

    def read(self):
        self.restartprice = self.read_int32()


class ArenaNextWavePacket(Packet.Packet):
    def __init__(self):
        super(ArenaNextWavePacket, self).__init__()
        self.typeid = 0

    def write(self, typeid):
        self.write_int32(typeid)

    def read(self):
        self.typeid = self.read_int32()
        return self.typeid


class BuyResultPacket(Packet.Packet):
    def __init__(self):
        super(BuyResultPacket, self).__init__()
        self.result = 0
        self.message = ''

    def write(self, result, message):
        self.write_int32(result)
        self.write_string(message)

    def read(self):
        self.result = self.read_int32()
        self.message = self.read_string()
        return self.result, self.message


class ClientStatPacket(Packet.Packet):
    def __init__(self):
        super(ClientStatPacket, self).__init__()
        self.name = ''
        self.value = 0

    def write(self, name, value):
        self.write_string(name)
        self.write_int32(value)

    def read(self):
        self.name = self.read_string()
        self.value = self.read_int32()
        return self.name, self.value


class CreateGuildResultPacket(Packet.Packet):
    def __init__(self):
        super(CreateGuildResultPacket, self).__init__()
        self.success = None
        self.errorText = ''

    def write(self, success, errortext):
        self.write_boolean(success)
        self.write_string(errortext)

    def read(self):
        self.success = self.read_boolean()
        self.errorText = self.read_string()
        return self.success, self.errorText


class CreateSuccessPacket(Packet.Packet):
    def __init__(self):
        super(CreateSuccessPacket, self).__init__()
        self.charId = 0
        self.objectId = 0

    def write(self, objectid, charId):
        self.write_int32(objectid)
        self.write_int32(charId)

    def read(self):
        self.objectId = self.read_int32()
        self.charId = self.read_int32()
        return self.objectId, self.charId


class DamagePacket(Packet.Packet):
    def __init__(self):
        super(DamagePacket, self).__init__()
        self.targetid = 0
        self.effects = []
        self.damage = 0.0
        self.killed = None
        self.bulletid = ''
        self.objectid = 0

    def write(self, targetid, effects, damage, killed, bulletid, objectid):
        self.write_int32(targetid)
        self.write_unsignedbyte(len(effects))
        for effect in effects:
            self.write_unsignedbyte(effect)
        self.write_uint16(damage)
        self.write_boolean(killed)
        self.write_unsignedbyte(bulletid)
        self.write_int32(objectid)

    def read(self):
        self.targetid = self.read_int32()
        for _ in range(self.read_unsignedbyte()):
            self.effects.append(self.read_unsignedbyte())
        self.damage = self.read_uint16()
        self.killed = self.read_boolean()
        self.bulletid = self.read_unsignedbyte()
        self.objectid = self.read_int32()

class DeathPacket(Packet.Packet):
    def __init__(self):
        super(DeathPacket, self).__init__()
        self.accountid = ''
        self.charid = 0
        self.killedby = ''
        self.zombietype = 0
        self.zombieid = 0

    def write(self, accountid, charid, killedby, zombietype, zombieid):
        self.write_string(accountid)
        self.write_int32(charid)
        self.write_string(killedby)
        self.write_int32(zombietype)
        self.write_int32(zombieid)

    def read(self):
        self.accountid = self.read_string()
        self.charid = self.read_int32()
        self.killedby = self.read_string()
        self.zombietype = self.read_int32()
        self.zombieid = self.read_int32()
        return self.accountid, self.charid, self.killedby, self.zombietype, self.zombieid


class EnemyShootPacket(Packet.Packet):
    def __init__(self):
        super(EnemyShootPacket, self).__init__()
        self.bulletId = 0
        self.ownerId = 0
        self.bulletType = 0
        self.startingPos = 0, 0
        self.angle = 0.0
        self.damage = 0
        self.numShots = 0
        self.angleInc = 0.0

    def write(self, bulletId, ownerid, bulletType, startingPos, angle, damage, numShots=1, angleInc=0):
        self.write_unsignedbyte(bulletId)
        self.write_int32(ownerid)
        self.write_unsignedbyte(bulletType)
        self.write_float(startingPos[0])
        self.write_float(startingPos[1])
        self.write_float(angle)
        self.write_int16(damage)
        self.write_unsignedbyte(numShots)
        self.write_float(angleInc)

    def read(self):
        self.bulletId = self.read_unsignedbyte()
        self.ownerId = self.read_int32()
        self.bulletType = self.read_unsignedbyte()
        self.startingPos = self.read_float(), self.read_float()
        self.angle = self.read_float()
        self.damage = self.read_int16()
        if len(self.data[self.index:]) > 0:
            self.numShots = self.read_unsignedbyte()
            self.angleInc = self.read_float()
        else:
            self.numShots = 1
            self.angleInc = 0
        return self.bulletType, self.ownerId, self.bulletType, self.startingPos, self.angle, self.damage, self.numShots, self.angleInc


class FailurePacket(Packet.Packet):
    def __init__(self):
        super(FailurePacket, self).__init__()
        self.ErrorId = 0
        self.ErrorMessage = ''

    def write(self, errorid, errormessage):
        self.write_int32(errorid)
        self.write_string(errormessage)

    def read(self):
        self.ErrorId = self.read_int32()
        self.ErrorMessage = self.read_string()
        return self.ErrorId, self.ErrorMessage


class NewTickPacket(Packet.Packet):
    def __init__(self):
        super(NewTickPacket, self).__init__()
        self.TickId = 0
        self.TickTime = 0
        self.Statuses = []

    def write(self, tickid, ticktime, statuses):
        self.write_int32(tickid)
        self.write_int32(ticktime)
        self.write_bytestring(statuses)

    def read(self):
        self.TickId = self.read_int32()
        self.TickTime = self.read_int32()
        self.Statuses = self.read_bytestring()
        return self.TickId, self.TickTime, self.Statuses


class FilePacket(Packet.Packet):
    def __init__(self):
        super(FilePacket, self).__init__()
        self.name = ''
        self.bytes = []

    def write(self, name, bytes):
        self.write_string(name)
        self.write_bytestring(bytes)

    def read(self):
        self.name = self.read_string()
        self.bytes = self.read_bytestring()
        return self.name, self.bytes


class GlobalNotificationPacket(Packet.Packet):
    def __init__(self):
        super(GlobalNotificationPacket, self).__init__()
        self.typeId = 0
        self.text = ''

    def write(self, typeid, text):
        self.write_int32(typeid)
        self.write_string(text)

    def read(self):
        self.typeId = self.read_int32()
        self.text = self.read_string()
        return self.typeId, self.text


class NotificationPacket(Packet.Packet):
    def __init__(self):
        super(NotificationPacket, self).__init__()
        self.objectId = 0
        self.message = ""
        self.color = 0

    def write(self, objectId, message, color):
        self.write_int32(objectId)
        self.write_string(json.dumps({'key': 'blank', 'tokens': {'data': message}}))
        self.write_int32(color)

    def read(self):
        self.objectId = self.read_int32()
        self.message = json.loads(self.read_string())
        self.color = self.read_int32()
        return self.objectId, self.message, self.color


class GotoPacket(Packet.Packet):
    def __init__(self):
        super(GotoPacket, self).__init__()
        self.objectId = 0
        self.location = ()

    def write(self, objectId, location):
        self.write_int32(objectId)
        self.write_float(location[0])
        self.write_float(location[1])

    def read(self):
        self.objectId = self.read_int32()
        self.location = (self.read_float(), self.read_float())
        return self.objectId, self.location


class HatchEggPacket(Packet.Packet):
    def __init__(self):
        super(HatchEggPacket, self).__init__()
        self.petName = ''
        self.petSkinId = 0

    def write(self, name, skinId):
        self.write_string(name)
        self.write_int32(skinId)

    def read(self):
        self.petName = self.read_string()
        self.petSkinId = self.read_int32()
        return self.petName, self.petSkinId


class InvResultPacket(Packet.Packet):
    def __init__(self):
        super(InvResultPacket, self).__init__()
        self.result = 0

    def write(self, result):
        self.write_int32(result)

    def read(self):
        self.result = self.read_int32()
        return self.result


class InvitedToGuildPacket(Packet.Packet):
    def __init__(self):
        super(InvitedToGuildPacket, self).__init__()
        self.name = ''
        self.guildName = ''

    def write(self, name, guildname):
        self.write_string(name)
        self.write_string(guildname)

    def read(self):
        self.name = self.read_string()
        self.guildName = self.read_string()
        return self.name, self.guildName


class KeyInfoResponsePacket(Packet.Packet):
    def __init__(self):
        super(KeyInfoResponsePacket, self).__init__()
        self.response = []

    def write(self, response):
        self.write_bytestring(response)

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
        self.gameid = 0
        self.keytime = 0
        self.isfromarena = None
        self.key = []

    def write(self, name, host, stats, port, gameid, keytime, isfromarena, key):
        self.write_string(name)
        self.write_string(host)
        self.write_string(stats)
        self.write_int32(port)
        self.write_int32(gameid)
        self.write_int32(keytime)
        self.write_boolean(isfromarena)
        self.write_bytestring(key)

    def read(self):
        self.name = self.read_string()
        self.host = self.read_string()
        self.stats = self.read_string()
        self.port = self.read_int32()
        self.gameid = self.read_int32()
        self.keytime = self.read_int32()
        self.isfromarena = self.read_boolean()
        self.key = self.read_bytestring()
        return self.name, self.host, self.stats, self.port, self.gameid, self.keytime, self.isfromarena, self.key


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

    def write(self, width, height, name, displayName, fp, background, difficulty, allowPlayerTeleport, showDisplays,
              clientXML, extraXML):
        self.write_int32(width)
        self.write_int32(height)
        self.write_string(name)
        self.write_string(displayName)
        self.write_uint32(fp)
        self.write_int32(background)
        self.write_int32(difficulty)
        self.write_boolean(allowPlayerTeleport)
        self.write_boolean(showDisplays)
        self.write_string(clientXML)
        self.write_string(extraXML)

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