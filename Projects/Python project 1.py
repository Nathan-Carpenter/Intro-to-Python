#Nathan Carpenter
#started 10/11/2020


import console
console.clear()


#This is the function that is my project
def inktober(): 
	
	areink = input("Are you participating in inktober? (yes/no) ")
	
	if areink == "yes": #If the user is going to use the purpose of the function
		drawdone = input("Nice! How many drawings have you done so far?")
		drawdone = int(drawdone)
		
		daysdone = input("What Day of inktober is it? ")
		daysdone = int(daysdone)
		
		#Daysdone and drawdone are the drawings done so far (out of 31) and current day of october it is
		
		daysleft = 31 - daysdone
		drawleft = 31 - drawdone
		#drawleft and daysleft are 
		daysleft = int(daysleft)
		drawleft = int(drawleft)
		
		dpday = drawleft/daysleft
		dpday = str(dpday)
		
		 
		print("Nice! If its day %i of inktober and you have %i drawings done, you have %i drawings left to do, which means drawing %s drawings per day to finish before the end of october" %(daysdone,drawdone,drawleft,dpday)) 
	
	elif areink == "no": #If the user is not going to be using the purpose of this function
		ask2 = input("Alright, but it would be a lot of fun, would you want to do it next year? (yes/no) ")
		
		if ask2 == "yes":
			print("Nice! Its really fun to do")
			
		elif ask2 == "no":
			print("Alright")
		
		else:
			print("You did not input a y(for yes) or a n(for no)")
	
	else:
		print("You did not input a y(for yes) or a n(for no)")
		
