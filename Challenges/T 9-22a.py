#ask for 2 words and then
#if lemgth of a is bigger than b, etc 

a = input("Give a word ")
b = input("Give another word ")
print()


if len(a)<len(b):
	print("The word %s is longer than the word %s" %(b,a))

elif len(b)<len(a):
	print("The word %s is longer than the word %s" %(a,b))
	
else:
	print("The words %s and %s are the same length" %(a,b))

#a[1] isnhow to find the letter at value 1 of variable a

if a[2]==b[2]:
	print("The second letter of %s is %s, which is also the second letter in %s " %(a,a[2],b))

else:
	print("The second letters in %s and %s arent the same" %(a,b))
