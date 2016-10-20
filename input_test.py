lb = int(input("Enter a lower bound value: "))
ub = int(input("Enter a upper bound value: "))

print("You have selected lower bound as: {0} \n \
You have selected upper bound as: {1} \n".format(lb, ub))

verif = input("Do you want to continue (y/n): ")
resp=verif.lower()

if resp == 'y':
	for mul in range (lb, (ub+1)):
		for i in range (1, 11):
			print("{0} * {1} = {2}".format(mul, i, i*mul))
		print("\n")
else:
	print("We're Done!!! Bye :-) \n")

	
