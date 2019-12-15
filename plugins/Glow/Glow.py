import Packets
import Proxy


class Glow:
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self._proxy.hookPacket(Packets.UpdatePacket, self.onUpdate)
        self._proxy.hookPacket(Packets.PlayerShootPacket, self.onAllyShoot)

    def onAllyShoot(self, packet: Packets.PlayerShootPacket):
        if packet.angle < 0:
            angle = (packet.angle * -1) * 57.296
        else:
            angle = 180 + (180 - (packet.angle * 57.296))
        print(angle)

    def onUpdate(self, packet: Packets.UpdatePacket):
        for entity in packet.newobjs:
            if entity.status.object_id == self._proxy.playerid:
                for statdata in entity.status.data:
                    if statdata.id == statdata.id.Stats.SupporterStat:
                        statdata.IntValue = 1