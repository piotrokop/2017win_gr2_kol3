###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

import numpy as np
import time
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