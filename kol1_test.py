import unittest
from kol1 import flightSimulator

class MyTest(unittest.TestCase):
	def setUp(self):
		self.angle = 0.0
		self.angleStep = 0.5
		self.delay = 0.1
		self.test_instance = flightSimulator()

	def test_init(self):
		self.assertEqual(self.test_instance.angle, self.angle)
		self.assertEqual(self.test_instance.angleStep, self.angleStep)
		self.assertEqual(self.test_instance.delay, self.delay)

	def test_turning_left(self):
		self.angle = self.test_instance.angle
		self.test_instance.turnLeft()
		self.assertEqual(self.test_instance.angle, self.angle - self.angleStep)

	def test_turning_right(self):
		self.angle = self.test_instance.angle
		self.test_instance.turnRight()
		self.assertEqual(self.test_instance.angle, self.angle + self.angleStep)

	def test_making_turbulations(self):
		self.angle = self.test_instance.angle
		self.test_instance.makeTurbulations()
		self.assertNotEqual(self.test_instance.angle, self.angle)

	def test_making_correction(self):
		self.test_instance.angle = 5
		self.angle = 5
		self.test_instance.makeCorrection()
		self.assertEqual(self.test_instance.angle, self.angle - self.angleStep)