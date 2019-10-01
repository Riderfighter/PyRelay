import Packets
import Proxy

class GoldDigger:
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self._proxy.hookPacket(Packets.UpdatePacket, self.onUpdate)

    def onUpdate(self, packet: Packets.UpdatePacket):
        for entity in packet.newobjs:
			for statdata in entity.status.data:
				if statdata.id.m_type == statdata.id.Name:
					if statdata.StringValue != "":
						for statdata in entity.status.data:
							if statdata.id.m_type == statdata.id.Credits:
								print(statdata.IntValue)
				
