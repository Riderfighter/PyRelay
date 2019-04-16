import Packet
import json

# Client Packets
class AcceptTradePacket(Packet.Packet):
	def __init__(self):
		super(AcceptTradePacket, self).__init__()
		self.myOffers = []
		self.yourOffers = []
		
	
	def write(self, myOffers, yourOffers):
		self.writeBooleanarray(myOffers)
		self.writeBooleanarray(yourOffers)
	
	def read(self):
		self.myOffers = self.readBooleanarray()
		self.yourOffers = self.readBooleanarray()
		return self.myOffers, self.yourOffers

class AoEAckPacket(Packet.Packet):
	def __init__(self):
		super(AoEAckPacket, self).__init__()
		self.Time = 0
		self.X = 0.0
		self.Y = 0.0
		
	
	def write(self, time, x, y):
		self.writeInt32(time)
		self.writeFloat(x)
		self.writeFloat(y)
	
	def read(self):
		self.Time = self.readInt32()
		self.X = self.readFloat()
		self.Y = self.readFloat()
		return self.Time, (self.X, self.Y)
	
class BuyPacket(Packet.Packet):
	def __init__(self):
		super(BuyPacket, self).__init__()
		self.objectId = 0
		self.quantitiy = 0
		
	
	def write(self, objectId, quantitiy):
		self.writeInt32(objectId)
		self.writeInt32(quantitiy)
	
	def read(self):
		self.objectId = self.readInt32()
		self.quantitiy = self.readInt32()
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
		self.writeString(name)
		self.writeInt32(guildrank)
	
	def read(self):
		self.name = self.readString()
		self.guildRank = self.readInt32()
		return self.name, self.guildRank

class ChangeTradePacket(Packet.Packet):
	def __init__(self):
		super(ChangeTradePacket, self).__init__()
		self.offers = []
	
	def write(self, offers):
		self.writeBooleanarray(offers)
	
	def read(self):
		self.offers = self.readBooleanarray()
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
		self.writeString(name)
	
	def read(self):
		self.name = self.readString()
		return self.name

class CreateGuildPacket(Packet.Packet):
	def __init__(self):
		super(CreateGuildPacket, self).__init__()
		self.name = ''
	
	def write(self, name):
		self.writeString(name)
	
	def read(self):
		self.name = self.readString()

class CreatePacket(Packet.Packet):
	def __init__(self):
		super(CreatePacket, self).__init__()
		self.classType = 0
		self.skinType = 0
	
	def write(self, classType, skinType):
		self.writeUInt16(classType)
		self.writeUInt16(skinType)
	
	def read(self):
		self.classType = self.readUInt16()
		self.skinType = self.readUInt16()
		return self.classType, self.skinType

class EditAccountListPacket(Packet.Packet):
	def __init__(self):
		super(EditAccountListPacket, self).__init__()
		self.accountlistId = 0
		self.add = None
		self.objectId = 0
	
	def write(self, accountlistId, add, objectid):
		self.writeInt32(accountlistId)
		self.writeBoolean(add)
		self.writeInt32(objectid)
	
	def read(self):
		self.accountlistId = self.readInt32()
		self.add = self.readBoolean()
		self.objectId = self.readInt32()
		return self.accountlistId, self.add, self.objectId

class EnemyHitPacket(Packet.Packet):
	def __init__(self):
		super(EnemyHitPacket, self).__init__()
		self.time = 0
		self.bulletid = ''
		self.targetid = 0
		self.killed = None
	
	def write(self, time, bulletid, targetid, killed):
		self.writeInt32(time)
		self.writeByte(bulletid)
		self.writeInt32(targetid)
		self.writeBoolean(killed)
	
	def read(self):
		self.time = self.readInt32()
		self.bulletid = self.readByte()
		self.targetid = self.readInt32()
		self.killed = self.readBoolean()
		return self.time, self.bulletid, self.targetid, self.killed

