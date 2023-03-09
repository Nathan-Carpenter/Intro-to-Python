# Nathan Carpenter
# Dec 8
# Draws an orange square when and where touched, turns yellow and follows when finger moves, turns purple when the finger stops touching


from scene import *
import random
import math



class Myscene (Scene):
	
	
	def setup(self):
		self.color = .2, .2, .2
		self.backcolor = .2, .2, .2, 
		self.a = 400
		self.b = 400
		self.c = 100
		self.d = 100
		
	
	
	
	
	
	def update(self):
		background(self.backcolor)
		
		
		
		
		fill(self.color)
		rect(self.a, self.b, self.c, self.d)
		
		
		
		
	def touch_began(self, touch):
		self.color = 'orange'
		x, y = touch.location
		self.a = x - 50
		self.b = y - 50
		
		
		
		
	def touch_moved(self, touch):
		self.color = 'yellow'
		x, y = touch.location
		self.a = x - 50
		self.b = y - 50
		
		
		
		
		
	def touch_ended(self, touch):
		self.color= 'purple'
	

runsquare = Myscene()
run(runsquare)
