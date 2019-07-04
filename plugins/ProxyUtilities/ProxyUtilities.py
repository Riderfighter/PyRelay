import threading
import uuid

import Client
import Packets
import Proxy
import State


# Basic plugin just to test the callback system
class ProxyUtilities:
    # TODO: Handle joining realms
    def __init__(self, proxy: Proxy.Proxy, client: Client.Client):
        self._client = client
        self._proxy = proxy
        self.objectId = 0
        client.hook_packet(Packets.HelloPacket, self.on_hello)
        client.hook_packet(Packets.CreateSuccessPacket, self.on_create_success)
        client.hook_packet(Packets.ReconnectPacket, self.on_reconnect)
        client.hook_packet(Packets.FailurePacket, self.on_failure)
        client.hook_command("reload", self.reload_plugins)
        client.hook_command("plugintest", self.send_test)

    def send_test(self, args):
        packet = Packets.NotificationPacket()
        packet.write(self.objectId, "Ran plugin test.", 0x8B00FF)
        self._client.send_to_client(packet)

    def reload_plugins(self, args):
        self._client.load_plugins()
        new_packet = Packets.NotificationPacket()
        new_packet.write(self.objectId, "Plugins reloaded.", 0x8B00FF)
        self._client.send_to_client(new_packet)

    @staticmethod
    def on_failure(packet: Packets.FailurePacket):
        data = packet.read()
        print(data)

    def on_hello(self, packet: Packets.HelloPacket):
        """
        This is really dumb I need to debug this more on why it doesn't work. I would like to use PyCharm debug mode to
        see the stack but but I need to run with sudo and pycharm can't do that.

        I'm reconsidering this IDE more and more everyday.
        """
        data = packet.read()

        if len(packet.key) != 0:
            packet.send = False
            state = self._proxy.states[bytes.hex(packet.key)]
            self._client.state = state
            new_packet = Packets.HelloPacket()
            new_packet.write(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                             bytes.fromhex(state.realConKey), data[9], data[10], data[11], data[12], data[13], data[14],
                             data[15])
            self._client.state.realConKey = ""
            self._client.send_to_server(new_packet)
        else:
            print("Generating new state")
            guid = uuid.uuid4().hex
            s = State.State(guid)
            self._client.state = s
            self._proxy.states[guid] = s

    def on_reconnect(self, packet: Packets.ReconnectPacket):
        packet.send = False
        packet.read()
        new_packet = Packets.ReconnectPacket()
        if packet.host:
            self._client.state.lastServer = packet.host
        if packet.port != -1:
            self._client.state.lastPort = packet.port
        if packet.key:
            self._client.state.realConKey = bytes.hex(packet.key)
            self._client.state.realConKeyTime = packet.keytime
        new_packet.write(packet.name, "localhost", packet.stats, 2050, packet.gameid, packet.keytime,
                         packet.isfromarena, bytes.fromhex(self._client.state.guid))
        self._client.send_to_client(new_packet)
        self._client.shutdown_client()

    def on_create_success(self, packet: Packets.CreateSuccessPacket):
        data = packet.read()
        self.objectId = data[0]
        new_packet = Packets.NotificationPacket()
        new_packet.write(self.objectId, "Welcome to PyRelay!", 0x8B00FF)
        threading.Timer(1.5, self._client.send_to_client, args=(new_packet,)).start()
