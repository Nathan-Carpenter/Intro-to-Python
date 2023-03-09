from scene import *
import sound
import random
import math

class MyScene (Scene):
	def setup(self):
		# My dot
		self.dot = Point(500,400) #close to middle of th screen
	
		# The area of intrest
		self.area = Rect(100,100,100,100)
		
		
		self.vy = 12 #speed of 12 pixels/cycle
		self.vx = -5
	
	def update(self):
		
		# Draw the area
		rect(*self.area) #same as rect(self.area.x, self.area.y,...)
		
		self.area.y += self.vy
		self.area.x += self.vx
		
		if self.area.y < 0 or self.area.max_y > 810:
			self.vy = self.vy * -1
		
		if self.area.x < 0 or self.area.max_x > 1080:
			self.vx = self.vx * -1
		
		
		# Draw dot
		#image('spc:PowerupYellowStar', self.dot.x, self.dot.y, 20, 20)
		
		"""# Move Dot
		self.dot.x = self.dot.x + -10*gravity().y
		self.dot.y = self.dot.y + 10*gravity().x
		
		# Test if it is in the box, it gets taller if it is
		if self.dot in self.area:
			self.area.h += 2 ##same as area.h = area.h + 2"""
		
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

game = MyScene()
run(game)
