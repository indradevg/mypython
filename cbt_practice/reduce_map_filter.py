#!/usr/bin/python3.4
from functools import reduce

'''
Program demonstrating the function of 3 built in functions viz.., "reduce", "map", "filter"
'''

'''
To Concatnate the Array elements as one string
'''
def addval(a,b):
        return a + b


'''
Find the vowels in the given string
'''
def fvow(a):
        return a.lower() in [ "a", "e", "i", "o", "u"]


l1=["I", "am", "a", "happy", "Man"]

print(list(reduce(addval, l1)))
print(list(map(fvow, list(reduce(addval, l1)))))
print(list(filter(fvow, list(reduce(addval, l1)))))


