#Nathan Carpenter
#Oct 20, 2020
#has a list with a set of specific items, asks to remove a number by name and replace it with "X" and asks to remove a number by index and adds a "Y" to the end


import console
console.clear()


#The list of items
start = ['nathan', 'carpenter', 'purple', 'thirteen', 'mango', 'kona']

print(start)

#The two inputs of name and index
itemname = input("Select a word by name to remove it ")
itemnum = input("Select a word by index to remove it ")
itemnum = int(itemnum)

#finding where the name item is
inplace = start.index(itemname)

#Making the modifications to the list
start.remove(itemname)
start.insert(inplace, "X")
start.pop(itemnum)
start.append("Y")


#printing the modified list
print(start)


