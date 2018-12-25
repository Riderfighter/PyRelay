import byteio
import rc4decrypt

# Client Packets
class AcceptTradePacket:
	def __init__(self):
		self.myOffers = []
		self.yourOffers = []
		self.packet = byteio.Packet()
	
	def write(self, myOffers, yourOffers):
		self.packet.writeBooleanarray(myOffers)
		self.packet.writeBooleanarray(yourOffers)
	
	def read(self):
		self.myOffers = self.packet.readBooleanarray()
		self.yourOffers = self.packet.readBooleanarray()
		return self.myOffers, self.yourOffers

class AoEAckPacket:
	def __init__(self):
		self.Time = 0
		self.X = 0.0
		self.Y = 0.0
		self.packet = byteio.Packet()
	
	def write(self, time, x, y):
		self.packet.writeInt32(time)
		self.packet.writeFloat(x)
		self.packet.writeFloat(y)
	
	def read(self):
		self.Time = self.packet.readInt32()
		self.X = self.packet.readFloat()
		self.Y = self.packet.readFloat()
		return self.Time, (self.X, self.Y)
	
class BuyPacket:
	def __init__(self):
		self.objectId = 0
		self.quantitiy = 0
		self.packet = byteio.Packet()
	
	def write(self, objectId, quantitiy):
		self.packet.writeInt32(objectId)
		self.packet.writeInt32(quantitiy)
	
	def read(self):
		self.objectId = self.packet.readInt32()
		self.quantitiy = self.packet.readInt32()
		return self.objectId, self.quantitiy

class CancelTradePacket:
	def __init__(self):
		self.packet = byteio.Packet()
	
	def write(self):
		pass
	
	def read(self):
		pass

class ChangeGuildRankPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''
		self.guildRank = 0

	def write(self, name, guildrank):
		self.packet.writeString(name)
		self.packet.writeInt32(guildrank)
	
	def read(self):
		self.name = self.packet.readString()
		self.guildRank = self.packet.readInt32()
		return self.name, self.guildRank

class ChangeTradePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.offers = []
	
	def write(self, offers):
		self.packet.writeBooleanarray(offers)
	
	def read(self):
		self.offers = self.packet.readBooleanarray()
		return self.offers

class CheckCreditsPacket:
	def __init__(self):
		self.packet = byteio.Packet()

	def write(self):
		pass

	def read(self):
		pass

class ChooseNamePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''

	def write(self, name):
		self.packet.writeString(name)
	
	def read(self):
		self.name = self.packet.readString()
		return self.name

class CreateGuildPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''
	
	def write(self, name):
		self.packet.writeString(name)
	
	def read(self):
		self.name = self.packet.readString()

class CreatePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.classType = 0
		self.skinType = 0
	
	def write(self, classType, skinType):
		self.packet.writeUInt16(classType)
		self.packet.writeUInt16(skinType)
	
	def read(self):
		self.classType = self.packet.readUInt16()
		self.skinType = self.packet.readUInt16()
		return self.classType, self.skinType

class EditAccountListPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.accountlistId = 0
		self.add = None
		self.objectId = 0
	
	def write(self, accountlistId, add, objectid):
		self.packet.writeInt32(accountlistId)
		self.packet.writeBoolean(add)
		self.packet.writeInt32(objectid)
	
	def read(self):
		self.accountlistId = self.packet.readInt32()
		self.add = self.packet.readBoolean()
		self.objectId = self.packet.readInt32()
		return self.accountlistId, self.add, self.objectId

class EnemyHitPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.bulletid = ''
		self.targetid = 0
		self.killed = None
	
	def write(self, time, bulletid, targetid, killed):
		self.packet.writeInt32(time)
		self.packet.writeByte(bulletid)
		self.packet.writeInt32(targetid)
		self.packet.writeBoolean(killed)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.bulletid = self.packet.readByte()
		self.targetid = self.packet.readInt32()
		self.killed = self.packet.readBoolean()
		return self.time, self.bulletid, self.targetid, self.killed

class EnterArenaPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.currency = 0
	
	def write(self, currency):
		self.packet.writeInt32(currency)
	
	def read(self):
		self.currency = self.packet.readInt32()
		return self.currency

class EscapePacket:
	def __init__(self):
		self.packet = byteio.Packet()
	
	def write(self):
		pass

	def read(self):
		pass

class GotoAckPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
	
	def write(self, time):
		self.packet.writeInt16(time)
	
	def read(self):
		self.time = self.packet.readInt32()
		return self.time

class GroundDamagePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.X = 0.0
		self.Y = 0.0
	
	def write(self, time, x, y):
		self.packet.writeInt32(time)
		self.packet.writeFloat(x)
		self.packet.writeFloat(y)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.X = self.packet.readFloat()
		self.Y = self.packet.readFloat()
		return self.time, self.X, self.Y

class GuildInvitePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''
	
	def write(self, name):
		self.packet.writeString(name)
	
	def read(self):
		self.name = self.packet.readString()
		return self.name

class GuildRemovePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''
	
	def write(self, name):
		self.packet.writeString(name)
	
	def read(self):
		self.name = self.packet.readString()
		return self.name

class HelloPacket:
	def __init__(self):
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
		self.packet = byteio.Packet()
	
	def write(self, buildVersion, gameId, GUID, random1, password, random2, secret, keyTime, key, mapjson, entrytag, gamenet, gamenetuserId, playplatform, platformtoken, usertoken):
		self.packet.writeString(buildVersion)
		self.packet.writeInt32(gameId)
		self.packet.writeString(GUID)
		self.packet.writeInt32(random1)
		self.packet.writeString(password)
		self.packet.writeInt32(random2)
		self.packet.writeString(secret)
		self.packet.writeInt32(keyTime)
		self.packet.writeBytearray(key)
		self.packet.writeUTFString(mapjson)
		self.packet.writeString(entrytag)
		self.packet.writeString(gamenet)
		self.packet.writeString(gamenetuserId)
		self.packet.writeString(playplatform)
		self.packet.writeString(platformtoken)
		self.packet.writeString(usertoken)
	
	def read(self):
		self.buildVersion = self.packet.readString()
		self.gameId = self.packet.readInt32()
		self.GUID = self.packet.readString()
		self.random1 = self.packet.readInt32()
		self.password = self.packet.readString()
		self.random2 = self.packet.readInt32()
		self.secret = self.packet.readString()
		self.keyTime = self.packet.readInt32()
		self.key = self.packet.readBytearray()
		self.MapJSON = self.packet.readUTFString()
		self.entryTag = self.packet.readString()
		self.gameNet = self.packet.readString()
		self.gamenetuserId = self.packet.readString()
		self.playPlatform = self.packet.readString()
		self.platformToken = self.packet.readString()
		self.userToken = self.packet.readString()
		return self.buildVersion, self.gameId, self.GUID, self.random1, self.password, self.random2, self.secret, self.keyTime, self.key, self.MapJSON, self.entryTag, self.gameNet, self.gamenetuserId, self.playPlatform, self.platformToken, self.userToken

class InvDropPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.slot = ()
	
	def write(self, objectid, slotid, objecttype):
		self.packet.writeInt32(objectid)
		self.packet.writeByte(slotid)
		self.packet.writeInt32(objecttype)
	
	def read(self):
		self.slot = (self.packet.readInt32(), self.packet.readByte(), self.packet.readInt32())
		return self.slot

class InvSwapPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.location = ()
		self.slotobject1 = ()
		self.slotobject2 = ()
	
	def write(self, time, location, slotobject1, slotobject2):
		self.packet.writeInt32(time)
		self.packet.writeFloat(location[0])
		self.packet.writeFloat(location[1])
		self.packet.writeInt32(slotobject1[0])
		self.packet.writeByte(slotobject1[1])
		self.packet.writeInt32(slotobject1[2])
		self.packet.writeInt32(slotobject2[0])
		self.packet.writeByte(slotobject2[1])
		self.packet.writeInt32(slotobject2[2])
	
	def read(self):
		self.time = self.packet.readInt32()
		self.location = (self.packet.readFloat(), self.packet.readFloat())
		self.slotobject1 = (self.packet.readInt32(), self.packet.readByte(), self.packet.readInt32())
		self.slotobject2 = (self.packet.readInt32(), self.packet.readByte(), self.packet.readInt32())
		return self.time, self.location, self.slotobject1, self.slotobject2

class JoinGuildPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.guildName = ''
	
	def write(self, guildName):
		self.packet.writeString(guildName)
	
	def read(self):
		self.guildName = self.packet.readString()
		return self.guildName

class KeyInfoRequestPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.Request = []
	
	def write(self, request):
		self.packet.writeBytearray(request)
	
	def read(self):
		self.Request = self.packet.readBytearray()

class LeaveArenaPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
	
	def write(self, time):
		self.packet.writeInt32(time)

	def read(self):
		self.time = self.packet.readInt32()
		return self.time

class LoadPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.characterId = 0
		self.isfromArena = None
	
	def write(self, characterid, isfromarena):
		self.packet.writeInt32(characterid)
		self.packet.writeBoolean(isfromarena)
	
	def read(self):
		self.characterId = self.packet.readInt32()
		self.isfromArena = self.packet.readBoolean()
		return self.characterId, self.isfromArena

class MovePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.tickId = 0
		self.time = 0
		self.NewPostion = ()
		self.Records = []
	
	def write(self, tickid, time, newposition, records):
		self.packet.writeInt32(tickid)
		self.packet.writeInt32(time)
		self.packet.writeFloat(newposition[0])
		self.packet.writeFloat(newposition[1])
		length = 0
		self.packet.writeInt16(0)
		if length == 0:
			return
		else:
			for record in records:
				self.packet.writeInt32(record)
	
	def read(self):
		self.tickId = self.packet.readInt32()
		self.time = self.packet.readInt32()
		self.NewPostion = (self.packet.readFloat(), self.packet.readFloat())
		self.packet.readInt16()
		length = 0
		if length == 0:
			self.Records = []
		else:
			try:
				for x in range(length):
					self.Records.append(self.packet.readInt32())
			except Exception as e:
				print(e)

class OtherHitPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.bulletId = ''
		self.objectId = 0
		self.targetId = 0
	
	def write(self, time, bulletid, objectid, targetid):
		self.packet.writeInt32(time)
		self.packet.writeByte(bulletid)
		self.packet.writeInt32(objectid)
		self.packet.writeInt32(targetid)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.bulletId = self.packet.readByte()
		self.objectId = self.packet.readInt32()
		self.targetId = self.packet.readInt32()
		return self.time, self.bulletId, self.objectId, self.targetId

class PetCommandPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.commands = {'FOLLOW_PET': 1, 'UNFOLLOW_PET': 2, 'RELEASE_PET': 3}
		self.commandId = 0
		self.petId = 0
	
	def write(self, command, petid):
		self.packet.writeByte(self.commands.get(command))
		self.packet.writeInt32(petid)
	
	def read(self):
		self.commandId = self.packet.readByte()
		self.petId = self.packet.readInt32()
		return self.commandId, self.petId
	
class PetYardCommandPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.commands = {'UPGRADE_PET_YARD': 1, 'FEED_PET': 2, 'FUSE_PET': 3}
		self.commandId = ''
		self.petId1 = 0
		self.petId2 = 0
		self.objectId = 0
		self.slotobject = ()
		self.currency = ''
	
	def write(self, command, petId1, petId2, objectId, slotobject, currency):
		self.packet.writeByte(self.commands.get(command))
		self.packet.writeInt32(petId1)
		self.packet.writeInt32(petId2)
		self.packet.writeInt32(objectId)
		self.packet.writeInt32(slotobject[0])
		self.packet.writeByte(slotobject[1])
		self.packet.writeInt32(slotobject[2])
		self.packet.writeByte(currency)
	
	def read(self):
		self.commandId = self.packet.readByte()
		self.petId1 = self.packet.readInt32()
		self.petId2 = self.packet.readInt32()
		self.objectId = self.packet.readInt32()
		self.slotobject = (self.packet.readInt32(), self.packet.readByte(), self.packet.readInt32())
		self.currency = self.packet.readByte()
		return self.commandId, self.petId1, self.petId2, self.objectId, self.slotobject, self.currency

class PlayerHitPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.bulletId = ''
		self.objectId = 0
	
	def write(self, bulletid, objectid):
		self.packet.writeByte(bulletid)
		self.packet.writeInt32(objectid)
	
	def read(self):
		self.bulletId = self.packet.readByte()
		self.objectId = self.packet.readInt32()
		return self.bulletId, self.objectId
	
class PlayerShootPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.bulletId = ''
		self.containerType = 0
		self.position = ()
		self.angle = 0.0
	
	def write(self, time, bulletId, containerType, position, angle):
		self.packet.writeInt32(time)
		self.packet.writeByte(bulletId)
		self.packet.writeInt16(containerType)
		self.packet.writeFloat(position[0])
		self.packet.writeFloat(position[1])
		self.packet.writeFloat(angle)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.bulletId = self.packet.readByte()
		self.containerType = self.packet.readInt16()
		self.position = (self.packet.readFloat(), self.packet.readFloat())
		self.angle = self.packet.readFloat()
		return self.time, self.bulletId, self.containerType, self.position, self.angle

class PlayerTextPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.text = ''
	
	def write(self, text):
		self.packet.writeString(text)
	
	def read(self):
		self.text = self.packet.readString()
		return self.text

class PongPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.serial = 0
	
	def write(self, time, serial):
		self.packet.writeInt32(time)
		self.packet.writeInt32(serial)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.serial = self.packet.readInt32()
		return self.time, self.serial

class RequestTradePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''
	
	def write(self, name):
		self.packet.writeString(name)
	
	def read(self):
		self.name = self.packet.readString()
		return self.name

class ReskinPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.skinId = 0
	
	def write(self, skinid):
		self.packet.writeInt32(skinid)
	
	def read(self):
		self.skinId = self.packet.readInt32()
		return self.skinId

class ReskinPetPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.newpetType = 0
		self.item = ()
	
	def write(self, newpettype, item):
		self.packet.writeInt32(newpettype)
		self.packet.writeInt32(item[0])
		self.packet.writeByte(item[1])
		self.packet.writeInt32(item[2])
	
	def read(self):
		self.newpetType = self.packet.readInt32()
		self.item = (self.packet.readInt32(),self.packet.readByte(),self.packet.readInt32())
		return self.newpetType, self.item

class SetConditionPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.conditionEffect = ''
		self.conditionDuration = 0.0
	
	def write(self, effect, duration):
		self.packet.writeByte(effect)
		self.packet.writeInt16(duration)

	def read(self):
		self.conditionEffect = self.packet.readByte()
		self.conditionDuration = self.packet.readInt16()
		return self.conditionEffect, self.conditionDuration

class ShootAckPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
	
	def write(self, time):
		self.packet.writeInt32(time)
	
	def read(self):
		self.time = self.packet.readInt32()
		return self.time

class SquareHitPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.bulletId = ''
		self.objectId = 0
	
	def write(self, time, bulletid, objectid):
		self.packet.writeInt32(time)
		self.packet.writeByte(bulletid)
		self.packet.writeInt32(objectid)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.bulletid = self.packet.readByte()
		self.objectid = self.packet.readInt32()
		return self.time, self.bulletid, self.objectid

class TeleportPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.objectId = 0
	
	def write(self, objectid):
		self.packet.writeInt32(objectid)
	
	def read(self):
		self.objectId = self.packet.readInt32()
		return self.objectId

class TinkerQuestPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.slot = ()
	
	def write(self, slot):
		self.packet.writeInt32(slot[0])
		self.packet.writeByte(slot[1])
		self.packet.writeInt32(slot[2])
	
	def read(self):
		self.slot = (self.packet.readInt32(), self.packet.readByte(), self.packet.readInt32())
		return self.slot

class UpdateAckPacket:
	def __init__(self):
		self.packet = byteio.Packet()
	
	def write(self):
		pass
	
	def read(self):
		pass
		# return self.packet.data

class UseItemPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.time = 0
		self.slotObject = ()
		self.itemUsePos = ()
		self.useType = ''
	
	def write(self, time, slotObject, itemUsePos, useType):
		self.packet.writeInt32(time)
		self.packet.writeInt32(slotObject[0])
		self.packet.writeByte(slotObject[1])
		self.packet.writeInt32(slotObject[2])
		self.packet.writeFloat(itemUsePos[0])
		self.packet.writeFloat(itemUsePos[1])
		self.packet.writeByte(useType)
	
	def read(self):
		self.time = self.packet.readInt32()
		self.slotObject = (self.packet.readInt32(),self.packet.readByte(),self.packet.readInt32())
		self.itemUsePos = (self.packet.readFloat(),self.packet.readFloat())
		self.useType = self.packet.readByte()
		return self.time, self.slotObject, self.itemUsePos, self.useType

class UsePortal:
	def __init__(self):
		self.objectid = 0
		self.packet = byteio.Packet()

	def write(self, objectid):
		self.packet.writeInt32(objectid)

	def read(self):
		self.objectid = self.packet.readInt32()

class ViewQuestsPacket:
	def __init__(self):
		self.packet = byteio.Packet()
	
	def write(self):
		pass
	
	def read(self):
		pass


#Server packets?
class AccountListPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.AccountListId = 0
		self.AccountIds = []
		self.LockAction = 0
	
	def write(self, accountlistid, accountids, lockaction):
		self.packet.writeInt32(accountlistid)
		self.packet.writeString(accountids)
		self.packet.writeInt32(lockaction)
	
	def read(self):
		self.AccountListId = self.packet.readInt32()
		self.AccountIds = self.packet.readString()
		self.LockAction = self.packet.readInt32()
		return self.AccountListId, self.AccountIds, self.LockAction

class AllyShootPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.BulletId = ''
		self.OwnerId = 0
		self.ContainerType = 0
		self.Angle = 0.0
	
	def write(self, bulletid, ownerid, containertype, angle):
		self.packet.writeByte(bulletid)
		self.packet.writeInt32(ownerid)
		self.packet.writeInt16(containertype)
		self.packet.writeFloat(angle)
	
	def read(self):
		self.BulletId = self.packet.readByte()
		self.OwnerId = self.packet.readInt32()
		self.ContainerType = self.packet.readInt16()
		self.Angle = self.packet.readFloat()
		return self.BulletId, self.OwnerId, self.ContainerType, self.Angle

class AoEPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.location = ()
		self.radius = 0.0
		self.damage = 0
		self.effects = ''
		self.effectduration = 0.0
		self.origintype = 0
		self.color = 0
	
	def write(self, location, radius, damage, effects, effectduration, orgintype, color):
		self.packet.writeFloat(location[0])
		self.packet.writeFloat(location[1])
		self.packet.writeFloat(radius)
		self.packet.writeUInt16(damage)
		self.packet.writeByte(effects)
		self.packet.writeFloat(effectduration)
		self.packet.writeInt16(orgintype)
		self.packet.writeInt32(color)
	
	def read(self):
		self.location = (self.packet.readFloat(), self.packet.readFloat())
		self.radius = self.packet.readFloat()
		self.damage = self.packet.readUInt16()
		self.effects = self.packet.readByte()
		self.effectduration = self.packet.readFloat()
		self.origintype = self.packet.readInt16()
		self.color = self.packet.readInt32()
		return self.location, self.radius, self.damage, self.effects, self.effectduration, self.origintype, self.color

class ArenaDeathPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.restartprice = 0
	
	def write(self, restartprice):
		self.packet.writeInt32(restartprice)
	
	def read(self):
		self.restartprice = self.packet.readInt32()

class ArenaNextWavePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.typeid = 0
	
	def write(self, typeid):
		self.packet.writeInt32(typeid)
	
	def read(self):
		self.typeid = self.packet.readInt32()
		return self.typeid

class BuyResultPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.result = 0
		self.message = ''
	
	def write(self, result, message):
		self.packet.writeInt32(result)
		self.packet.writeString(message)
	
	def read(self):
		self.result = self.packet.readInt32()
		self.message = self.packet.readString()
		return self.result, self.message

class ClientStatPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.name = ''
		self.value = 0
	
	def write(self, name, value):
		self.packet.writeString(name)
		self.packet.writeInt32(value)
	
	def read(self):
		self.name = self.packet.readString()
		self.value = self.packet.readInt32()
		return self.name, self.value

class CreateGuildResultPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.success = None
		self.errorText = ''
	
	def write(self, success, errortext):
		self.packet.writeBoolean(success)
		self.packet.writeString(errortext)
	
	def read(self):
		self.success = self.packet.readBoolean()
		self.errorText = self.packet.readString()
		return self.success, self.errorText

class CreateSuccessPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.charId = 0
		self.objectId = 0
	
	def write(self, objectid, charId):
		self.packet.writeInt32(objectid)
		self.packet.writeInt32(charId)
	
	def read(self):
		self.objectId = self.packet.readInt32()
		self.charId = self.packet.readInt32()
		return self.objectId, self.charId

class DamagePacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.targetid = 0
		self.effects = []
		self.damage = 0.0
		self.killed = None
		self.bulletid = ''
		self.objectid = 0
	
class DeathPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.accountid = ''
		self.charid = 0
		self.killedby = ''
		self.zombietype = 0
		self.zombieid = 0
	
	def write(self, accountid, charid, killedby, zombietype, zombieid):
		self.packet.writeString(accountid)
		self.packet.writeInt32(charid)
		self.packet.writeString(killedby)
		self.packet.writeInt32(zombietype)
		self.packet.writeInt32(zombieid)
	
	def read(self):
		self.accountid = self.packet.readString()
		self.charid = self.packet.readInt32()
		self.killedby = self.packet.readString()
		self.zombietype = self.packet.readInt32()
		self.zombieid = self.packet.readInt32()
		return self.accountid, self.charid, self.killedby, self.zombietype, self.zombieid
	
class EnemyShootPacket:
	def __init__(self):
		self.packet = byteio.Packet()

class FailurePacket:
	def __init__(self):
		self.ErrorId = 0
		self.ErrorMessage = ''
		self.packet = byteio.Packet()
	
	def write(self, errorid, errormessage):
		self.packet.writeInt32(errorid)
		self.packet.writeString(errormessage)
	
	def read(self):
		self.ErrorId = self.packet.readInt32()
		self.ErrorMessage = self.packet.readString()
		return self.ErrorId, self.ErrorMessage


class NewTickPacket:
	def __init__(self):
		self.packet = byteio.Packet()
		self.TickId = 0
		self.TickTime = 0
		self.Statuses = []
	
	def write(self, tickid, ticktime, statuses):
		self.packet.writeInt32(tickid)
		self.packet.writeInt32(ticktime)
		self.packet.writeBytearray(statuses)
	
	def read(self):
		self.TickId = self.packet.readInt32()
		self.TickTime = self.packet.readInt32()
		self.Statuses = self.packet.readBytearray()
		return self.TickId, self.TickTime, self.Statuses