class EnterArenaPacket(Packet.Packet):
	def __init__(self):
		super(EnterArenaPacket, self).__init__()
		self.currency = 0
	
	def write(self, currency):
		self.writeInt32(currency)
	
	def read(self):
		self.currency = self.readInt32()
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
		self.writeInt16(time)
	
	def read(self):
		self.time = self.readInt32()
		return self.time

class GroundDamagePacket(Packet.Packet):
	def __init__(self):
		super(GroundDamagePacket, self).__init__()
		self.time = 0
		self.X = 0.0
		self.Y = 0.0
	
	def write(self, time, x, y):
		self.writeInt32(time)
		self.writeFloat(x)
		self.writeFloat(y)
	
	def read(self):
		self.time = self.readInt32()
		self.X = self.readFloat()
		self.Y = self.readFloat()
		return self.time, self.X, self.Y

class GuildInvitePacket(Packet.Packet):
	def __init__(self):
		super(GuildInvitePacket, self).__init__()
		self.name = ''
	
	def write(self, name):
		self.writeString(name)
	
	def read(self):
		self.name = self.readString()
		return self.name

class GuildRemovePacket(Packet.Packet):
	def __init__(self):
		super(GuildRemovePacket, self).__init__()
		self.name = ''
	
	def write(self, name):
		self.writeString(name)
	
	def read(self):
		self.name = self.readString()
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
		
	
	def write(self, buildVersion, gameId, GUID, random1, password, random2, secret, keyTime, key, mapjson, entrytag, gamenet, gamenetuserId, playplatform, platformtoken, usertoken):
		self.writeString(buildVersion)
		self.writeInt32(gameId)
		self.writeString(GUID)
		self.writeInt32(random1)
		self.writeString(password)
		self.writeInt32(random2)
		self.writeString(secret)
		self.writeInt32(keyTime)
		self.writeBytearray(key)
		self.writeString(mapjson)
		self.writeString(entrytag)
		self.writeString(gamenet)
		self.writeString(gamenetuserId)
		self.writeString(playplatform)
		self.writeString(platformtoken)
		self.writeString(usertoken)
	
	def read(self):
		self.buildVersion = self.readString()
		self.gameId = self.readInt32()
		self.GUID = self.readString()
		self.random1 = self.readInt32()
		self.password = self.readString()
		self.random2 = self.readInt32()
		self.secret = self.readString()
		self.keyTime = self.readInt32()
		self.key = self.readBytearray()
		self.MapJSON = self.readString()
		self.entryTag = self.readString()
		self.gameNet = self.readString()
		self.gamenetuserId = self.readString()
		self.playPlatform = self.readString()
		self.platformToken = self.readString()
		self.userToken = self.readString()
		return self.buildVersion, self.gameId, self.GUID, self.random1, self.password, self.random2, self.secret, self.keyTime, self.key, self.MapJSON, self.entryTag, self.gameNet, self.gamenetuserId, self.playPlatform, self.platformToken, self.userToken

class InvDropPacket(Packet.Packet):
	def __init__(self):
		super(InvDropPacket, self).__init__()
		self.slot = ()
	
	def write(self, objectid, slotid, objecttype):
		self.writeInt32(objectid)
		self.writeByte(slotid)
		self.writeInt32(objecttype)
	
	def read(self):
		self.slot = (self.readInt32(), self.readByte(), self.readInt32())
		return self.slot

class InvSwapPacket(Packet.Packet):
	def __init__(self):
		super(InvSwapPacket, self).__init__()
		self.time = 0
		self.location = ()
		self.slotobject1 = ()
		self.slotobject2 = ()
	
	def write(self, time, location, slotobject1, slotobject2):
		self.writeInt32(time)
		self.writeFloat(location[0])
		self.writeFloat(location[1])
		self.writeInt32(slotobject1[0])
		self.writeByte(slotobject1[1])
		self.writeInt32(slotobject1[2])
		self.writeInt32(slotobject2[0])
		self.writeByte(slotobject2[1])
		self.writeInt32(slotobject2[2])
	
	def read(self):
		self.time = self.readInt32()
		self.location = (self.readFloat(), self.readFloat())
		self.slotobject1 = (self.readInt32(), self.readByte(), self.readInt32())
		self.slotobject2 = (self.readInt32(), self.readByte(), self.readInt32())
		return self.time, self.location, self.slotobject1, self.slotobject2

