#Nathan Carpenter
#Nov 1, 2020
#This code has a dictionary with 5 items and either gives detail about one or adds a new item to the dictionary


#im using a function so that I can show both results in the console

def start(): 
	dict1 = {
		"pens": 8,
		"pencils": 12,
		"sketchbooks": 3,
		"markers": 18,
		"erasers": 2
	}
	
	
	print(dict1)
	iteminspect = input("What drawing item would you like to inspect? ")
	
	if iteminspect in dict1:
		
		x = dict1[iteminspect]
		
		print("You have %s %s in your bag" %(x, iteminspect))

	else:
		itemnum = input("That item is not in the bag. How many do you put in? ")	
		dict1[iteminspect] = itemnum
		
		print("")
		print("The new bag is %s" %(dict1))
	

