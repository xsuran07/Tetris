## @brief Implementation of game objects.
## @author Jakub Šuráň (xsuran07)

import pygame
import constants as const

## @class Representation of game object ("square")
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

	## @brief Simple method for getting x-coordinate.
	## @return Returns object's x-coordinate.
	def get_x(self):
		return self.x

	## @brief Simple method for getting y-coordinate.
	## @return Returns object's y-coordinate.
	def get_y(self):
		return self.y

	## @brief Simple method for setting both coordinates.
	def set_cor(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	## @brief Adds given value to x-coordinate.
	def add_x(self, value):
		self.x += value

	## @brief Adds given value to y-coordinate.
	def add_y(self, value):
		self.y += value
	
	## @brief Finds out which blocks on playing field are occupied by the object.
	## @return Returns hash map with occupied blocks.
	def get_active_blocks(self):
		ret = {}

		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):
					key = (self.x - 1 + j, self.y - 2 + i)
					ret[key] = self.color

		return ret
	
	## @brief Adds blocks which object currently occupies into given hash map + checks if object isn't over the top.
	## @return True if everything is ok, False if any part of object is over the top of playing field.
	def add_active_blocks(self, struct):
		ret = True

		for i, row in enumerate(self.states[self.pos]):
			for j, square in enumerate(row):
				if(square):					
					key = (self.x - 1 + j, self.y - 2 + i)

					if(key[1] < 0):
						ret = False
						continue
					struct[key] = self.color
					
		return ret
	
## @class Representation of game object ("long line")
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

## @class Representation of game object ("reverse L")
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

## @class Representation of game object ("L")
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

## @class Representation of game object ("reverse Z")
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

## @class Representation of game object ("Z")
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

## @class Representation of game object ("ship")
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
