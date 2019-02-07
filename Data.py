#class for data structure so i can kep track of all necessary info
class Data():
	#parameters
	#t is file number; lat is line number; lon is posiiton in line; v is the actual value
	def __init__(self, time, latitude, longitude, v):
		self.t = time
		self.lat = latitude
		self.lon = longitude
		self.val = v

	def __str__(self):
		return str((self.t, self.lat, self.lon, self.val))

	#self and other are from adjacent time frames and same lat/lon
	def __add__(self, other):
		return Data((self.t + other.t)/2, self.lat, self.lon, (self.val + other.val)/2)

	#pass in string tuple, returns Data object
	def fromStr(s):
		s = s.split(", ")
		t = int(s[0][-1:])
		la = int(s[1])
		lo = int(s[2])
		v = float(s[3][:-1])
		return Data(t, la, lo, v)