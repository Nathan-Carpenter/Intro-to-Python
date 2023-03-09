# Nathan Carpenter
# 1/22/21
# This code runs 100 objects that all bounce around the screen


from scene import *
import sound
import random
import math


class Bounce (object):
	def __init__(self):
		self.x = random.randint(1,1080)
		self.y = random.randint(1,810)
		self.w = random.randint(10,30)
		self.h = random.randint(10,30)
		self.r = random.random() 
		self.g = random.random()
		self.b = random.random()
		self.vx = random.randint(-15,15)
		self.vy = random.randint(-15,15)



class MyScene (Scene):
	def setup(self):
		self.roster = []
		self.x = 0
		
		
		for x in range(100):
			new = Bounce()
			self.roster.append(new)
		
		
	def update(self):
				
				
		for each in self.roster:
			fill(each.r, each.g, each.b)
			ellipse(each.x, each.y, each.w, each.h)
			
			
			each.x += each.vx
			each.y += each.vy
			
			
			if each.x < 1:
				each.vx *= -1
			if each.x > 1080:
				each.vx *= -1
			if each.y <1:
				each.vy *= -1
			if each.y > 810:
				each.vy *= -1
			
			
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

potato = MyScene()
run(potato)
