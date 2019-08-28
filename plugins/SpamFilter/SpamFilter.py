import Packets
import Proxy

class SpamFilter:
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self.spam_to_filter = ['realmbags', 'rpgstash', 'rotmgmax', 'realmstock', 'eye of oryx', "oryxin",
                               "realm power.net", "rwtmg.com", "realmpower", "rqru", "rotmgstore"]
        proxy.hookPacket(Packets.TextPacket, self.onText)

    def onText(self, packet: Packets.TextPacket):
        # data = packet.read()
        for keyword in self.spam_to_filter:
            if keyword.lower() in packet.text.lower():
                packet.send = False
