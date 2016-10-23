#!/usr/bin/python3

lst1=["Hi ", "There ", "how ", "are ", "you ", "doing."]

lst2=["I ","am ","doing ","good."]


print(lst1+lst2)
print ("Lenght of list 1 : ", len(lst1))
print ("Lenght of list 2 : ", len(lst2))
lst1.append("Brother")
lst2.insert(1,",")
print ("Adding one more item to list 1 ['brother'] ", lst1)
print ("Adding one correction to list 2 [','] ", lst2)

print ("Is 'Hi' Present in lst1 : {0}".format("Hi " in lst1) )


fruits = ["apple", "bananna", "grapes"]

fruits.insert(len(fruits), "Pears")

pop_item = fruits.pop()
print(pop_item)