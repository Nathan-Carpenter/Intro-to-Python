from scene import *




class MyScene (Scene):
	def setup(self):
		self.x = 500
		self.y = 400
		self.v = 8
		
		
		
	def update(self):
		rect(self.x, self.y, 100, 100)
		
		
		
		self.x = self.x + -gravity().y*self.v
		self.y = self.y + gravity().x*self.v
		
		
		print(self.size)
		#dont let it go off the left edge
		if self.x < 1:
			self.x = 1
		
		
		#dont let if off the right edge
		if self.x > 980:
			self.x = 980
			
			
		#dont let it go off the bottom edge
		if self.y < 1:
			self.y = 1
			
			
		#dont let it go off the top edge
		if self.y > 710:
			self.y = 710
											

xlp = MyScene()
run(xlp, LANDSCAPE)
