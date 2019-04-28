import Packets
import Client
import Proxy

class SpamFilter:
    def __init__(self, proxy: Proxy.Proxy, client: Client.Client):
        self._client = client
        self._proxy = proxy
        self.spam_to_filter = ['realmbags', 'rpgstash', 'rotmgmax', 'realmstock', 'eye of oryx', "oryxin", "realm power.net", "rwtmg.com"]
        client.hookPacket(Packets.TextPacket, self.onText)

    def onText(self, packet):
        data = packet.read()
        for keyword in self.spam_to_filter:
            if keyword in data[5].lower():
                packet.send = False