class JoinGuildPacket(Packet.Packet):
	def __init__(self):
		super(JoinGuildPacket, self).__init__()
		self.guildName = ''
	
	def write(self, guildName):
		self.writeString(guildName)
	
	def read(self):
		self.guildName = self.readString()
		return self.guildName

class KeyInfoRequestPacket(Packet.Packet):
	def __init__(self):
		super(KeyInfoRequestPacket, self).__init__()
		self.Request = []
	
	def write(self, request):
		self.writeBytearray(request)
	
	def read(self):
		self.Request = self.readBytearray()

class LeaveArenaPacket(Packet.Packet):
	def __init__(self):
		super(LeaveArenaPacket, self).__init__()
		self.time = 0
	
	def write(self, time):
		self.writeInt32(time)

	def read(self):
		self.time = self.readInt32()
		return self.time

class LoadPacket(Packet.Packet):
	def __init__(self):
		super(LoadPacket, self).__init__()
		self.characterId = 0
		self.isfromArena = None
	
	def write(self, characterid, isfromarena):
		self.writeInt32(characterid)
		self.writeBoolean(isfromarena)
	
	def read(self):
		self.characterId = self.readInt32()
		self.isfromArena = self.readBoolean()
		return self.characterId, self.isfromArena

class MovePacket(Packet.Packet):
	def __init__(self):
		super(MovePacket, self).__init__()
		self.tickId = 0
		self.time = 0
		self.NewPostion = ()
		self.Records = []
	
	def write(self, tickid, time, newposition, records):
		self.writeInt32(tickid)
		self.writeInt32(time)
		self.writeFloat(newposition[0])
		self.writeFloat(newposition[1])
		length = 0
		self.writeInt16(0)
		if length == 0:
			return
		else:
			for record in records:
				self.writeInt32(record)
	
	def read(self):
		self.tickId = self.readInt32()
		self.time = self.readInt32()
		self.NewPostion = (self.readFloat(), self.readFloat())
		length = self.readInt16()
		if length == 0:
			self.Records = []
		else:
			try:
				for _ in range(length):
					self.Records.append(self.readInt32())
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
		self.writeInt32(time)
		self.writeByte(bulletid)
		self.writeInt32(objectid)
		self.writeInt32(targetid)
	
	def read(self):
		self.time = self.readInt32()
		self.bulletId = self.readByte()
		self.objectId = self.readInt32()
		self.targetId = self.readInt32()
		return self.time, self.bulletId, self.objectId, self.targetId

class PetCommandPacket(Packet.Packet):
	def __init__(self):
		super(PetCommandPacket, self).__init__()
		self.commands = {'FOLLOW_PET': 1, 'UNFOLLOW_PET': 2, 'RELEASE_PET': 3}
		self.commandId = 0
		self.petId = 0
	
	def write(self, command, petid):
		self.writeByte(self.commands.get(command))
		self.writeInt32(petid)
	
	def read(self):
		self.commandId = self.readByte()
		self.petId = self.readInt32()
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
		self.writeByte(self.commands.get(command))
		self.writeInt32(petId1)
		self.writeInt32(petId2)
		self.writeInt32(objectId)
		self.writeInt32(slotobject[0])
		self.writeByte(slotobject[1])
		self.writeInt32(slotobject[2])
		self.writeByte(currency)
	
	def read(self):
		self.commandId = self.readByte()
		self.petId1 = self.readInt32()
		self.petId2 = self.readInt32()
		self.objectId = self.readInt32()
		self.slotobject = (self.readInt32(), self.readByte(), self.readInt32())
		self.currency = self.readByte()
		return self.commandId, self.petId1, self.petId2, self.objectId, self.slotobject, self.currency

