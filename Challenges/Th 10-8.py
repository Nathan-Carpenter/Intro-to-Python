#Nathan carpenter

import console
console.clear()

def maxmin(x,y,z):
	x = int(x)
	y = int(y)
	z = int(z)
	if x > y and x > z:
		if y > z:
			print("% is the largest number and % is the smallest number" %(x,z))
		elif z > y:
			print("% is the largest number and % is the smallest number" %(x,y))
	elif y > x and z > z:
		if x > z:
			print("% is the largest number and % is the smallest number" %(y,z))
		elif z > x:
			print("% is the largest number and % is the smallest number" %(y,x))
	elif z > x and z > y:
		if x > y:
			print("% is the largest number and % is the smallest number" %(z,y))
		elif y > x:
			print("% is the largest number and % is the smallest number" %(z,x))
# end of maxmin()----------------------------------#
