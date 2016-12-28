from soco import SoCo

class Sonos(object):
	IP = "xxxxx"
	def __init__(self):
		self.connection = SoCo(self.IP)

	def pause(self):
		self.connection.pause()

	def play(self):
		self.connection.play()

	def next(self):
		self.connection.next()

	def getCurrentTrack(self):
		return self.connection.get_current_track_info()