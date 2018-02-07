class Car(object):
	"""Class to move car forward"""
	def __init__(self, left_servo_channel, right_servo_channel):
		# Import the PCA9685 module
		import Adafruit_PCA9685

		# set which channel servo is assigned to
		self.left_servo = left_servo_channel
		self.right_servo = right_servo_channel

		# Initialise the PCA9685 using the default address (0x40).
		self.pwm = Adafruit_PCA9685.PCA9685()

		# Set frequency to 60hz, good for servos.
		self.pwm.set_pwm_freq(60)

	# Helper function to make setting a servo pulse width simpler.
	def set_servo_pulse(self, channel, pulse):
		"""set servo pulse"""
		pulse_length = 1000000    # 1,000,000 us per second
		pulse_length //= 60       # 60 Hz
		print('{0}us per period'.format(pulse_length))
		pulse_length //= 4096     # 12 bits of resolution
		print('{0}us per bit'.format(pulse_length))
		pulse *= 1000
		pulse //= pulse_length
		self.pwm.set_pwm(channel, 0, pulse)

	# set left servo to forward
	def servo_left_forward(self):
		"""move left servo forwards relative to the cars position"""
		pulse = 150
		self.pwm.set_pwm(self.left_servo, 0, pulse)

	# set left servo to backward
	def servo_left_backward(self):
		"""move left servo backwards relative to the cars position"""
		pulse = 600
		self.pwm.set_pwm(self.left_servo, 0, pulse)

	# set left servo to stop
	def servo_left_stop(self):
		"""stop left servo"""
		pulse = 0
		self.pwm.set_pwm(self.left_servo, 0, pulse)

	# set right servo to forward
	def servo_right_forward(self):
		"""move right servo forwards relative to the cars position"""
		pulse = 600
		self.pwm.set_pwm(self.right_servo, 0, pulse)

	# set right servo to backward
	def servo_right_backward(self):
		"""move right servo backwards relative to the cars position"""
		pulse = 150
		self.pwm.set_pwm(self.right_servo, 0, pulse)

	# set right servo to stop
	def servo_right_stop(self):
		"""stop right servo"""
		pulse = 0
		self.pwm.set_pwm(self.right_servo, 0, pulse)

	# move car forward
	def move_forward(self):
		"""move car forward"""
		self.servo_left_forward()
		self.servo_right_forward()

	# move car backward
	def move_backward(self):
		"""move car backward"""
		self.servo_left_backward()
		self.servo_right_backward()

	# move car left
	def move_left(self):
		"""rotate car to the left"""
		self.servo_left_backward()
		self.servo_right_forward()

	# move car right
	def move_right(self):
		"""rotate car to the right"""
		self.servo_right_backward()
		self.servo_left_forward()

	# stop car
	def move_stop(self):
		"""bring car to stop"""
		self.servo_left_stop()
		self.servo_right_stop()
