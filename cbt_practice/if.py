#!/usr/bin/python3.4
import os
'''
This is a test programme to test the IF functionality
Just reads a number and returns a absolute value
'''

a = int(input("Enter an interger: "))

if a < 0:
	os.system("clear")
	print("The absolute value of {0} is {1}".format(a,-a))
else:
	print("The absolute value of {0} is {1}".format(a,a))
