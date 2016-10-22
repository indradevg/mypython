#!/usr/bin/python3.4

inf = input("Enter the path of the file: ")
mode = input ("Enter the mode in which you need it to open")

with open(inf, mode) as myfil:
        for i in myfil.readlines():
                print (i)
