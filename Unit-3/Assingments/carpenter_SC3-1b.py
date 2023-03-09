# Nathan Carpenter
# Dec 11, 2020
# Starts with a white Background, changes to random when touched

from scene import *
import random


class MyScene (Scene):
	def setup(self):
		self.color = 'white'
		self.a = 1
		self.b = 1
		self.c = 1
		
	def update(self):
		background(self.color)
		self.color = self.a, self.b, self.c
		
		
		
	def touch_began(self, touch):
		self.a = random.randint(0,1)
		self.b = random.randint(0,1)
		self.c = random.randint(0,1)
		
husky = MyScene()
run(husky)
		
