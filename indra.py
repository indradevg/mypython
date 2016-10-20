class Human():
	"""docstring for ClassName"""
	def __init__(self, name, age, gender):
		self.n = name
		self.a = age
		self.g = gender

	def speak_name(self):
		print("Hi {0}!!!, I wonder if you are really {1}, you such a sexy {2}".format(self.n, self.a, self.g))

	def perform_math(self, fun1, *values):
		print('''Well {0}, I know you are a math genie. 
Well lets see what how many lacs will you earn: {1}'''.format(self.n, fun1(*values))


def sum_up(*input_num):
	tot = 0
	for num in input_num:
		tot += num
	return tot

Indra = Human("Indra", "29", "Male")

Indra.speak_name()

Indra.perform_math(sum_up, 1, 2, 3)

Indra.perform_math(sum_up, 10, 20, 30)
