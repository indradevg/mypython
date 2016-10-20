#!/usr/bin/python3.4

read_string=""
counter = 0
new_content = []

with open("/home/linux/example.txt", "r") as exf:
	#read_string=exf.read()
	for str1 in exf:
		for char in str1:
			if char != ' ':
	        		if counter % 2 == 0:
        	        		new_content.append(char.upper())
        			else:
                			new_content.append(char.lower())
        			counter += 1
			else:
				new_content.append(char)

print (''.join(new_content))
