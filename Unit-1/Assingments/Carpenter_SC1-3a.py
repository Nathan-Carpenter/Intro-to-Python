#Nathan Carpenter
#10/2/20
#when you input a word it will print out saying if the word is more than, less than, or equal to 6 letters long


def wordsize(word):
	word = word.upper()
	if len(word) > 6:
		print("%s is more than 6 letters long " %(word))
	elif len(word) < 6:
		print("%s is less than 6 letters long " %(word))
	else:
		print("%s is exactly 6 letters long" %(word))
		

