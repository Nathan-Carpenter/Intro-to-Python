#Nathan Carpenter
#9/22/20
#this code asks for an age and then depending on such, gives back one of 3 messages 

import console
console.clear()

age = int(input("Hi! How old are you? "))

if age < 11:
	print("wow you're pretty young")
	
elif age < 20:
	
	print("you're a teenager ")
	
else:
	print("hello there, adult")
