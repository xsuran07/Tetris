## @brief Implementation of class for displaying text.
## @author Jakub Šuráň (xsuran07)

import pygame
import constants as cons

## @brief Class for displaying text.
class Text:
	def __init__(self, text, x, y, color, screen, box):
		self.text = text
		self.x = x
		self.y = y
		self.color =  color
		self.font = pygame.font.SysFont("ubuntumono", cons.FONT_INFO_SIZE)
		self.screen = screen
		self.box = box

	## @brief Displays given text.
	def draw(self):
		if(self.box):
			pygame.draw.rect(self.screen, cons.BLACK, (self.x, self.y, cons.OFFSET, cons.FONT_INFO_SIZE))

		tmp = self.font.render(self.text, True, self.color)
		self.screen.blit(tmp, (self.x + cons.WIDTH // 8 - len(self.text)*cons.FONT_INFO_SIZE//4, self.y))

	## @brief
	def set_text(self, new_text):
		self.text = new_text
