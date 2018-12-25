import struct
import binascii


class Packet:
	def __init__(self):
		self.data = bytearray()
		self.index = 0

	def reset(self):
		self.index = 0
		self.data.clear()

	def advance(self, amt):
		self.index += amt
		return self.index

	def readInt32(self):
		t = struct.unpack(">i", self.data[self.index:self.advance(4)])
		return t[0]
			
	def writeInt32(self, i):
		d = struct.pack(">i", i)
		self.data[self.index:self.advance(4)] = d
		
	def readUInt32(self):
		t = struct.unpack(">I", self.data[self.index:self.advance(4)])
		return t[0]
			
	def writeUInt32(self, i):
		d = struct.pack(">I", i)
		self.data[self.index:self.advance(4)] = d

	def readInt16(self):
		t = struct.unpack(">h", self.data[self.index:self.advance(2)])
		return t[0]

	def writeInt16(self, i):
		d = struct.pack(">h", i)
		self.data[self.index:self.advance(2)] = d	

	def readUInt16(self):
		t = struct.unpack(">H", self.data[self.index:self.advance(2)])
		return t[0]

	def writeUInt16(self, i):
		d = struct.pack(">H", i)
		self.data[self.index:self.advance(2)] = d

	def writeByte(self, i):
		d = struct.pack(">b", ord(i))
		self.data[self.index:self.advance(1)] = d

	def readByte(self):
		t = struct.unpack(">b", self.data[self.index:self.advance(1)])
		return t[0]

	def readFloat(self):
		t = struct.unpack(">f", self.data[self.index:self.advance(4)])
		return t[0]

	def writeFloat(self, f):
		d = struct.pack(">f", f)	
		self.data[self.index:self.advance(4)] = d
	
	def readBoolean(self):
		d = struct.unpack(">?",self.data[self.index:self.advance(1)])
		return d[0]
	
	def writeBoolean(self, bool):
		d = struct.pack(">?", bool)
		self.data[self.index:self.advance(1)] = d

	def writeString(self, str):
		length = len(str)
		self.writeInt16(length)
		if length == 0:
			return
		else:
			for i in str:
				self.writeByte(i)

	def readString(self):
		length = self.readInt16()
		if length == 0:
			return ""
		else:
			d = ""
			for _ in range(length):
				d += chr(self.readByte())	#convert the byte from byte type to int/String type
			return d
	
	def writeUTFString(self, str):
		length = len(str)
		self.writeInt32(length)
		if length == 0:
			return
		else:
			for i in str:
				self.writeByte(i.encode('utf8'))

	def readUTFString(self):
		length = self.readInt32()
		if length == 0:
			return ''
		else:
			d = ""
			for _ in range(length):
				d += chr(self.readByte())
			return d

	def writeBytearray(self, bytes):
			length = len(bytes)
			self.writeInt16(length)
			if length == 0:
				return
			else:
				for i in bytes:
					self.writeByte(i)
	
	def readBytearray(self):
		length = self.readInt16()
		if length == 0:
			return []
		else:
			d = []
			for _ in range(length):
				d.append(self.readByte())	#convert the byte from byte type to int/String type
			return d

	def writeBooleanarray(self, bytes):
		length = len(bytes)
		self.writeInt32(length)
		if length == 0:
			return
		else:
			for i in bytes:
				self.writeBoolean(i)
	
	def readBooleanarray(self):
		length = self.readInt16()
		if length == 0:
			return []
		else:
			d = []
			for _ in range(length):
				d.append(self.readBoolean())
			return d