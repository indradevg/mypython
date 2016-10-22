#!/usr/bin/python3.4

def adder():
	def inadd(*arry):
		total = 0
		for i in arry:
			total += i
		return total
	return inadd


a = adder()
print(a(1,2,3))
print(a(1,4,5,7))
