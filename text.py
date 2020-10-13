import pygame
import constants as cons

class Text:
	def __init__(self, text, x, y, color, screen, box):
		self.text = text
		self.x = x
		self.y = y
		self.color =  color
		self.font = pygame.font.SysFont("ubuntumono", cons.FONT_INFO_SIZE)
		self.screen = screen
		self.box = box

	def draw(self):
		if(self.box):
			pygame.draw.rect(self.screen, cons.BLACK, (self.x, self.y, cons.OFFSET, cons.FONT_INFO_SIZE))

		tmp = self.font.render(self.text, True, self.color)
		self.screen.blit(tmp, (self.x + cons.WIDTH // 8 - len(self.text)*cons.FONT_INFO_SIZE//4, self.y))


