#!/usr/bin/python3.4

print("Name of the programe is: {0}".format(__name__))

while True:
	s = input("Enter a sting og 4 letters width or 'q' to quite:")
	if s == 'q':
		break
	if len(s) < 4 :
		print("Value too small")
		continue
	#else:
#		print("Value too large")
#		continue
	print("String was of sufficient lenght.")
	raise SystemExit

