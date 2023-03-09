#Nathan Carpenter
#Oct 20
#The code asks for 4 words and then adds any words that arent in the list to it, and any that are in it to a seperate list

import console
console.clear()

x = ['watermelon', 'book', 'pencil', 'measure', 'trees', 'computer']

y = []

print("The current list is")
print(x)

w1 = input("Please insert a word (1/4)")

w2 = input("Please insert a word (2/4)")

w3 = input("Please insert a word (3/4)")

w4 = input("Please insert a word (4/4)")


if w1.lower() in x:
	y.append(w1)
else:
	x.append(w1)
	
if w2.lower() in x:
	y.append(w2)
else:
	x.append(w2)
	
if w3.lower() in x:
	y.append(w3)
else:
	x.append(w3)
	
if w4.lower() in x:
	y.append(w4)
else:
	x.append(w4)
	

x.sort()
z = len(y)
	
print("Your list in alphabetical order is", x)
print("There are %s words in list Y" %(z))
