import pygame
import constants as const

class Shape1:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.pos = 0
		self.color = const.RED
		self.states = [[[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
						[0, 0, 0, 0],
					], [[0, 0, 0, 0],
						[0, 1, 1, 0],
						[0, 1, 1, 0],
						[0, 0, 0, 0],
					],
		]

	def draw(self, drawer):
		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):
					drawer(self.x - 1 + j, self.y - 2 + i, const.WHITE, self.color)

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def set_cor(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

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
					ret[key] = self.color

		return ret
	
	def add_active_blocks(self, struct):
		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):
					key = (self.x - 1 + j, self.y - 2 + i)
					struct[key] = self.color

class Shape2(Shape1):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.color = const.GREEN
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
		self.color = const.BLUE
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
		self.color = const.LIGHT_PURPLE
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
		self.color = const.DARK_PURPLE
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
		self.color = const.LIGHT_ORANGE
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
		self.color = const.DARK_ORANGE
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
