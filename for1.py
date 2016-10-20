#!/usr/bin/python3.4
i=10

print("i value before : the loop: ", i)

for i in range(5):
	print(i)

'''
The for loops work in such a way that leave's behind the i value
to the end of the loop and re-assigns the value to i which was initializd as 10 in our case
'''
print("i value after the loop: ", i)

'''
The below line in the for loop when enclosed in the [ ] will not allow the for loop variable leak
However, in Python 3.x, we can use closures to prevent the for-loop variable to cut into the global namespace
'''
i = 1
#print([i for i in range(5)])
[print(i) for i in range(5)]
print(i, '-> i in global')
