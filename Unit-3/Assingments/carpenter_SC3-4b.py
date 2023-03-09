# Nathan Carpenter
# 1/22/21
#


from scene import *
import sound
import random
import math


class Asteroids (object):
	def __init__(self):
		self.x = 100
		self.y = 300
		self.w = random.randint(10,30)
		self.h = random.randint(10,30)
		self.vx = random.randint(5,20)
		self.vy = random.randint(-10,10)
		self.grav = -7


class MyScene (Scene):
	def setup(self):
		self.launcher = Rect(1,255,150,150)
		self.fire_button = Rect(950,50,100,100)
		self.roster = []
		self.type = ['spc:MeteorGrayMed1','spc:MeteorGrayMed2','spc:MeteorGraySmall1','spc:MeteorGraySmall2','spc:MeteorGrayTiny1','spc:MeteorGrayTiny2']
		self.type2 = 0 
	
	
	def update(self):
		
		
		for each in self.roster:
			image(random.choice(self.type), each.x, each.y, each.w, each.h)
			
			each.x += each.vx
			each.y += each.vy
			each.grav += .5
			each.y -= each.grav
			
			
		image('spc:Beam7', *self.launcher)
		image('spc:MeteorGrayMed1', *self.fire_button)
		
	
	def touch_began(self, touch):
		if touch.location in self.fire_button:
			for x in range(50):
				new = Asteroids()
				self.roster.append(new)
				
				
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

stick = MyScene()
run(stick)
