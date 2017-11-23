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

class flightSimulator():
	def __init__(self):
		self.angle = 0.0
		self.angleStep = 0.5
		self.delay = 0.1

	def turnLeft(self):
		self.angle -= self.angleStep

	def turnRight(self):
		self.angle += self.angleStep

	def start(self):
		while True:
			self.makeTurbulations()
			self.makeCorrection()
			self.printOrientation()
			time.sleep(self.delay)

			# key = ord(getch())
			# if key == 27: # ESC
			# 	break
			# elif key == 80:
			# 	self.turnLeft()
			# elif key == 72:
			# 	self.turnRight()

	def printOrientation(self):
		print self.angle

	def makeTurbulations(self):
		self.angle += np.random.normal()
		# self.angle += np.random.

	def makeCorrection(self):
		if self.angle > 0:
			self.angle -= self.angleStep
		else:
			self.angle += self.angleStep


if __name__=="__main__":
	fly = flightSimulator()
	fly.start()