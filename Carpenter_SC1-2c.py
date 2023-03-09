#Nathan Carpenter
#9-25-20
#this code asks a question and then depending on the responce gives 1 of 2 questions

import console
console.clear()

q1 = input("Do you like warm or cool colors better? ")

if q1 == "warm".lower() or "warm colors".lower():
	q2 = input("Which color do you like the best, Red, Orange, Yellow, Green, or Purple? ")
	
	if q2 == "red".lower():
		print("Nice! I think red is a really cool color as well")
	elif q2 == "orange".lower():
		print("Orange is a nice color")
	elif q2 == "yellow".lower():
		print("Cool, I also really like yellow, it makes really pretty flowers")
	elif q2 == "green".lower():
		print("Oh nice! I also like green because it can be either a cool or warm color")
	elif q2 == "purple".lower():
		print("Awesome! purple is my facorite color, and its also really cool because it can be a cool or warm color")
	else:
		print("you did not give one of the colors I asked about")

elif q1 == "cold".lower() or "cold colors".lower():
	q3 = input("What's your favorite color, Blue, Green, or Purple")
	
	if q3 == "blue".lower():
		print()
	elif q3 == "green".lower():
		print(print("Oh nice! I also like green because it can be either a cool or warm color"))
	elif q3 == "purple".lower():
		print("Awesome! purple is my facorite color, and its also really cool because it can be a cool or warm color")
	else:
		print("thats not one of the options")
