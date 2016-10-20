#!/usr/bin/env python3

from sys import exit

def gensq(n):
	for i in range(n):
		yield i ** 2

rg = int(input("Enter the largest value: "))


if rg <= 0:
        exit("Enter a valid interger...")

a = gensq(rg)

#print (next(a))
#print (next(a))
#print (next(a))
#print (next(a))


while rg > 0:
	resp = input("Do you want to Continue (y/n): ")
	
	rg -= 1

	if resp == 'y':
		#print (rg)
		print (next(a))
	else:
		exit("Thanks for using this program....")

else:
	print ("Thanks for using this program.....")
