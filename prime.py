#!/usr/bin/python3.4
'''
Prime number 
'''

import functools

nums = range(2, 50) 
for i in range(2, 8): 
    nums = list(filter(lambda x: x == i or x % i, nums))

print(nums)


''' 
Lambda Examples
'''

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print(list(filter(lambda x: x % 3 == 0, foo)))

print(list(map(lambda x: x * 2 + 10, foo)))

print(functools.reduce(lambda x, y: x + y, foo))
