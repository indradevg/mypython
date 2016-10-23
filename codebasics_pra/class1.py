class Student:

    def __init__ (self, n, a, s):
        self.name = n
        self.age = a
        self.sex = s
    
    def print_val (self):
        print ('''
        Hi {0} !!!, Welcome aboard.
        According to you age [{1}], you have been choosed to grade 3.

        Have a great day {2} 
        '''.format(self.name, self.age, self.sex))

Stu1 = Student("Indra", 29, "Male")
Stu2 = Student("Tippo", 2, "Female")

Stu1.print_val()
Stu2.print_val()

