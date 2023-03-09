from scene import *
import sound
import random
import math


class MyScene (Scene):
	def setup(self):
		
		self.dot = Point(540,405)
		
		self.area = Rect(100,100,200,150)
		self.area2 = Rect(200,200,100,300)
		
		self.vy = 10 #speed of 12 pixels/cycle
		self.vx = -5
		
		self.vy2 = 5
		self.vx2 = -10
		
		
		self.r = 0
		self.g = 0
		self.b = 0
		
		self.fill = 'white'
		self.fill2 = 'white'
	def update(self):
		
		fill(self.fill)
		rect(*self.area) #same as rect(self.area.x, self.area.y,...)
		fill(self.fill2)
		rect(*self.area2)
		fill('white')
		self.area.y += self.vy
		self.area.x += self.vx
		
		if self.area.y < 0 or self.area.max_y > 810:
			self.vy = self.vy * -1
		
		if self.area.x < 0 or self.area.max_x > 1080:
			self.vx = self.vx * -1
			
			
		self.area2.y += self.vy2
		self.area2.x += self.vx2
		
		if self.area2.y < 0 or self.area2.max_y > 810:
			self.vy2 = self.vy2 * -1
			
		if self.area2.x < 0 or self.area2.max_x > 1080:
			self.vx2 = self.vx2 * -1
			
			
			
			
			
		#bonus point
		self.r = random.randint(0,1)
		self.g = random.randint(0,1)
		self.b = random.randint(0,1)
		
		
		if self.area.intersects(self.area2) == True:
			overlap = self.area.intersection(self.area2)
			fill(self.r,self.g,self.b)
			rect(*overlap)
		
		
		# Point & turning pink 
		fill('red')
		ellipse(*self.dot, 20, 20)
		
		if self.dot in self.area:
			self.fill = 'pink'
		else:
			self.fill = 'white'	
			
		if self.dot in self.area2:
			self.fill2 = 'pink'
		else:
			self.fill2 = 'white'
					
	def touch_began(self, touch):
		pass
	def touch_moved(self, touch):
		pass
	def touch_ended(self, touch):
		pass
rectangles = MyScene()
run(rectangles)
