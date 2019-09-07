import math

import Packet


class StatType:
    MaximumHP = 0
    HP = 1
    Size = 2
    MaximumMP = 3
    MP = 4
    NextLevelExperience = 5
    Experience = 6
    Level = 7
    Inventory0 = 8
    Inventory1 = 9
    Inventory2 = 10
    Inventory3 = 11
    Inventory4 = 12
    Inventory5 = 13
    Inventory6 = 14
    Inventory7 = 15
    Inventory8 = 16
    Inventory9 = 17
    Inventory10 = 18
    Inventory11 = 19
    Attack = 20
    Defense = 21
    Speed = 22
    Vitality = 26
    Wisdom = 27
    Dexterity = 28
    Effects = 29
    Stars = 30
    Name = 31
    Texture1 = 32
    Texture2 = 33
    MerchandiseType = 34
    Credits = 35
    MerchandisePrice = 36
    PortalUsable = 37
    AccountId = 38
    AccountFame = 39
    MerchandiseCurrency = 40
    ObjectConnection = 41
    MerchandiseRemainingCount = 42
    MerchandiseRemainingMinutes = 43
    MerchandiseDiscount = 44
    MerchandiserankRequirement = 45
    HealthBonus = 46
    ManaBonus = 47
    AttackBonus = 48
    DefenseBonus = 49
    SpeedBonus = 0
    VitalityBonus = 51
    WisdomBonus = 52
    DexterityBonus = 53
    OwnerAccountId = 54
    RankRequired = 55
    NameChosen = 56
    CharacterFame = 57
    CharacterFameGoal = 58
    Glowing = 59
    SinkLevel = 60
    AltTextureIndex = 61
    GuildName = 62
    GuildRank = 63
    OxygenBar = 64
    XpBoosterActive = 65
    XpBoostTime = 66
    LootDropBoostTime = 67
    LootTierBoostTime = 68
    HealthPotionCount = 69
    MagicPotionCount = 70
    Backpack0 = 71
    Backpack1 = 72
    Backpack2 = 73
    Backpack3 = 74
    Backpack4 = 75
    Backpack5 = 76
    Backpack6 = 77
    Backpack7 = 78
    HasBackpack = 79
    Skin = 80
    PetInstanceId = 81
    PetName = 82
    PetType = 83
    PetRarity = 84
    PetMaximumLevel = 85
    PetFamily = 86
    PetPoints0 = 87
    PetPoints1 = 88
    PetPoints2 = 89
    PetLevel0 = 90
    PetLevel1 = 91
    PetLevel2 = 92
    PetAbilityType0 = 93
    PetAbilityType1 = 94
    PetAbilityType2 = 95
    Effects2 = 96
    FortuneTokens = 97
    SupporterPointsStat = 98
    SupporterStat = 99
    m_type = None

    def __init__(self, ttype):
        self.m_type = ttype

    def isutf8(self):
        return self.m_type in (self.Name, self.AccountId, self.OwnerAccountId, self.GuildName, self.PetName)


class StatData:
    id: StatType = None
    IntValue = 0
    StringValue = ""

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def isStringData(self):
        return self.id.isutf8()

    def read(self):
        self.id = StatType(self.sprcls.read_byte())
        if self.isStringData():
            self.StringValue = self.sprcls.read_string()
        else:
            self.IntValue = self.sprcls.read_int32()
        return self.id, self.StringValue, self.IntValue

    def write(self):
        self.sprcls.write_byte(self.id.m_type)
        if self.isStringData():
            self.sprcls.write_string(self.StringValue)
        else:
            self.sprcls.write_int32(self.IntValue)


class Location:
    x = 0.0
    y = 0.0

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.x = self.sprcls.read_float()
        self.y = self.sprcls.read_float()
        return self.x, self.y

    def write(self):
        self.sprcls.write_float(self.x)
        self.sprcls.write_float(self.y)

    def DistanceSquaredTo(self, location):
        dx = location.x - self.x
        dy = location.y - self.y
        return dx * dx + dy * dy

    def DistanceTo(self, location):
        return math.sqrt(self.DistanceSquaredTo(location))

    def GetAngle(self, l1, l2):
        dX = l2.x - l1.x
        dY = l2.y - l1.y
        return math.atan2(dY, dX)

    def GetAngle2(self, x1, y1, x2, y2):
        dX = x2 - x1
        dY = y2 - y1
        return math.atan2(dX, dY)


class MoveRecord:
    time = 0
    x = 0
    y = 0

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.time = self.sprcls.read_int32()
        self.x = self.sprcls.read_float()
        self.y = self.sprcls.read_float()
        return self.time, self.x, self.y

    def write(self):
        self.sprcls.write_int32(self.time)
        self.sprcls.write_float(self.x)
        self.sprcls.write_float(self.y)


class Status:
    object_id = 0
    position: Location = None
    data = []

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.object_id = self.sprcls.read_int32()
        self.position = Location(self.sprcls)
        self.position.read()
        self.data = list(range(self.sprcls.read_int16()))
        for _ in range(len(self.data)):
            statData = StatData(self.sprcls)
            statData.read()
            self.data[_] = statData
        return self.object_id, self.position, self.data

    def write(self):
        self.sprcls.write_int32(self.object_id)
        self.position.write()
        self.sprcls.write_int16(len(self.data))
        for status in self.data:
            status.write()


class Tile:
    x = 0
    y = 0
    type = 0

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.x = self.sprcls.read_int16()
        self.y = self.sprcls.read_int16()
        self.type = self.sprcls.read_uint16()
        return self.x, self.y, self.type

    def write(self):
        self.sprcls.write_int16(self.x)
        self.sprcls.write_int16(self.y)
        self.sprcls.write_uint16(self.type)


class Entity:
    objecttype = 0
    status: Status = None

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.objecttype = self.sprcls.read_int16()
        self.status = Status(self.sprcls)
        self.status.read()
        return self.objecttype, self.status

    def write(self):
        self.sprcls.write_int16(self.objecttype)
        self.status.write()


class SlotObject:
    objectid = 0
    slotid = 0
    objecttype = 0

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.objectid = self.sprcls.read_int32()
        self.slotid = self.sprcls.read_byte()
        self.objecttype = self.sprcls.read_int32()

    def write(self):
        self.sprcls.write_int32(self.objectid)
        self.sprcls.write_byte(self.slotid)
        self.sprcls.write_int32(self.objecttype)


class Item:
    itemItem = 0
    slotType = 0
    tradeable = False
    included = False

    def __init__(self, superclass: Packet.Packet):
        self.sprcls = superclass

    def read(self):
        self.itemItem = self.sprcls.read_int32()
        self.slotType = self.sprcls.read_int32()
        self.tradeable = self.sprcls.read_boolean()
        self.included = self.sprcls.read_boolean()

    def write(self):
        self.sprcls.write_int32(self.itemItem)
        self.sprcls.write_int32(self.slotType)
        self.sprcls.write_boolean(self.tradeable)
        self.sprcls.write_boolean(self.included)
