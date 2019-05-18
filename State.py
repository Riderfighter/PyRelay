class State:
    defaultServer = "54.183.236.213"
    defaultPort = 2050
    realConKey = b""
    realConKeyTime = -1
    lastServer = defaultServer
    lastPort = defaultPort

    def __init__(self, guid):
        self.guid = guid
