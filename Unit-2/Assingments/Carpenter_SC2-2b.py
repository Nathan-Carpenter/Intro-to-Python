#Nathan Carpenter
#Nov 1, 2020
#


inventory = {
	"pens": 8,
	"pencils": 12,
	"sketchbooks": 3,
	"markers": 18,
	"erasers": 2
}

print(inventory)
print("Use the function 'adjust' to increase and/or decrease items")

def adjust():
	change1 = input("Which item would you like to adjust? ")
	a = input("Would you like to increase or decrease %s? " %(change1))
	
	change2 = input("Which item would you like to adjust? ")
	b = input("Would you like to increase or decrease %s? " %(change2))
	
	change3 = input("Which item would you like to adjust?")
	c = input("Would you like to increase or decrease %s? " %(change3))
	
	#adjusting via 1st input
	
	
	if a == "increase":
		x = inventory[change1]
		inventory[change1] = x + 1
	
	elif a == "decrease":
		x = inventory[change1]
		inventory[change1] = x - 1	
		
		
	if b == "increase":
		y = inventory[change2]
		inventory[change2] = y + 1
		
	elif b == "decrease":
		y = inventory[change2]
		inventory[change2] = y - 1
	
	
	if c == "increase":
		z = inventory[change3]
		inventory[change3] = z + 1
		
	elif c == "decrease":
		z = inventory[change3]
		inventory[change3] = z - 1
		
	print(inventory)
