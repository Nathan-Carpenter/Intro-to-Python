# Nathan Carpenter
# 12-8-2020
# this program introduces SCENE

#imports scene without having to type "scene" each time
from scene import *
import random
import math

class Myscene (Scene):#allow me to MOD the Scene
	
	def setup(self): #runs ONCE when you hit play (starting values)
		
		self.color = 'red'
		self.x = 50
		self.v = 3
		
		
		
	def update(self): 
		#runs 60x per second AUTOMATICIALLY
		#this is the ONLY place you can draw stuff
		background('gray')
		#print(self.size)
		
		#draw a circle that fades in color
		
		#fill(math.sin(self.t), 0.45, math.cos(self.t))
		fill(1, 0, 1,)
		ellipse(self.x,375,200,200)
		
		#change the balls postiion
		self.x = self.x + self.v
		
		
		#wrap back around to other side if it goes off screen
		if self.x > 1080:
			self.x = -200
		
	def touch_began(self, touch): #runs when finger LANDS on screen
		
		self.v = self.v + 1
	





pineapple = Myscene()
run(pineapple)







