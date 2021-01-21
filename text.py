## @brief Implementation of class for displaying text.
## @author Jakub Šuráň (xsuran07)

import pygame
import constants as const

## @brief Class for displaying text.
class Text:
	def __init__(self, text, x, y, color, screen, width, size, box=False):
		self.text = text
		self.x = x
		self.y = y
		self.color =  color
		self.screen = screen
		self.width = width
		self.box = box
		self.size = size
		self.font = pygame.font.SysFont("ubuntumono", self.size)

	## @brief Displays given text.
	def draw(self):
		if(self.box):
			pygame.draw.rect(self.screen, const.ALMOST_BLACK, (self.x, self.y, self.width, self.size))

		tmp = self.font.render(self.text, True, self.color)
		self.screen.blit(tmp, (self.x + self.width // 2 - len(self.text)*self.size//4, self.y))

	## @brief
	def set_text(self, new_text):
		self.text = new_text

## @brief Class for displaying logo.
class Logo(Text):
	def __init__(self, x, y, screen, width, size):
		super().__init__("TETRIS", x, y, const.BLACK, screen, width, size, box=False)

		self.color = [(255,0,0), (51, 204, 51), (0,0,255), (128, 0,128), (255, 200, 0), (255, 150, 0)]

	## @brief Displays given logo.
	def draw(self):
		for i in range(len(self.text)):
			text = self.font.render(str(self.text[i]), True, self.color[i])
			self.screen.blit(text, (i * self.size//2 + self.x + self.width // 2 - len(self.text)*self.size//4 , self.y))
