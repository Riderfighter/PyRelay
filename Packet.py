import struct


class Packet:
    def __init__(self):
        self.data = bytearray()
        self.index = 0
        self.send = True

    def reset(self):
        self.index = 0
        self.data = bytearray()

    def advance(self, amt):
        self.index += amt
        return self.index

    def read_int32(self):
        t = struct.unpack(">i", self.data[self.index:self.advance(4)])
        return t[0]

    def write_int64(self, i):
        d = struct.pack(">q", i)
        self.data[self.index:self.advance(8)] = d

    def read_int64(self):
        t = struct.unpack(">q", self.data[self.index:self.advance(8)])
        return t[0]

    def write_uint64(self, i):
        d = struct.pack(">Q", i)
        self.data[self.index:self.advance(8)] = d

    def read_uint64(self):
        t = struct.unpack(">Q", self.data[self.index:self.advance(8)])
        return t[0]

    def write_int32(self, i):
        d = struct.pack(">i", i)
        self.data[self.index:self.advance(4)] = d

    def read_uint32(self):
        t = struct.unpack(">I", self.data[self.index:self.advance(4)])
        return t[0]

    def write_uint32(self, i):
        d = struct.pack(">I", i)
        self.data[self.index:self.advance(4)] = d

    def read_int16(self):
        t = struct.unpack(">h", self.data[self.index:self.advance(2)])
        return t[0]

    def write_int16(self, i):
        d = struct.pack(">h", i)
        self.data[self.index:self.advance(2)] = d

    def read_uint16(self):
        t = struct.unpack(">H", self.data[self.index:self.advance(2)])
        return t[0]

    def write_uint16(self, i):
        d = struct.pack(">H", i)
        self.data[self.index:self.advance(2)] = d

    def write_byte(self, i):
        d = struct.pack(">b", i)
        self.data[self.index:self.advance(1)] = d

    def read_byte(self):
        t = struct.unpack(">b", self.data[self.index:self.advance(1)])
        return t[0]

    def write_unsignedbyte(self, i):
        d = struct.pack(">B", i)
        self.data[self.index:self.advance(1)] = d

    def read_unsignedbyte(self):
        t = struct.unpack(">B", self.data[self.index:self.advance(1)])
        return t[0]

    def read_float(self):
        t = struct.unpack(">f", self.data[self.index:self.advance(4)])
        return t[0]

    def write_float(self, f):
        d = struct.pack(">f", f)
        self.data[self.index:self.advance(4)] = d

    def read_boolean(self):
        d = struct.unpack(">?", self.data[self.index:self.advance(1)])
        return d[0]

    def write_boolean(self, bool):
        d = struct.pack(">?", bool)
        self.data[self.index:self.advance(1)] = d

    def write_string(self, string):
        length = len(string)
        self.write_uint16(length)
        if length == 0:
            return
        self.data[self.index:self.advance(length)] = struct.pack(f">{length}s", string.encode("utf8"))

    def read_string(self):
        length = self.read_uint16()
        if length == 0:
            return ""
        d = struct.unpack(f">{length}s", self.data[self.index:self.advance(length)])[0].decode(
            "utf8")  # convert the byte from byte type to int/String type
        return d

    def write_bytestring(self, bytes):
        length = len(bytes)
        self.write_int16(length)
        if length == 0:
            return
        self.data[self.index:self.advance(length)] = bytes

    def read_bytestring(self):
        length = self.read_int16()
        if length == 0:
            return b''
        d = bytes(self.data[self.index:self.advance(length)])
        return d

    def write_booleanarray(self, bytes):
        length = len(bytes)
        self.write_int32(length)
        if length == 0:
            return
        for i in bytes:
            self.write_boolean(i)

    def read_booleanarray(self):
        length = self.read_int16()
        if length == 0:
            return []
        d = []
        for _ in range(length):
            d.append(self.read_boolean())
        return d