#Nathan Carpenter
#re-submitting at 9/22/20
#this code asks for a word and 2 numbers, and the. gives the letter at each of those positions and the letters between the 2 positions.


import console
console.clear()


word = input("Input a word ")

n1 = int(input("Now input a number "))
if n1 > len(word):
	print(word,"doesn't have",len(word),"letters in it")
	n1 = int(input("Input a number that fits "))
else:
	pass
n2 = int(input("Now another number "))
if n2 > len(word):
	print(word,"doesn't have",len(word),"letters in it")
	n2 = int(input("Input a number that fits "))
else:
	pass	
word = word.upper()

print(word)

word = word.lower()

print("the letter in postion",n1,"is '"+word[n1]+"' and the letter in position",n2,"is '"+word[n2]+"'. In between them is '"+word[n1+1: n2]+"'")




