#Nathan Carpenter
#Nov 10
#This code asks for 7 words using a for loop, and then prints back each word, how long that word is, and how many uppercase letters are in that word


import console
console.clear()

print("Im going to ask you for 7 words. ")

assingmentlist = []


for x in range(7):
	add = input("Please input a word: ")
	assingmentlist.append(add)
	
for y in assingmentlist:
	uppercase = sum(1 for c in y if c.isupper())
	print("the word '%s' has %i letters (and %i of them are capitalized)" %(y, int(len(y)), uppercase))
