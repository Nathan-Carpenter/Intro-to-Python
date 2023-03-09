#Nathan Carpenter
#re-submitting at 9/22/20
#this code takes a name and 2 numbers and then types pit a message including the name,both numbers,and the 1st number multiplies by the 2nd

import console
console.clear()

print("Hi there!")

name = input("What's your name? ")


x = int(input("What's your favorite number? "))


y = int(input("Now give a number to multiply by your favorite number "))
z = x*y

#i couldnt figure out how to have this one have to spaces, it wouldnt let me use + without an error message:
#unsupported operand type(s) for +: 'int' and 'str'
print("#"+name+"'sfavoritenumberis"+str(x)+"and"+str(x)+"times"+str(y)+"is"+str(z))

console.set_font("chalkduster", 20)
print("#%s'sfavoritenumberis%iand%itimes%iis%i" % (name,x,x,y,z) )
