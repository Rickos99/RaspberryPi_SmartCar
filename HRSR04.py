class DistanceSensor(object):
	"""Distance sensor stored as a class"""
	pulse_start = 0
	pulse_end = 0

	def __init__(self, TRIG, ECHO):
		import RPi.GPIO as GPIO
		import time

		self.gpio = GPIO
		self.time = time

		self.gpio.setmode(self.gpio.BCM)

		self.trig = TRIG
		self.echo = ECHO

		# setup GPIO
		self.gpio.setup(self.trig, self.gpio.OUT)
		self.gpio.setup(self.echo, self.gpio.IN)

		self.gpio.output(self.trig, False)

		print("Wait for distance sensor start")
		# wait for sensor to settle
		#self.time.sleep(1)

	def distance(self):
		"""Return distance from sensor as an integer"""

		self.gpio.output(self.trig, True)
		self.time.sleep(0.00001)
		self.gpio.output(self.trig, False)

		while self.gpio.input(self.echo) == 0:
			self.pulse_start = self.time.time()

		while self.gpio.input(self.echo) == 1:
			self.pulse_end = self.time.time()

		pulse_duration = self.pulse_end - self.pulse_start

		distance_n = int(pulse_duration * 17150)

		return distance_n
