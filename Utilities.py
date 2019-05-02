import os
import xml.etree.ElementTree as ET

import Packets


class Packetsetup:
    def __init__(self):
        tree = ET.parse(f'{os.path.dirname(os.path.realpath(__file__))}/xmls/packets.xml')
        self.root = tree.getroot()
        self.output = {}

    def setupPacket(self):
        constantpacketpointers = {'FAILURE': Packets.FailurePacket, 'CREATESUCCESS': Packets.CreateSuccessPacket,
                                  'CREATE': Packets.CreatePacket, 'PLAYERSHOOT': Packets.PlayerShootPacket,
                                  'MOVE': Packets.MovePacket, 'PLAYERTEXT': Packets.PlayerTextPacket,
                                  'TEXT': Packets.TextPacket, 'SERVERPLAYERSHOOT': None, 'DAMAGE': None, 'UPDATE': None,
                                  'UPDATEACK': Packets.UpdateAckPacket, 'NOTIFICATION': Packets.NotificationPacket,
                                  'NEWTICK': Packets.NewTickPacket, 'INVSWAP': Packets.InvSwapPacket,
                                  'USEITEM': Packets.UseItemPacket, 'SHOWEFFECT': None, 'HELLO': Packets.HelloPacket,
                                  'GOTO': None, 'INVDROP': Packets.InvDropPacket, 'INVRESULT': None,
                                  'RECONNECT': Packets.ReconnectPacket,
                                  'PING': None, 'PONG': Packets.PongPacket, 'MAPINFO': None, 'LOAD': Packets.LoadPacket,
                                  'PIC': None, 'SETCONDITION': Packets.SetConditionPacket,
                                  'TELEPORT': Packets.TeleportPacket, 'USEPORTAL': Packets.UsePortal, 'DEATH': None,
                                  'BUY': Packets.BuyPacket, 'BUYRESULT': None, 'AOE': None,
                                  'GROUNDDAMAGE': Packets.GroundDamagePacket, 'PLAYERHIT': Packets.PlayerHitPacket,
                                  'ENEMYHIT': Packets.EnemyHitPacket, 'AOEACK': Packets.AoEAckPacket,
                                  'SHOOTACK': Packets.ShootAckPacket, 'OTHERHIT': Packets.OtherHitPacket,
                                  'SQUAREHIT': Packets.SquareHitPacket, 'GOTOACK': Packets.GotoAckPacket,
                                  'EDITACCOUNTLIST': Packets.EditAccountListPacket, 'ACCOUNTLIST': None,
                                  'QUESTOBJID': None, 'CHOOSENAME': Packets.ChooseNamePacket, 'NAMERESULT': None,
                                  'CREATEGUILD': Packets.CreateGuildPacket,
                                  'GUILDRESULT': Packets.CreateGuildResultPacket,
                                  'GUILDREMOVE': Packets.GuildRemovePacket, 'GUILDINVITE': Packets.GuildInvitePacket,
                                  'ALLYSHOOT': Packets.AllyShootPacket, 'ENEMYSHOOT': Packets.EnemyShootPacket,
                                  'REQUESTTRADE': Packets.RequestTradePacket,
                                  'TRADEREQUESTED': None, 'TRADESTART': None, 'CHANGETRADE': Packets.ChangeTradePacket,
                                  'TRADECHANGED': None, 'ACCEPTTRADE': Packets.AcceptTradePacket,
                                  'CANCELTRADE': Packets.CancelTradePacket, 'TRADEDONE': None, 'TRADEACCEPTED': None,
                                  'CLIENTSTAT': None, 'CHECKCREDITS': Packets.CheckCreditsPacket,
                                  'ESCAPE': Packets.EscapePacket, 'FILE': Packets.FilePacket, 'INVITEDTOGUILD': None,
                                  'JOINGUILD': Packets.JoinGuildPacket,
                                  'CHANGEGUILDRANK': Packets.ChangeGuildRankPacket, 'PLAYSOUND': None,
                                  'GLOBALNOTIFICATION': None, 'RESKIN': Packets.ReskinPacket, 'PETUPGRADEREQUEST': None,
                                  'ACTIVEPETUPDATEREQUEST': None, 'ACTIVEPETUPDATE': None, 'NEWABILITY': None,
                                  'PETYARDUPDATE': None, 'EVOLVEPET': None, 'DELETEPET': None, 'HATCHPET': None,
                                  'ENTERARENA': Packets.EnterArenaPacket, 'IMMINENTARENAWAVE': None, 'ARENADEATH': None,
                                  'ACCEPTARENADEATH': None, 'VERIFYEMAIL': None, 'RESKINUNLOCK': None,
                                  'PASSWORDPROMPT': None, 'QUESTFETCHASK': None, 'QUESTREDEEM': None,
                                  'QUESTFETCHRESPONSE': None, 'QUESTREDEEMRESPONSE': None, 'PETCHANGEFORMMSG': None,
                                  'KEYINFOREQUEST': Packets.KeyInfoRequestPacket, 'KEYINFORESPONSE': None,
                                  'CLAIMLOGINREWARDMSG': None, 'LOGINREWARDMSG': None, 'QUESTROOMMSG': None}
        thing1 = {}
        output = {}
        for child in self.root:
            thing1[child[0].text] = int(child[1].text)
        for packet in thing1:
            output[thing1.get(packet)] = constantpacketpointers[packet]

        return output
