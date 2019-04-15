import Packets
import Proxy


# Basic plugin just to test the callback system
class WelcomeMessage(object):
    def __init__(self, proxy: Proxy.Proxy):
        self._proxy = proxy
        proxy.hookPacket(Packets.HelloPacket, self.onHello)
    
    def onHello(self, client, packet):
        data = packet.read()
        print(data)