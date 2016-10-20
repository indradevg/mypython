class Charecter():

	char_count=0
	__MAX_HEALTH__ = 100

	def __init__(self,name):
		self.mem = name
		self.health = Charecter.__MAX_HEALTH__
		Charecter.char_count += 1


spidy = Charecter("Spiderman")
batman = Charecter("BatMan")

print (Charecter.char_count)
print (spidy.health, batman.health)
