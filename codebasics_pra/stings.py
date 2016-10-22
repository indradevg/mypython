#!/usr/bin/python3

str1="Welcome to Python"
str2='hi there'

print ("++++++++  STRING OPERATIONS ++++++++")

print('''
str1[0:6] : {0}
str1[5:] : {1}
str1[-9:-1] : {2}'''.format(str1[0:6], str1[5:], str1[-9:-1]) )

print('''Sum of string str1 and str2 : {0} '''.format(str1+" "+str2))
