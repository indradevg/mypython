#!/usr/bin/python3.4
class BaseClass(object): 
	def __init__(self): 
		self.val = 100 
	
	def printMe(self): 
		print ("PrintMe")

class ChildClass(BaseClass): 
	def __init__(self): 
		super(ChildClass, self).__init__() 

		


x = ChildClass() 
x.printMe()
print (x.val)
