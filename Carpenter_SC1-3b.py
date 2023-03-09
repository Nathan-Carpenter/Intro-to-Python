#Nathan Carpenter
#10/2/2020
#this code when a number is input will give both that number squared and the square root, and if its an integer, it will tell if its odd or even, if its not it will tell how many digits are in it


import console


def supercalc(x):
	y = x ** 2
	z = x ** 0.5
	a = len(str(x))
	print("%s squared is %s" %(x,y))
	print("The square root of %s is %s" %(x,z))
	if x == int(x):
		if (x % 2) ==0:
			print("%s is an even number" %(x))
		else:
			print("%s is an odd number" %(x))
	else:
		print("there are %s total digits in %s" %(a-1,x))
	
