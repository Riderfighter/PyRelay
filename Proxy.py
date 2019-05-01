import importlib
import os
import socket
import struct
import threading
import time

import Client
import Packet
import Utilities


# 6a39570cc9de4ec71d64821894 c79332b197f92ba85ed281a023
# client to proxy only

class Proxy(object):
    # Constant variables/classes
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _clients = []
    # commonly mutated variables/classes
    # Dont access _packetHooks/_commandHooks directly, they are considered private variables.
    states = {}

    def enableSWFPROXY(self):
        adobe_policy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        adobe_policy.bind(('127.0.0.1', 843))
        adobe_policy.listen(1)
        while True:
            policy, addr = adobe_policy.accept()
            print("sending xml")
            policy.sendall(
                b'<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>')
            policy.close()

    def enableClients(self):
        # TODO: Allow multiple clients connected to the proxy and handle each individually
        self.listener.bind(('127.0.0.1', 2050))
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.listen(5)
        while True:
            client, _ = self.listener.accept()
            client = Client.Client(self, client)
            threading.Thread(target=client.start).start()
            time.sleep(0.005)  # Don't touch this, if you do your cpu usage rises to like 99.8%

    def start(self):
        threading.Thread(target=self.enableSWFPROXY).start()
        threading.Thread(target=self.enableClients).start()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.start()
