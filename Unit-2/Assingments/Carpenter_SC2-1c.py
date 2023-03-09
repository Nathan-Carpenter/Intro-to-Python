#Nathan Carpenter
#Oct 20
#The code asks for a number and says what position it is in the list, then the ammount of numbers in the list, the biggest and smallest number in the list, and the average and most common number in the list

import console
console.clear()

x = [1, 85, 12, 5, 2, 4, 21, 8, 12, 54, 12, 85, 12, 5, 12, 45, 12, 9, 1, 5, 2, 8, 1, 89, 21, 84, 21, 8, 21, 5, 2, 4, 1, 45, 2, 1, 8, 2, 84, 12, 8, 15, 8, 21, 45, 21, 86, 12, 8, 12, 85, 12, 98, 7, 3, 87, 21, 45, 1, 64, 12, 7, 21, 84, 2, 748, 1, 45, 1, 6, 84, 31, 4, 12, 83, 51, 58441, 7, 12, 8, 5, 12, 81, 2, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 4, 45, 897, 32, 897, 12, 8, 12, 8, 12, 12, 1, 45, 69, 42, 0, 8, 4, 6, 2, 5, 89, 46, 32, 67, 84, 45]

y = input("Please input a number ")
y = int(y)


if y in x:
	
	z = x.index(y)
	a = x.count(y)
	print("The first time your nuber appears in the list is in position %s and it appears a total of %i times." %(z, a))

else:
	print("Your number was not in the list.")


b = len(x)
b = int(b)

c = min(x)
c = int(c)

d = max(x)
d = int(d)

e = sum(x)
e = int(e)

f = e/b


def freq(x):
	return max(set(x), key = x.count)
	
g = freq(x)
g = int(g)

print("There are a total of %i numbers in the list, of which %i is the largest and %i is the smallest." %(b, d, c))
print("The average of all the numbers in the list is %s which is %s rounded, and the most common number is %i." %(f, int(f), g))




