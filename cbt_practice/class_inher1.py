#!/usr/bin/python3.4

class BaseClass(object):
	def __init__ (self):
		print ("Inside Base Class")

	def inbase(self):
		print ("I am a function inside BC")

class Dc(BaseClass):
	def __init__ (self):
		super(Dc, self).__init__()
		self.dcvar="I am a var in Dc"

	def strptr(self):
		print ("Inside Derived Class")
		print ("Value of DcVar is: {0}".format(self.dcvar))

x = Dc()

print(type(x))
x.inbase()
print (x.dcvar)
x.strptr()



