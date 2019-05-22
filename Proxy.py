import socket
import threading
import time

import Client


# 6a39570cc9de4ec71d64821894 c79332b197f92ba85ed281a023
# Client.py to proxy only

class Proxy(object):
    _debug = True
    # Constant variables/classes
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # commonly mutated variables/classes
    # Dont access _packetHooks/_commandHooks directly, they are considered private variables.
    states = {}

    @staticmethod
    def enable_swf_for_proxy():
        adobe_policy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        adobe_policy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        adobe_policy.bind(('127.0.0.1', 843))
        adobe_policy.listen(1)
        while True:
            policy, addr = adobe_policy.accept()
            print("sending xml")
            policy.sendall(
                b'<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            policy.close()

    def enable_clients(self):
        # TODO: Allow multiple clients connected to the proxy and handle each individually
        self.listener.bind(('127.0.0.1', 2050))
        self.listener.listen(5)
        while True:
            client, _ = self.listener.accept()
            client1 = Client.Client(self, client)
            threading.Thread(target=client1.start).start()
            time.sleep(0.005)  # Don't touch this, if you do your cpu usage rises to like 99.8%

    def start(self):
        if not self._debug:
            threading.Thread(target=self.enable_swf_for_proxy).start()
        threading.Thread(target=self.enable_clients).start()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.start()
