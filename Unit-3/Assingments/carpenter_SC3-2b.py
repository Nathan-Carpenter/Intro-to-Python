# Nathan Carpenter
# Dec 18
# In Landscape mode, This code has an orange circle that moves using ipad tilt around 2 dimentions, not going off any of the sides, and changing the widh based on the x-value. My name is also printed and changes color over time


from scene import *
import random


class MyScene (Scene):
	
	
	def setup(self):
		self.x = 500
		self.y = 400
		self.v = 8
		self.color = 'orange'
		self.W = 100
		self.W2 = 100
		self.color2 = 'lavender'
		self.r = 0
		self.g = 0
		self.b = 1
		self.clr = 1
		
		
		
		
	
	
	
	
	
	def update(self):
		fill(self.color)
		ellipse(self.x,self.y,self.W,100)
		
		self.x = self.x + -gravity().y*self.v
		self.y = self.y + gravity().x*self.v
		
		
		#dont let it go off the left edge
		if self.x < 1:
			self.x = 1
		
		
		#dont let if off the right edge
		if self.x > 780:
			self.x = 780
			
			
		#dont let it go off the bottom edge
		if self.y < 1:
			self.y = 1
			
			
		#dont let it go off the top edge
		if self.y > 710:
			self.y = 710
			
		
	
		if self.clr == 1:
			self.b = self.b - .01
			self.r = self.r + .01
			if self.r > 1:
				self.clr = 2
		
		if self.clr == 2:
			self.r = self.r - .01
			self.g = self.g + .01
			if self.g > 1:
				self.clr = 3
				
		if self.clr == 3:
			self.g = self.g - .01
			self.b = self.b + .01
			if self.b > 1:
				self.clr = 1
		
			
					
			
		self.color2 = (self.r,self.g,self.b)
		tint(self.color2)
		text('Nathan Carpenter','Helvetica-Bold', 50, 375, 700)	
		
		#change width based on x pos
		
		self.W = self.W2 + (self.x/3.9)
		#print(self.W)
		
		
		
		


basket = MyScene()
run(basket, LANDSCAPE)
