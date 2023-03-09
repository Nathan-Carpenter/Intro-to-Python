#Nathan Carpenter
#Nov 3, 2020
#This code has a menu and as long as you answer 'y' to the question of woould you like to add to the menu it will continue to add the item to the menu that you input, and once you say n it will print the current menu 

import console
console.clear()

menu = {
	"Pizza": 2.99,
	"Hotdog": 1.99,
	"Taco": 1.99
}

print(menu)

ask1 = input("Would you like to add a new item to the menu? (y/n) ")

if ask1 == 'y':
	ask1 = 'y'
	while ask1 =='y':
		ask2 = input("What is the new item? ")
		ask3 = input("How much does it cost? ")
		
		menu[ask2] = ask3
		ask1 = input("Would you like to add a new item to the menu? (y/n) ")
		
print(menu)

	