class PlayerHitPacket(Packet.Packet):
	def __init__(self):
		super(PlayerHitPacket, self).__init__()
		self.bulletId = ''
		self.objectId = 0
	
	def write(self, bulletid, objectid):
		self.writeByte(bulletid)
		self.writeInt32(objectid)
	
	def read(self):
		self.bulletId = self.readByte()
		self.objectId = self.readInt32()
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
		self.writeInt32(time)
		self.writeByte(bulletId)
		self.writeInt16(containerType)
		self.writeFloat(position[0])
		self.writeFloat(position[1])
		self.writeFloat(angle)
	
	def read(self):
		self.time = self.readInt32()
		self.bulletId = self.readByte()
		self.containerType = self.readInt16()
		self.position = (self.readFloat(), self.readFloat())
		self.angle = self.readFloat()
		return self.time, self.bulletId, self.containerType, self.position, self.angle

class PlayerTextPacket(Packet.Packet):
	def __init__(self):
		super(PlayerTextPacket, self).__init__()
		self.text = ''
	
	def write(self, text):
		self.writeString(text)
	
	def read(self):
		self.text = self.readString()
		return self.text

class PongPacket(Packet.Packet):
	def __init__(self):
		super(PongPacket, self).__init__()
		self.time = 0
		self.serial = 0
	
	def write(self, time, serial):
		self.writeInt32(time)
		self.writeInt32(serial)
	
	def read(self):
		self.time = self.readInt32()
		self.serial = self.readInt32()
		return self.time, self.serial

class RequestTradePacket(Packet.Packet):
	def __init__(self):
		super(RequestTradePacket, self).__init__()
		self.name = ''
	
	def write(self, name):
		self.writeString(name)
	
	def read(self):
		self.name = self.readString()
		return self.name

class ReskinPacket(Packet.Packet):
	def __init__(self):
		super(ReskinPacket, self).__init__()
		self.skinId = 0
	
	def write(self, skinid):
		self.writeInt32(skinid)
	
	def read(self):
		self.skinId = self.readInt32()
		return self.skinId

class ReskinPetPacket(Packet.Packet):
	def __init__(self):
		super(ReskinPetPacket, self).__init__()
		self.newpetType = 0
		self.item = ()
	
	def write(self, newpettype, item):
		self.writeInt32(newpettype)
		self.writeInt32(item[0])
		self.writeByte(item[1])
		self.writeInt32(item[2])
	
	def read(self):
		self.newpetType = self.readInt32()
		self.item = (self.readInt32(),self.readByte(),self.readInt32())
		return self.newpetType, self.item

class SetConditionPacket(Packet.Packet):
	def __init__(self):
		super(SetConditionPacket, self).__init__()
		self.conditionEffect = ''
		self.conditionDuration = 0.0
	
	def write(self, effect, duration):
		self.writeByte(effect)
		self.writeInt16(duration)

	def read(self):
		self.conditionEffect = self.readByte()
		self.conditionDuration = self.readInt16()
		return self.conditionEffect, self.conditionDuration

class ShootAckPacket(Packet.Packet):
	def __init__(self):
		super(ShootAckPacket, self).__init__()
		self.time = 0
	
	def write(self, time):
		self.writeInt32(time)
	
	def read(self):
		self.time = self.readInt32()
		return self.time

class SquareHitPacket(Packet.Packet):
	def __init__(self):
		super(SquareHitPacket, self).__init__()
		self.time = 0
		self.bulletId = ''
		self.objectId = 0
	
	def write(self, time, bulletid, objectid):
		self.writeInt32(time)
		self.writeByte(bulletid)
		self.writeInt32(objectid)
	
	def read(self):
		self.time = self.readInt32()
		self.bulletid = self.readByte()
		self.objectid = self.readInt32()
		return self.time, self.bulletid, self.objectid

