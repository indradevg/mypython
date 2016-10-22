#!/usr/bin/python3.4

def summ(a=0,b=0):
    return a+b

a=int(input("Enter an interger: "))
b=int(input("Enter another interger: "))

print("Sum of {0} and {1} is: {2}".format(a,b,summ(a,b)))
print("Sum without any arguments: {0}".format(summ()))
print("Sum of {0} and {1} is: {2}".format(1,0,summ(a=1)))
