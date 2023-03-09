import console
console.clear()

from scene import *

class MyScene (Scene):
	
	def setup(self):
		#initial positions of objects
		self.x1 = 200
		self.y1 = 100
		self.x2 = 400
		self.y2 = 100
		
		
	def update(self):
		#draw and move first object
		image('spc:LaserBlue10', self.x1, self.y1, 20,100)
		self.y1 = self.y1 + 5
		#handle wrapping for first object
		if self.y1 > self.size.h:
			self.y1 = -125
			
		#draw and move second object
		image('spc:LaserRed10', self.x2, self.y2, 20,100)
		self.y2 = self.y2 + 6
		#handle wrapping for first object
		if self.y2 > self.size.h:
			self.y2 = -125		
		
		
george = MyScene()
run(george)