class TeleportPacket(Packet.Packet):
	def __init__(self):
		super(TeleportPacket, self).__init__()
		self.objectId = 0
	
	def write(self, objectid):
		self.writeInt32(objectid)
	
	def read(self):
		self.objectId = self.readInt32()
		return self.objectId

class TinkerQuestPacket(Packet.Packet):
	def __init__(self):
		super(TinkerQuestPacket, self).__init__()
		self.slot = ()
	
	def write(self, slot):
		self.writeInt32(slot[0])
		self.writeByte(slot[1])
		self.writeInt32(slot[2])
	
	def read(self):
		self.slot = (self.readInt32(), self.readByte(), self.readInt32())
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
		self.writeInt32(time)
		self.writeInt32(slotObject[0])
		self.writeByte(slotObject[1])
		self.writeInt32(slotObject[2])
		self.writeFloat(itemUsePos[0])
		self.writeFloat(itemUsePos[1])
		self.writeByte(useType)
	
	def read(self):
		self.time = self.readInt32()
		self.slotObject = (self.readInt32(),self.readByte(),self.readInt32())
		self.itemUsePos = (self.readFloat(),self.readFloat())
		self.useType = self.readByte()
		return self.time, self.slotObject, self.itemUsePos, self.useType

class UsePortal(Packet.Packet):
	def __init__(self):
		super(UsePortal, self).__init__()
		self.objectid = 0

	def write(self, objectid):
		self.writeInt32(objectid)

	def read(self):
		self.objectid = self.readInt32()

class ViewQuestsPacket(Packet.Packet):
	def __init__(self):
		super(ViewQuestsPacket, self).__init__()
	def write(self):
		pass
	
	def read(self):
		pass


#Server packets?
class TextPacket(Packet.Packet):
	def __init__(self):
		super(TextPacket, self).__init__()
	def write(self, name, objectid, numstars, bubbletime, recipient, text, cleantext):
		self.writeString(name)
		self.writeInt32(objectid)
		self.writeInt32(numstars)
		self.writeByte(chr(bubbletime))
		self.writeString(recipient)
		self.writeString(text)
		self.writeString(cleantext)
	
	def read(self):
		return (self.readString(), self.readInt32(), self.readInt32(), self.readByte(), self.readString(), self.readString(), self.readString())

class AccountListPacket(Packet.Packet):
	def __init__(self):
		super(AccountListPacket, self).__init__()
		self.AccountListId = 0
		self.AccountIds = []
		self.LockAction = 0
	
	def write(self, accountlistid, accountids, lockaction):
		self.writeInt32(accountlistid)
		self.writeString(accountids)
		self.writeInt32(lockaction)
	
	def read(self):
		self.AccountListId = self.readInt32()
		self.AccountIds = self.readString()
		self.LockAction = self.readInt32()
		return self.AccountListId, self.AccountIds, self.LockAction

class AllyShootPacket(Packet.Packet):
	def __init__(self):
		super(AllyShootPacket, self).__init__()
		self.BulletId = ''
		self.OwnerId = 0
		self.ContainerType = 0
		self.Angle = 0.0
	
	def write(self, bulletid, ownerid, containertype, angle):
		self.writeByte(bulletid)
		self.writeInt32(ownerid)
		self.writeInt16(containertype)
		self.writeFloat(angle)
	
	def read(self):
		self.BulletId = self.readByte()
		self.OwnerId = self.readInt32()
		self.ContainerType = self.readInt16()
		self.Angle = self.readFloat()
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
		self.writeFloat(location[0])
		self.writeFloat(location[1])
		self.writeFloat(radius)
		self.writeUInt16(damage)
		self.writeByte(effects)
		self.writeFloat(effectduration)
		self.writeInt16(orgintype)
		self.writeInt32(color)
	
	def read(self):
		self.location = (self.readFloat(), self.readFloat())
		self.radius = self.readFloat()
		self.damage = self.readUInt16()
		self.effects = self.readByte()
		self.effectduration = self.readFloat()
		self.origintype = self.readInt16()
		self.color = self.readInt32()
		return self.location, self.radius, self.damage, self.effects, self.effectduration, self.origintype, self.color

