import Packets


class SpamFilter:
    def __init__(self, proxy):
        self._proxy = proxy
        self.spam_to_filter = ['realmbags', 'rpgstash', 'rotmgmax', 'realmstock', 'eye of oryx', "oryxin", "realm power.net", "rwtmg.com"]
        proxy.hookPacket(Packets.TextPacket, self.onText)

    def onText(self, client, packet):
        data = packet.read()
        for keyword in self.spam_to_filter:
            if keyword in data[5].lower():
                packet.send = False
