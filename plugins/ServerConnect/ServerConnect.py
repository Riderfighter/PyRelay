import Packets
import Proxy


class ServerConnect:
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        self.servers = {
            "use": "52.23.232.42",
            "ase": "52.77.221.237",
            "uss": "52.91.68.60",
            "ussw": "54.183.179.205",
            "use2": "3.88.196.105",
            "usnw": "54.234.151.78",
            "ae": "54.199.197.208",
            "eusw": "52.47.178.13",
            "uss2": "54.183.236.213",
            "eun2": "52.59.198.155",
            "eus": "35.180.134.209",
            "uss3": "13.57.182.96",
            "euw2": "34.243.37.98",
            "usmw": "13.59.49.120",
            "euw": "52.47.149.74",
            "use3": "54.157.6.58",
            "usw": "13.57.254.131",
            "usw3": "54.67.119.179",
            "usmw2": "18.218.255.91",
            "eue": "18.195.167.79",
            "aus": "54.252.165.65",
            "eun": "54.93.78.148",
            "usw2": "54.215.251.128"
        }
        self._proxy.hookCommand("conn", self.connect_to_server)
        # self._proxy.hookPacket(Packets.CreateSuccessPacket, self.onCreateSuccess)

    def onCreateSuccess(self, packet: Packets.CreateSuccessPacket):
        textpacket = Packets.TextPacket()
        textpacket.bubbletime = 0
        textpacket.cleantext = f'Thanks for using ServerConnect, try me out with "/conn usw2"'
        textpacket.name = "#ServerConnect"
        textpacket.numstars = -1
        textpacket.objectid = -1
        textpacket.recipient = ""
        textpacket.text = f'Thanks for using ServerConnect, try me out with "/conn usw2"'
        textpacket.write()
        self._proxy.sendToClient(textpacket)

    def connect_to_server(self, args):
        if args[0] in self.servers:
            ip = self.servers[args[0]]
            self._proxy.defaultServer = ip
            self._proxy.lastServer = ip
            packet = Packets.ReconnectPacket()
            # name, host, stats, port, gameId, keyTime, isFromArena, key
            packet.name = "{\"text\":\"server.nexus\"}"
            packet.host = "localhost"
            packet.stats = ""
            packet.port = 2050
            packet.gameId = -2
            packet.keyTime = 0
            packet.isFromArena = False
            packet.key = b""
            packet.write()
            self._proxy.sendToClient(packet)
            # self._proxy.restartProxy()
        else:
            textpacket = Packets.TextPacket()
            textpacket.bubbletime = 0
            textpacket.cleantext = f'"{args[0]}" is not a valid server. Try one of these: {", ".join(self.servers.keys())}!'
            textpacket.name = "#ServerConnect"
            textpacket.numstars = -1
            textpacket.objectid = -1
            textpacket.recipient = ""
            textpacket.text = f'"{args[0]}" is not a valid server. Try one of these: {", ".join(self.servers.keys())}!'
            textpacket.write()
            self._proxy.sendToClient(textpacket)
