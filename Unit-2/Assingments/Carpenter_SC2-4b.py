#Nathan Carpenter
#nov 11, 2020
#This code

import console
console.clear()

num = input("Please input a number between 100 and 1000 ")
num = int(num)
if num < 100 or num > 1000:
	x = 1
	while x == 1:
		num = input("The number you input was not inbetween 100 and 1000, please try again: ")
		num = int(num)
		
		if num < 100 or num > 1000:
			x = 1
		else:
			x = 2
	
if num > 100 and num < 1000:
	
	num = int(num)
	list1 = []
	for y in range(1, num):
		
		
		y = int(y)
		
		a = y / 3
		b = y / 7
		c = y / 5
		
		if a == int(a) and b == int(b):
			if not c == int(c):
				
				list1.append(y)
print(list1)
