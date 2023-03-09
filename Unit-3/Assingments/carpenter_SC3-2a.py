# Nathan Carpenter
# Dec 18
# In portrait mode, this code moves a red elipse in 2 dimentions via ipad tilt. The ellipse cant go off of the bottom edge. If the ellipse goes off of the left side it wraps around from the right, changing to a random color. If the ellips goes off of the top, you get a little supprise, that either ends after 2 sec, or when yu touch the screen

from scene import *
import random

class MyScene (Scene):
	
	def setup(self):
		self.x = 355
		self.y = 490
		self.v = 8
		self.color = 'red'
		self.r = 1
		self.g = 0
		self.b = 0
		self.bonus = 0
		self.blength = 0
	
	def update(self):
		fill(self.color)
		ellipse(self.x,self.y,100,100)
		
		
		self.x = self.x + gravity().x*self.v
		self.y = self.y + gravity().y*self.v
		
		
		if self.y < 1:
			self.y = 1
			
		if self.x < -105:
			self.x = 815
			
			self.r = random.randint(0,1)
			self.g = random.randint(0,1)
			self.b = random.randint(0,1)
			
			
			self.color = (self.r, self.g, self.b)
			
			 
		tint('lavender')
		text('Nathan Carpenter','Helvetica-Bold', 50, 375, 700)
		
		
		#My fun little suprise :)
		
		
		#when you go over the top you go to the middle and flash until
		#you touch the screen
		
	
		if self.y > 1080:
			self.y = 490
			self.bonus = 1
			self.blength = 120
			
		if self.bonus == 1:	
			self.r = random.randint(0,1)
			self.b = random.randint(0,1)
			self.g = random.randint(0,1)
			
			self.color = (self.r, self.g, self.b)
			self.blength = self.blength - 1
			
			if self.blength == 0:
				self.bonus = 0
						
	def touch_began(self, touch):
		self.bonus = 0		
		self.color = 'red'
		
			
potato = MyScene()
run(potato, PORTRAIT)
