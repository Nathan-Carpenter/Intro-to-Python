import console
console.clear()

x = input("Give a single character")

if x in 'AEIOU':
	print("%s is an upper case vowel" %(x))

elif x in 'bcdfghjklmnpqrstvwxz'.upper():
	print("%s is an upper case consonant" %(x))

elif x in 'aeiou':
	print("%s is a lower case vowel")
	
elif x in 'bcdfghjklmnpqrstvwxz':
	print("%s is a lower case consonant" %(x))
	
elif x is ' ':
	print("%s is a space" %(x))
	
elif x in '1234567890':
	print("%s a number" %(x))
	
else:
	print("%s must be a puncuation mark" %(x))