class ArenaDeathPacket(Packet.Packet):
	def __init__(self):
		super(ArenaDeathPacket, self).__init__()
		self.restartprice = 0
	
	def write(self, restartprice):
		self.writeInt32(restartprice)
	
	def read(self):
		self.restartprice = self.readInt32()

class ArenaNextWavePacket(Packet.Packet):
	def __init__(self):
		super(ArenaNextWavePacket, self).__init__()
		self.typeid = 0
	
	def write(self, typeid):
		self.writeInt32(typeid)
	
	def read(self):
		self.typeid = self.readInt32()
		return self.typeid

class BuyResultPacket(Packet.Packet):
	def __init__(self):
		super(BuyResultPacket, self).__init__()
		self.result = 0
		self.message = ''
	
	def write(self, result, message):
		self.writeInt32(result)
		self.writeString(message)
	
	def read(self):
		self.result = self.readInt32()
		self.message = self.readString()
		return self.result, self.message

class ClientStatPacket(Packet.Packet):
	def __init__(self):
		super(ClientStatPacket, self).__init__()
		self.name = ''
		self.value = 0
	
	def write(self, name, value):
		self.writeString(name)
		self.writeInt32(value)
	
	def read(self):
		self.name = self.readString()
		self.value = self.readInt32()
		return self.name, self.value

class CreateGuildResultPacket(Packet.Packet):
	def __init__(self):
		super(CreateGuildResultPacket, self).__init__()
		self.success = None
		self.errorText = ''
	
	def write(self, success, errortext):
		self.writeBoolean(success)
		self.writeString(errortext)
	
	def read(self):
		self.success = self.readBoolean()
		self.errorText = self.readString()
		return self.success, self.errorText

class CreateSuccessPacket(Packet.Packet):
	def __init__(self):
		super(CreateSuccessPacket, self).__init__()
		self.charId = 0
		self.objectId = 0
	
	def write(self, objectid, charId):
		self.writeInt32(objectid)
		self.writeInt32(charId)
	
	def read(self):
		self.objectId = self.readInt32()
		self.charId = self.readInt32()
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
	
class DeathPacket(Packet.Packet):
	def __init__(self):
		super(DeathPacket, self).__init__()
		self.accountid = ''
		self.charid = 0
		self.killedby = ''
		self.zombietype = 0
		self.zombieid = 0
	
	def write(self, accountid, charid, killedby, zombietype, zombieid):
		self.writeString(accountid)
		self.writeInt32(charid)
		self.writeString(killedby)
		self.writeInt32(zombietype)
		self.writeInt32(zombieid)
	
	def read(self):
		self.accountid = self.readString()
		self.charid = self.readInt32()
		self.killedby = self.readString()
		self.zombietype = self.readInt32()
		self.zombieid = self.readInt32()
		return self.accountid, self.charid, self.killedby, self.zombietype, self.zombieid
	
class EnemyShootPacket(Packet.Packet):
	def __init__(self):
		super(EnemyShootPacket, self).__init__()

class FailurePacket(Packet.Packet):
	def __init__(self):
		super(FailurePacket, self).__init__()
		self.ErrorId = 0
		self.ErrorMessage = ''
		
	
	def write(self, errorid, errormessage):
		self.writeInt32(errorid)
		self.writeString(errormessage)
	
	def read(self):
		self.ErrorId = self.readInt32()
		self.ErrorMessage = self.readString()
		return self.ErrorId, self.ErrorMessage


class NewTickPacket(Packet.Packet):
	def __init__(self):
		super(NewTickPacket, self).__init__()
		self.TickId = 0
		self.TickTime = 0
		self.Statuses = []
	
	def write(self, tickid, ticktime, statuses):
		self.writeInt32(tickid)
		self.writeInt32(ticktime)
		self.writeBytearray(statuses)
	
	def read(self):
		self.TickId = self.readInt32()
		self.TickTime = self.readInt32()
		self.Statuses = self.readBytearray()
		return self.TickId, self.TickTime, self.Statuses

