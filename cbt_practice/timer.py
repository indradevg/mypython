#!/usr/bin/python3.4

import os

print ("Welcome to the timer")
timr = int(input("Enter how many sec you need the timer for: "))

while timr >= 0:
	if (timr%5) == 0:
		print ("%s sec left" % ((str(timr)).zfill(2)))
		os.system('sleep 1')
		timr -= 1
	else:
		os.system('sleep 1')
		timr -= 1
		continue


if timr == -1:
	print ("BOOM THE TIMER COMPLETED")
