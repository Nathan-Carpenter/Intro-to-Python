#Nathan Carpenter
#Nov 5, 2020
#This code asks you to guess a random number between 1 and 20 and will repeat asking until you guess the right number

import console
console.clear()

imp1 = input("Guess which number i'm thinking of (1-20) ")
import random
for x in range(1):
	rand = random.randint(1,20)
	
imp1 = int(imp1)
while not imp1 == rand:
	imp1 = int(imp1)
	if imp1 > rand:
		imp1 = input("That was too high! Try again: ") 
	elif imp1 < rand:
		imp1 = input("That was too low! Try again: ")
print("Nice job! %i was the number I was thinking of!" %(rand))
