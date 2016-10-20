#!/usr/bin/python3.4 
'''
When enclosed variable name "var" exist, the effect of global on nested function i.e., function enclosed with in another function, the inner function doesnt
have any effect of the global keyword and rather consider it as local.

Ex: The programme will getnerate the below output

inside inner, var is  bar
inside outer function, var is  foo

'''

var = 'Head bar'
def ex6():
	var = 'foo'
	def inner():
		global var
#		var = 'bar'
		print ('inside inner, var is ', var)

	inner()
	print ('inside outer function, var is ', var)


ex6()
print ('Var in outer function, var is ', var)

