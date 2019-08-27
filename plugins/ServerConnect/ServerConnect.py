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
        proxy.hookCommand("conn", self.connect_to_server)

    def connect_to_server(self, args):
        if args[0] in self.servers:
            ip = self.servers[args[0]]
            self._proxy.defaultServer = ip
            self._proxy.lastServer = ip
            packet = Packets.ReconnectPacket()
            # name, host, stats, port, gameid, keytime, isfromarena, key
            packet.write("{\"text\":\"server.nexus\"}", "localhost", "", 2050, -2, 0, False, b"")
            self._proxy.sendToClient(packet)
            # self._proxy.restartProxy()
        else:
            packet = Packets.GlobalNotificationPacket()
            packet.write(self._proxy.playerid,
                         f'{args[0]} is not a valid server. Try one of the following: {" ".join(self.servers)}')
            self._proxy.sendToClient(packet)
