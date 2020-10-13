import pygame
import constants as cons

class Shape1:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.pos = 0
		self.color = (255, 0, 0)
		self.states = [[[0, 0, 0, 0],
						[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
					],
		]

	def draw(self, drawer):
		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):
					drawer(self.x - 1 + j, self.y - 2 + i, cons.WHITE, self.color)
	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def add_x(self, value):
		self.x += value

	def add_y(self, value):
		self.y += value
	
	def get_active_blocks(self):
		ret = {}

		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):
					key = (self.x - 1 + j, self.y - 2 + i)
					ret[key] = 1

		return ret
	
	def add_active_blocks(self, struct):
		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):
					key = (self.x - 1 + j, self.y - 2 + i)
					struct[key] = 1

class Shape2(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.states = [[[0, 0, 0, 0],
						[0, 0, 0, 0],
						[1, 1, 1, 1],
						[0, 0, 0, 0],
					], [[0, 1, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[1, 1, 1, 1],
						[0, 0, 0, 0],
					], [[0, 1, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
					],
		]

class Shape3(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.states = [[[0, 0, 0, 0],
						[1, 0, 0, 0],
						[1, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[1, 1, 1, 0],
						[0, 0, 1, 0],
					], [[0, 0, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
						[1, 1, 0, 0],
					],
		]

class Shape4(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.states = [[[0, 0, 0, 0],
						[0, 0, 1, 0],
						[1, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 1, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[1, 1, 1, 0],
						[1, 0, 0, 0],
					], [[0, 0, 0, 0],
						[1, 1, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 0, 0],
					],
		]

class Shape5(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.states = [[[0, 0, 0, 0],
						[0, 1, 1, 0],
						[1, 1, 0, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 1, 0],
						[0, 0, 1, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[0, 1, 1, 0],
						[1, 1, 0, 0],
					], [[0, 0, 0, 0],
						[1, 0, 0, 0],
						[1, 1, 0, 0],
						[0, 1, 0, 0]
					], 
		]

class Shape6(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.states = [[[0, 0, 0, 0],
						[1, 1, 0, 0],
						[0, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 0, 1, 0],
						[0, 1, 1, 0],
						[0, 1, 0, 0],
					], [[0, 0, 0, 0],
						[1, 1, 0, 0],
						[0, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 0, 1, 0],
						[0, 1, 1, 0],
						[0, 1, 0, 0],
					],
		]

class Shape7(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.states = [[[0, 0, 0, 0],
						[0, 1, 0, 0],
						[1, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 0, 0],
					], [[0, 0, 0, 0],
						[0, 0, 0, 0],
						[1, 1, 1, 0],
						[0, 1, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 0, 0],
						[1, 1, 0, 0],
						[0, 1, 0, 0],
					],
		]
