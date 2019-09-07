import Packets
import Proxy


class Glow:
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self._proxy.hookPacket(Packets.UpdatePacket, self.onUpdate)

    def onUpdate(self, packet: Packets.UpdatePacket):
        for entity in packet.newobjs:
            if entity.status.object_id == self._proxy.playerid:
                for statdata in entity.status.data:
                    if statdata.id.m_type == 59:
                        statdata.IntValue = 100
