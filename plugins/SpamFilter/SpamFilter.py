import packets


class SpamFilter(object):
    def __init__(self, proxy):
        self._proxy = proxy
        self.spam_to_filter = ['realmbags', 'rpgstash', 'rotmgmax', 'realmstock', 'eye of oryx', "oryx.in", "realm power.net", "rwtmg.com"]
        proxy.hookPacket(packets.TextPacket, self.onText)

    def onText(self, packet):
        data = packet.read()
        for keyword in self.spam_to_filter:
            if keyword in data[5].lower():
                packet.send = False
