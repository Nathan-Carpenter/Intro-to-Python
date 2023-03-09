# Nathan Carpenter
# Dec 3rd, 2020
# For my project I will be doing 'mega tic tac toe'

import canvas
import console
console.clear()
canvas.clear()


# All of the positions for the game board


gamespaces = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4']
row1 = ['a1', 'b1', 'c1', 'd1']
row2 = ['a2', 'b2', 'c2', 'd2']
row3 = ['a3', 'b3', 'c3', 'd3']
row4 = ['a4', 'b4', 'c4', 'd4']
lineA = ['a1', 'a2', 'a3', 'a4']
lineB = ['b1', 'b2', 'b3', 'b4']
lineC = ['c1', 'c2', 'c3', 'c4']
lineD = ['d1', 'd2', 'd3', 'd4']

#--------- Allowing players to pick their color and name

fnt = 'Helvetica-Bold'
s = 20
canvas.set_fill_color( 1, 1, 1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

canvas.draw_text("Player 1, what is your name?", 0, 380, fnt, s)
name1 = input("player 1 name")
canvas.clear()

canvas.draw_text("Player 1, what color would you like to be:", 0, 380, fnt, s)
canvas.draw_text("red, orange, yellow, green, blue, purple, or pink", 0, 360, fnt, s)
clr1 = input("question 1")

while clr1 not in colors:
	canvas.clear()
	canvas.draw_text("Player 1, you did not input one of the avalible colors,", 0, 380, fnt, s)
	canvas.draw_text("please try again", 0, 360, fnt, s)
	canvas.draw_text("(red, orange, yellow, green, blue, purple, pink)", 0, 340, fnt, s)
	clr1 = input("question 1 wrong, try again")

if clr1 == 'red':
	def p1color():
		canvas.set_fill_color(1, .1, .1)
elif clr1 == 'orange':
	def p1color():
		canvas.set_fill_color(1, .5, .1)
elif clr1 == 'yellow':
	def p1color():
		canvas.set_fill_color(1, 1, .1)
elif clr1 == 'green':
	def p1color():
		canvas.set_fill_color(.1, 1, .3)
elif clr1 == 'blue':
	def p1color():
		canvas.set_fill_color(.1, .1, 1)
elif clr1 == 'purple':
	def p1color():
		canvas.set_fill_color(.7, .1, 1)
elif clr1 == 'pink':
	def p1color():
		canvas.set_fill_color(1, .5, 1)

canvas.clear()

canvas.draw_text("Player 2, what is your name?", 0, 380, fnt, s)
name2 = input("Player 2 name")
canvas.clear()

canvas.draw_text("Player 2, what color would you like to be:", 0, 380, fnt, s)
canvas.draw_text("red, orange, yellow, green, blue, purple, or pink", 0, 360, fnt, s)
clr2 = input("question 2")

while clr2 not in colors:
	canvas.clear()
	canvas.draw_text("Player 2, you did not input one of the avalible colors,", 0, 380, fnt, s)
	canvas.draw_text("please try again", 0, 360, fnt, s)
	canvas.draw_text("(red, orange, yellow, green, blue, purple, pink)", 0, 340, fnt, s)
	clr2 = input("question 1 wrong, try again")

while clr2 == clr1:
	canvas.clear()
	canvas.draw_text("You cant pick the same color as player 1, try again", 0, 340, fnt, s)
	clr2 = input("question 2 cant = question 1")


if clr2 == 'red':
	def p2color():
		canvas.set_fill_color(1, .1, .1)
elif clr2 == 'orange':
	def p2color():
		canvas.set_fill_color(1, .5, .1)
elif clr2 == 'yellow':
	def p2color():
		canvas.set_fill_color(1, 1, .1)
elif clr2 == 'green':
	def p2color():
		canvas.set_fill_color(.1, 1, .3)
elif clr2 == 'blue':
	def p2color():
		canvas.set_fill_color(.1, .1, 1)
elif clr2 == 'purple':
	def p2color():
		canvas.set_fill_color(.7, .1, 1)
elif clr2 == 'pink':
	def p2color():
		canvas.set_fill_color(1, .5, 1)


canvas.clear()


####------This begins the game board


def gameboard():
	canvas.set_fill_color(1, 1, 1)
	canvas.set_line_width(10)
	canvas.set_stroke_color(1, 1, 1)
	canvas.draw_line(100, 380, 100, 0)
	canvas.draw_line(200, 380, 200, 0)
	canvas.draw_line(300, 380, 300, 0)
	canvas.draw_line(0, 200, 400, 200)
	canvas.draw_line(0, 100, 400, 100)
	canvas.draw_line(0, 300, 400, 300)
	canvas.draw_text('a', 35, 400, fnt, s)
	canvas.draw_text('b', 140, 400, fnt, s)
	canvas.draw_text('c', 240, 400, fnt, s)
	canvas.draw_text('d', 340, 400, fnt, s)
	canvas.draw_text('1', 420, 360, fnt, s)
	canvas.draw_text('2', 420, 240, fnt, s)
	canvas.draw_text('3', 420, 140, fnt, s)
	canvas.draw_text('4', 420, 40, fnt, s)


canvas.draw_text('This is essentially just tic tac toe, but larger. The way', 0, 400, fnt, s)
canvas.draw_text('to play is on your turn, select a square by coordinate,', 0, 370, fnt, s)
canvas.draw_text('and when your name lights up, it is your turn', 0, 340, fnt, s)
canvas.draw_text("like a4, b1, etc. Type (y) when you understand", 0, 310, fnt, s)

startquestion = input("question 3")

while not startquestion == 'y':
	canvas.draw_text("you did not type (y), please type (y) to continue", 0, 280, fnt, s)
	startquestion = input("question 3 wrong, try again")
	
canvas.clear()

canvas.draw_text('The goal is to get 3 slots in a row, either in a straight', 0, 400, fnt, s)
canvas.draw_text('line or diagonally, or get a square of 2x2. Keep in mind', 0, 370, fnt, s)
canvas.draw_text('that the game will only end once both players go', 0, 340, fnt, s)
canvas.draw_text('Type (y) when you understand', 0, 310, fnt, s)
startquestion2 = input('second info page')

while not startquestion2 == 'y':
	canvas.draw_text("you did not type (y), please type (y) to continue", 0, 280, fnt, s)
	startquestion = input("second info wrong, try again")



canvas.clear()





gameboard()

def p1name():
	canvas.draw_text( name1, 75, 450, fnt, s)
def p2name():
	canvas.draw_text( name2, 275, 450, fnt, s)
#-------------------------------------------------------Turn functions

def a1():
	canvas.draw_text('X', 50, 350, fnt, s)
def b1():
	canvas.draw_text('X', 150, 350, fnt, s)
def c1():
	canvas.draw_text('X', 250, 350, fnt, s)
def d1():
	canvas.draw_text('X', 350, 350, fnt, s)
def a2():
	canvas.draw_text('X', 50, 250, fnt, s)
def b2():
	canvas.draw_text('X', 150, 250, fnt, s)
def c2():
	canvas.draw_text('X', 250, 250, fnt, s)
def d2():
	canvas.draw_text('X', 350, 250, fnt, s)
def a3():
	canvas.draw_text('X', 50, 150, fnt, s)
def b3():
	canvas.draw_text('X', 150, 150, fnt, s)
def c3():
	canvas.draw_text('X', 250, 150, fnt, s)
def d3():
	canvas.draw_text('X', 350, 150, fnt, s)
def a4():
	canvas.draw_text('X', 50, 50, fnt, s)
def b4():
	canvas.draw_text('X', 150, 50, fnt, s)
def c4():
	canvas.draw_text('X', 250, 50, fnt, s)
def d4():
	canvas.draw_text('X', 350, 50, fnt, s)


p1slots = []
p2slots = []


#---------------------------------------------------------Player 1's turn
def turn1():
	p1color()
	p1name()
	
	go1 = input('player1 turn')
	while not go1 in gamespaces:
		go1 = input('player 1 turn invalid, try again')
	while go1 in p1slots:
		go1 = input('player 1 turn invalid, try again')
	if go1 == 'a1':	
		a1()
		p1slots.append('a1')
	elif go1 == 'a2':
		a2()
		p1slots.append('a2')
	elif go1 == 'a3':
		a3()
		p1slots.append('a3')
	elif go1 == 'a4':
		a4()
		p1slots.append('a4')
	elif go1 == 'b1':
		b1()
		p1slots.append('b1')
	elif go1 == 'b2':
		b2()
		p1slots.append('b2')
	elif go1 == 'b3':
		b3()
		p1slots.append('b3')
	elif go1 == 'b4':
		b4()
		p1slots.append('b4')
	elif go1 == 'c1':
		c1()
		p1slots.append('c1')
	elif go1 == 'c2':
		c2()
		p1slots.append('c2')
	elif go1 == 'c3':
		c3()
		p1slots.append('c3')
	elif go1 == 'c4':
		c4()
		p1slots.append('c4')
	elif go1 == 'd1':
		d1()
		p1slots.append('d1')
	elif go1 == 'd2':
		d2()
		p1slots.append('d2')
	elif go1 == 'd3':
		d3()
		p1slots.append('d3')
	elif go1 == 'd4':
		d4()
		p1slots.append('d4')			


#---------------------------------------------------------Player 2's turn	
def turn2():
	p2color()
	p2name()
	
	go2 = input('player2 turn')
	while not go2 in gamespaces:
		go2 = input('player 2 turn invalid, try again')
	while go2 in p2slots:
		go2 = input('player 2 turn invalid, try again')
	if go2 == 'a1':	
		a1()
		p2slots.append('a1')
	elif go2 == 'a2':
		a2()
		p2slots.append('a2')
	elif go2 == 'a3':
		a3()
		p2slots.append('a3')
	elif go2 == 'a4':
		a4()
		p2slots.append('a4')
	elif go2 == 'b1':
		b1()
		p2slots.append('b1')
	elif go2 == 'b2':
		b2()
		p2slots.append('b2')
	elif go2 == 'b3':
		b3()
		p2slots.append('b3')
	elif go2 == 'b4':
		b4()
		p2slots.append('b4')
	elif go2 == 'c1':
		c1()
		p2slots.append('c1')
	elif go2 == 'c2':
		c2()
		p2slots.append('c2')
	elif go2 == 'c3':
		c3()
		p2slots.append('c3')
	elif go2 == 'c4':
		c4()
		p2slots.append('c4')
	elif go2 == 'd1':
		d1()
		p2slots.append('d1')
	elif go2 == 'd2':
		d2()
		p2slots.append('d2')
	elif go2 == 'd3':
		d3()
		p2slots.append('d3')
	elif go2 == 'd4':
		d4()
		p2slots.append('d4')
	

def resetname():
	canvas.set_fill_color(1, 1, 1)
	canvas.fill_rect(30, 435, 350, 50)

#--------------------------------------a function for who wins the game	
def winconditions1():
	canvas.set_fill_color(1, 1, 1)
	
	
	if len(p1slots) > 2:
		
		if 'a1' in p1slots:
			if 'a2' in p1slots:
				if 'a3' in p1slots:
					win.append('player1')
					print('1')
		if 'a2' in p1slots:
			if 'a3' in p1slots:
				if 'a4' in p1slots:
					win.append('player1')
					print('2')
		if 'b1' in p1slots:
			if 'b2' in p1slots:
				if 'b3' in p1slots:
					win.append('player1')
					print('3')
		if 'b2' in p1slots:
			if 'b3' in p1slots:
				if 'b4' in p1slots:
					win.append('player1')
					print('4')
		if 'c1' in p1slots:
			if 'c2' in p1slots:
				if 'c4' in p1slots:
					win.append('player1') 			
					print('5')
		if 'c2' in p1slots:
			if 'c3' in p1slots:
				if 'c4' in p1slots:
					win.append('player1')
					print('6')
		if 'd1' in p1slots:
			if 'd2' in p1slots:
				if 'd3' in p1slots:
					win.append('player1')
					print('7')
		if 'd2' in p1slots:
			if 'd3' in p1slots:
				if 'd4' in p1slots:
					win.append('player1')
					print('8')
		if 'a1' in p1slots:
			if 'b1' in p1slots:
				if 'c1' in p1slots:
					win.append('player1')
					print('9')
		if 'b1' in p1slots:
			if 'c1' in p1slots:
				if 'd1' in p1slots:
					win.append('player1')
					print('10')		
		if 'a2' in p1slots:
			if 'b2' in p1slots:
				if 'c2' in p1slots:
					win.append('player1')
					print('11')
		if 'b2' in p1slots:
			if 'c2' in p1slots:
				if 'd2' in p1slots:
					win.append('player1')
					print('12')
		if 'a3' in p1slots:
			if 'b3' in p1slots:
				if 'c3' in p1slots:
					win.append('player1')
					print('13')
		if 'b3' in p1slots:
			if 'c3' in p1slots:
				if 'd3' in p1slots:
					win.append('player1')
					print('14')
		if 'a4' in p1slots:
			if 'b4' in p1slots:
				if 'c3' in p1slots:
					win.append('player1')
					print('15')
		if 'b4' in p1slots:
			if 'c4' in p1slots:
				if 'd4' in p1slots:
					win.append('player1')
					print('16')
		#---------------------------diagonals
		
		if 'a1' in p1slots:
			if 'b2' in p1slots:
				if 'c3' in p1slots:
					win.append('player1')
		if 'b2' in p1slots:
			if 'c3' in p1slots:
				if 'd4' in p1slots:
					win.append('player1')
		if 'b1' in p1slots:
			if 'c2' in p1slots:
				if 'd3' in p1slots:
					win.append('player1')
		if 'a2' in p1slots:
			if 'b3' in p1slots:
				if 'c4' in p1slots:
					win.append('player1')
		if 'd1' in p1slots:
			if 'c2' in p1slots:
				if 'b3' in p1slots:
					win.append('player1')
		if 'c2' in p1slots:
			if 'b3' in p1slots:
				if 'a4' in p1slots:
					win.append('player1')
		if 'c1' in p1slots:
			if 'b2' in p1slots:
				if 'a3' in p1slots:
					win.append('player1')
		if 'd2' in p1slots:
			if 'c3' in p1slots:
				if 'b4' in p1slots:
					win.append('player1')
		#-----------------------------2x2 square
		
		if 'a1' in p1slots:
			if 'a2' in p1slots:
				if 'b1' in p1slots:
					if 'b2' in p1slots:
						win.append('player1')
		if 'a2' in p1slots:
			if 'a3' in p1slots:
				if 'b2' in p1slots:
					if 'b3' in p1slots:
						win.append('player1')
		if 'a3' in p1slots:
			if 'a4' in p1slots:
				if 'b3' in p1slots:
					if 'b4' in p1slots:
						win.append('player1')		
		if 'b1' in p1slots:
			if 'b2' in p1slots:
				if 'c1' in p1slots:
					if 'c2' in p1slots:
						win.append('player1')
		if 'b2' in p1slots:
			if 'b3' in p1slots:
				if 'c2' in p1slots:
					if 'c3' in p1slots:
						win.append('player1')
		if 'b3' in p1slots:
			if 'b4' in p1slots:
				if 'c3' in p1slots:
					if 'c4' in p1slots:
						win.append('player1')
		if 'c1' in p1slots:
			if 'c2' in p1slots:
				if 'd1' in p1slots:
					if 'd2' in p1slots:
						win.append('player1')
		if 'c2' in p1slots:
			if 'c3' in p1slots:
				if 'd2' in p1slots:
					if 'd3' in p1slots:
						win.append('player1')
		if 'c3' in p1slots:
			if 'c4' in p1slots:
				if 'd3' in p1slots:
					if 'd4' in p1slots:
						win.append('player1')
		
		
		
		
		
		
def winconditions2():
	canvas.set_fill_color(1, 1, 1)
	
	if len(p2slots) > 2:
		
		if 'a1' in p2slots:
			if 'a2' in p2slots:
				if 'a3' in p2slots:
					win.append('player2')
					print('1')
		if 'a2' in p2slots:
			if 'a3' in p2slots:
				if 'a4' in p2slots:
					win.append('player2')
					print('2')
		if 'b1' in p2slots:
			if 'b2' in p2slots:
				if 'b3' in p2slots:
					win.append('player2')
					print('3')
		if 'b2' in p2slots:
			if 'b3' in p2slots:
				if 'b4' in p2slots:
					win.append('player2')
					print('4')
		if 'c1' in p2slots:
			if 'c2' in p2slots:
				if 'c4' in p2slots:
					win.append('player2') 			
					print('5')
		if 'c2' in p2slots:
			if 'c3' in p2slots:
				if 'c4' in p2slots:
					win.append('player2')
					print('6')
		if 'd1' in p2slots:
			if 'd2' in p2slots:
				if 'd3' in p2slots:
					win.append('player2')
					print('7')
		if 'd2' in p2slots:
			if 'd3' in p2slots:
				if 'd4' in p2slots:
					win.append('player2')
					print('8')
		if 'a1' in p2slots:
			if 'b1' in p2slots:
				if 'c1' in p2slots:
					win.append('player2')
					print('9')
		if 'b1' in p2slots:
			if 'c1' in p2slots:
				if 'd1' in p2slots:
					win.append('player2')
					print('10')		
		if 'a2' in p2slots:
			if 'b2' in p2slots:
				if 'c2' in p2slots:
					win.append('player2')
					print('11')
		if 'b2' in p2slots:
			if 'c2' in p2slots:
				if 'd2' in p2slots:
					win.append('player2')
					print('12')
		if 'a3' in p2slots:
			if 'b3' in p2slots:
				if 'c3' in p2slots:
					win.append('player2')
					print('13')
		if 'b3' in p2slots:
			if 'c3' in p2slots:
				if 'd3' in p2slots:
					win.append('player2')
					print('14')
		if 'a4' in p2slots:
			if 'b4' in p2slots:
				if 'c3' in p2slots:
					win.append('player2')
					print('15')
		if 'b4' in p2slots:
			if 'c4' in p2slots:
				if 'd4' in p2slots:
					win.append('player2')
					print('16')
	#---------------------------diagonals
		
		if 'a1' in p2slots:
			if 'b2' in p2slots:
				if 'c3' in p2slots:
					win.append('player2')
		if 'b2' in p2slots:
			if 'c3' in p2slots:
				if 'd4' in p2slots:
					win.append('player2')
		if 'b1' in p2slots:
			if 'c2' in p2slots:
				if 'd3' in p2slots:
					win.append('player2')
		if 'a2' in p2slots:
			if 'b3' in p2slots:
				if 'c4' in p2slots:
					win.append('player2')
		if 'd1' in p2slots:
			if 'c2' in p2slots:
				if 'b3' in p2slots:
					win.append('player2')
		if 'c2' in p2slots:
			if 'b3' in p2slots:
				if 'a4' in p2slots:
					win.append('player2')
		if 'c1' in p2slots:
			if 'b2' in p2slots:
				if 'a3' in p2slots:
					win.append('player2')
		if 'd2' in p2slots:
			if 'c3' in p2slots:
				if 'b4' in p2slots:
					win.append('player2')
		#-----------------------------2x2 square
		
		if 'a1' in p2slots:
			if 'a2' in p2slots:
				if 'b1' in p2slots:
					if 'b2' in p2slots:
						win.append('player2')
		if 'a2' in p2slots:
			if 'a3' in p2slots:
				if 'b2' in p2slots:
					if 'b3' in p2slots:
						win.append('player2')
		if 'a3' in p2slots:
			if 'a4' in p2slots:
				if 'b3' in p2slots:
					if 'b4' in p2slots:
						win.append('player2')		
		if 'b1' in p2slots:
			if 'b2' in p2slots:
				if 'c1' in p2slots:
					if 'c2' in p2slots:
						win.append('player2')
		if 'b2' in p2slots:
			if 'b3' in p2slots:
				if 'c2' in p2slots:
					if 'c3' in p2slots:
						win.append('player2')
		if 'b3' in p2slots:
			if 'b4' in p2slots:
				if 'c3' in p2slots:
					if 'c4' in p2slots:
						win.append('player2')
		if 'c1' in p2slots:
			if 'c2' in p2slots:
				if 'd1' in p2slots:
					if 'd2' in p2slots:
						win.append('player2')
		if 'c2' in p2slots:
			if 'c3' in p2slots:
				if 'd2' in p2slots:
					if 'd3' in p2slots:
						win.append('player2')
		if 'c3' in p2slots:
			if 'c4' in p2slots:
				if 'd3' in p2slots:
					if 'd4' in p2slots:
						win.append('player2')
					
		


#---starting the game itself

resetname()
gamewin = 'no'
win = []
while gamewin == 'no':
	turn1()
	winconditions1()
	if 'player1' in win:
			if not 'player2' in win:
				gamewin = 'player1'
			elif 'player2' in win:
				gamewin = 'tie1'
	elif 'player2' in win:
			if not 'player1' in win:
				gamewin = 'player2'
			elif 'player1' in win:
				gamewin = 'tie2'
	else:
			win = []
			gamewin = 'no'
	
	resetname()
	turn2()
	winconditions2()
	resetname()
	if gamewin == 'no':
		if 'player1' in win:
			if not 'player2' in win:
				gamewin = 'player1'
			elif 'player2' in win:
				gamewin = 'tie1'
		elif 'player2' in win:
			if not 'player1' in win:
				gamewin = 'player2'
			elif 'player1' in win:
				gamewin = 'tie2'
		else:
			win = []
			gamewin = 'no'
	
	
	
canvas.clear()

if gamewin == 'player1':
	wintext = 'congradulations '+name1+', you won!'
	canvas.draw_text(wintext, 0, 400, fnt, s)
if gamewin == 'player2':
	wintext = 'congradulations '+name2+', you won!'
	canvas.draw_text(wintext, 0, 400, fnt, s)	
		
