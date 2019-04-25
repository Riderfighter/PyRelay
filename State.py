class State:
    defaultServer = "54.183.236.213"
    defaultPort = 2050
    realConKey = b''
    lastServer = defaultServer
    lastPort = defaultPort

    def __init__(self, guid):
        self.guid = guid