class FilePacket(Packet.Packet):
	def __init__(self):
		super(FilePacket, self).__init__()
		self.name = ''
		self.bytes = []
	
	def write(self, name, bytes):
		self.writeString(name)
		self.writeBytearray(bytes)
	
	def read(self):
		self.name = self.readString()
		self.bytes = self.readBytearray()
		return self.name, self.bytes

class GlobalNotificationPacket(Packet.Packet):
	def __init__(self):
		super(GlobalNotificationPacket, self).__init__()
		self.typeId = 0
		self.text = ''
	
	def write(self, typeid, text):
		self.writeInt32(typeid)
		self.writeString(text)
	
	def read(self):
		self.typeId = self.readInt32()
		self.text = self.readString()

class NotificationPacket(Packet.Packet):
	def __init__(self):
		super(NotificationPacket, self).__init__()
		self.objectId = 0
		self.message = ""
		self.color = 0
	
	def write(self, objectId, message, color):
		self.writeInt32(objectId)
		self.writeString(json.dumps({'key': 'blank', 'tokens': {'data': message}}))
		self.writeInt32(color)
	
	def read(self):
		self.objectId = self.readInt32()
		self.message = json.loads(self.readString())
		self.color = self.readInt32()
		return self.objectId, self.message, self.color

class GotoPacket(Packet.Packet):
	def __init__(self):
		super(GotoPacket, self).__init__()
		self.objectId = 0
		self.location = ()
	
	def write(self, objectId, location):
		self.writeInt32(objectId)
		self.writeFloat(location[0])
		self.writeFloat(location[1])
	
	def read(self):
		self.objectId = self.readInt32()
		self.location = (self.readFloat(), self.readFloat())
		return self.objectId, self.location

class HatchEggPacket(Packet.Packet):
	def __init__(self):
		super(HatchEggPacket, self).__init__()
		self.petName = ''
		self.petSkinId = 0
	
	def write(self, name, skinId):
		self.writeString(name)
		self.writeInt32(skinId)
	
	def read(self):
		self.petName = self.readString()
		self.petSkinId = self.readInt32()
		return self.petName, self.petSkinId

class InvResultPacket(Packet.Packet):
	def __init__(self):
		super(InvResultPacket, self).__init__()
		self.result = 0

	def write(self, result):
		self.writeInt32(result)
	
	def read(self):
		self.result = self.readInt32()
		return self.result

class InvitedToGuildPacket(Packet.Packet):
	def __init__(self):
		super(InvitedToGuildPacket, self).__init__()
		self.name = ''
		self.guildName = ''
	
	def write(self, name, guildname):
		self.writeString(name)
		self.writeString(guildname)
	
	def read(self):
		self.name = self.readString()
		self.guildName = self.readString()
		return self.name, self.guildName

class KeyInfoResponsePacket(Packet.Packet):
	def __init__(self):
		super(KeyInfoResponsePacket, self).__init__()
		self.response = []
	
	def write(self, response):
		self.writeBytearray(response)
	
	def read(self):
		self.response = self.readBytearray()
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
		self.writeString(name)
		self.writeString(host)
		self.writeString(stats)
		self.writeInt32(port)
		self.writeInt32(gameid)
		self.writeInt32(keytime)
		self.writeBoolean(isfromarena)
		self.writeBytearray(key)

	def read(self):
		self.name = self.readString()
		self.host = self.readString()
		self.stats = self.readString()
		self.port = self.readInt32()
		self.gameid = self.readInt32()
		self.keytime = self.readInt32()
		self.isfromarena = self.readBoolean()
		self.key = self.readBytearray()
		return self.name, self.host, self.stats, self.port, self.gameid, self.keytime, self.isfromarena, self.key