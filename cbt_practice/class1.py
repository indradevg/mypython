#!/usr/bin/python3.4

import math

''' "Circle", calculates the area and length of the circle. 
NOTE: with a varying radius.'''

class Circle:
	# init will be called upon instance creation of the class. Like constructors in Java.
	def __init__(self,radius):
		self.rad=radius
		self.area=0
		self.length=0

	'''Function to calculate area of the circle'''
	def getArea(self):
		self.area= math.pi * self.rad * self.rad
#		return self.area


	'''Function to calcluate the length of the circle'''
	def getLength(self):
		self.length= 2 * math.pi * self.rad
#		return self.length

	'''Function to read the radius from user'''
	def setRad(self, radius):
		self.rad=radius

	'''Function to return the string format of all functions'''
	def __str__(self):
		self.getLength()
		self.getArea()
		return "Radius of circle: {0}\n Area of Circle:  {1} \n Length of Circle: {2}".format(self.rad, self.area, self.length)
