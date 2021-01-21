## @brief Implementation of button.
## @author Jakub Šuráň (xsuran07)

import pygame
import constants as const

## @class Implementation of simle button - changes color when hovered, calls event handler when pressed
class Button:
	def __init__(self, x, y, width, height, text, color, colorActive, handler=None):
			self.x = x
			self.y = y
			self.width = width
			self.height = height
			self.text = text
			self.color = color
			self.colorActive = colorActive
			self.active = False
			self.handler = handler
			self.size = self.height - 20
			self.font = pygame.font.SysFont('ubuntumono', self.size)

	## @brief Displays button on the screen (when button is hovered, it changes color)
	def draw(self, display):
		BLACK = (0, 0, 0)

		pygame.draw.rect(display, BLACK, (self.x, self.y, self.width, self.height))		
		if(self.active):
			pygame.draw.rect(display, self.colorActive, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))		
		else:
			pygame.draw.rect(display, self.color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))


		text = self.font.render(self.text, True, (0, 0, 0))
		display.blit(text, (self.x + (self.width - len(self.text)*self.size // 2) // 2, self.y + 10))

	## @brief Perform given action when button is pressed
	def eventHandler(self):
		self.handler()

class Keys:
	def __init__(self, x, y, fun, color=const.BLACK):
		self.x = x
		self.y = y
		self.fun = fun
		self.colors = [color, color, color, color]

	def set_all_black(self):
		for i in range(4):
			self.colors[i] = const.BLACK

	def set_color(self, num, color):
		self.colors[num] = color

	def draw(self):
		self.fun(self.x, self.y, const.WHITE, self.colors[0], 0)
		self.fun(self.x, self.y+const.SQUARE, const.WHITE, self.colors[1], 1)
		self.fun(self.x-const.SQUARE, self.y+const.SQUARE, const.WHITE, self.colors[2], 2)
		self.fun(self.x+const.SQUARE, self.y+const.SQUARE, const.WHITE, self.colors[3], 3)
	
