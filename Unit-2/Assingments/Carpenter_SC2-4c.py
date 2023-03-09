#Nathan Carpenter
#Nov 13, 2020
#This code asks for at least 3 suits and at least 6 numbers and then makes every possible card with that, and then shuffles the cards and prints them

import console
import random
console.clear()

suits = input("Please type AT LEAST three suits (seperated by spaces) ")
snum = len(suits.split())
while snum < 3:
	suits = input("I said AT LEAST THREE suits (seperated by spaces) ")
	snum = len(suits.split())

numbers = input("Please type AT LEAST six numbers (seperated by spaces) ")
num = len(numbers.split())
while num < 6:
	numbers = input("I said AT LEAST SIX numbers (seperated by spaces) ")
	num = len(numbers.split())
	
suitlist = suits.split()
numlist = numbers.split()

cards = []

for x in suitlist:
	for y in numlist:
		
		cards.append('%s of %s' %(y, x))

cards2 = cards
deck = random.shuffle(cards2)
print(cards)
