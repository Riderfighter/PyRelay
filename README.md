# PyRelay

---

## What is PyRelay?

> PyRelay is a high preformance, modular tcp relay that can read and inject packets into clients fully written in python with limited third-party dependencies.

---

### Differences between master branch and dev.

> The main difference between the master branch and the dev branch is that the master branch allows you to have only one client connected but you are able to freely connect to whatever dungeon you want. The dev branch is an attempt at making the proxy support multiple clients at once and while this doesn't *exactly* work as it should you aren't able to connect to realms or vault without the whole relay crashing sadly :(

---

#### Todo:
- [X] Allow clients to reconnect to proxy.
    - Works on master branch flawlessly but fails in the dev branch.
- [X] Allow multiple clients to connect to proxy.
    - Sort of works on dev branch not on master though.
- [ ] Kill the socket connect to server in order to reset the serverside ciphers and not cause 10 minute disconnects.
    - This is an important thing that needs to be done but I've attempted to no avail.
- [X] Implement a plugin system.
    - [X] Allow commands to be set via plugins.
    - [X] Allow plugins to load on proxy startup.
    - [X] Reload all plugins for a client with a `/reload` command.
- [ ] Implement all packets.
    - [X] Implement core client packets.
    - [X] Implement core server packets.
- [ ] Implement an easy handler to objects.xml for plugins
- [ ] Implement a JSON socket which will allow third party languages such as JS, Go, or LUA to communicate with proxy.
    - [ ] Send packets for other langs to read.
    - [ ] Allow receiving JSON to be converted into packets to send to server/client.
    - [ ] Allow third party langs to disable core plugins such as reconnecthandler and reimplement them in their own langs.
- [ ] Make a nice GUI in QT or something, CLIs hurt my eyes
