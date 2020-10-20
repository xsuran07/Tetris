import pygame

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
	def draw(self, display):
		BLACK = (0, 0, 0)
		size = self.height - 20

		pygame.draw.rect(display, BLACK, (self.x, self.y, self.width, self.height))		
		if(self.active):
			pygame.draw.rect(display, self.colorActive, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))		
		else:
			pygame.draw.rect(display, self.color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))

		font = pygame.font.SysFont('ubuntumono', size)

		t = font.render(self.text, True, (0, 0, 0))
		display.blit(t, (self.x + (self.width - len(self.text)*size // 2) // 2, self.y + 10))

	def eventHandler(self):
		self.handler()


