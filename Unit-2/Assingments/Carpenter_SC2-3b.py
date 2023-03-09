#Nathan Carpenter
#Nov 5, 2020
#This code will ask for a word that starts with a vowel and as long as the word inputed does, it will add that word and then continue to ask until the word doesnt start with a vowel, and then print the list



x = []
z = 'y'
while z == 'y':
	question1 = input("Please give a word that starts with a vowel: ")
	vowels = ["a", "e", "i", "o", "u"]
	if question1[0].lower() in vowels: 
		if question1 in x:
			a = 'in'
			z = 'n'
		else:
			x.append(question1)
			z = 'y'
		
	else:
		z = 'n'
		a = 'on'
	
	
if a == 'on':
	print("Not to sure about what 'Vowel' means, are you? ")
	
if a == 'in':
	print("the word you inputed is already in the list")
	
print(x)
