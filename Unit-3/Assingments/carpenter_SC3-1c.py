# Nathan Carpenter
# Dec 11, 2020
# A 'control' panel in the corner with 3 different color swatches. The background starts beige, and turns whatever color swatch you press

from scene import *



class MyScene (Scene):
	def setup(self):
		self.color = 'beige'
		self.button1 = 0
		self.button2 = 0
		self.button3 = 0
		
		
		
	def update(self):
		background(self.color)
		fill('black')
		rect(0,0,320,120)
		fill('red')
		rect(1,1,100,100)
		fill('green')
		rect(101,1,100,100)
		fill('blue')
		rect(202,1,100,100)
		
		
		
		
		
		
		
		
	def touch_began(self, touch):
		if touch.location.y > 0 and touch.location.y < 100:
			if touch.location.x > 0 and touch.location.x < 101:
				self.color = 'red'
			elif touch.location.x > 101 and touch.location.x < 202:
				self.color = 'green'
			elif touch.location.x > 202 and touch.location.x < 303:
				self.color = 'blue'
			
		
		
		
		
		
		
bananna = MyScene()
run(bananna)
