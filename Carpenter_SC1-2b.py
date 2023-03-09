#Nathan carpenter
#9-25-20
#this code asks for a vowel and a word and depending on if thw word has said vowel in it, will give one of 2 responces


import console
console.clear()

word = input("Imput a word with the letter 'a' (capital or lowercase)")
lower = word.lower()

if 'a' in lower:
	print("The letter 'a' appears in",word)
	print("There are",lower.count('a'),"'a's in",word)
		
	# I looked this part up
	target = "a"
	indices = []
	for i in range(len(lower)):
		if lower[i:i+len(target)] == target:
			indices.append(i)
	# -----------------------
	
	last = indices[lower.count('a')-1]
	print("There are",len(lower) - (last+1),"letter(s) after the last 'a'")
	
	
elif 'a' not in lower:
	print("The letter 'a' doesnt appear",word)
	

