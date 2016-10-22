#!/usr/bin/env python3
'''
@decorfun, decorates decorval() wrapped around it as below.

decaoval() = "This is a decorator"
@decorfun(decaorval()) = decorfun("This is a decorator")

This string/function is passed to inside_decore and "String" is call range times.
'''


def decorfun(anyfun):
	def inside_decore():
		for i in range(8):
			anyfun()

	return inside_decore
@decorfun
def decorval():
	print ("This is a decorator")

try:
	decorval()
except:
	print("Something is wrong")

