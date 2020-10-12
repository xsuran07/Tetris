#!/bin/python3

import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FONT_INFO_SIZE = 60
SQUARE = WIDTH // 20

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Tetris")
		self.running = True
		self.clock = pygame.time.Clock()
		self.scores = [0, 0, 1]
		self.font_info = pygame.font.SysFont("ubuntumono", FONT_INFO_SIZE) 

	## @breif Function for displaying text
	# @param text Text to be displayed
	# @param color Color of the text
	# @param pos Position of the text
	# @param padding Flag to determine if there will be padding arround text 
	def draw_text(self, text, color, pos, padding=False):
		if(padding):
			pygame.draw.rect(self.screen, BLACK, (pos[0], pos[1], WIDTH // 4, FONT_INFO_SIZE))

		tmp = self.font_info.render(text, True, color)
		self.screen.blit(tmp, (pos[0] + WIDTH // 8 - len(text)*FONT_INFO_SIZE//4, pos[1]))

	## @breif Draws whole background
	def draw_background(self):
		left_banner = ["SCORE", "LINES", "LEVEL"]
		right_banner = ["FIRST", "SECOND", "THIRD"]
		
		
		pygame.draw.rect(self.screen, WHITE, (0, 0, WIDTH // 4, HEIGHT))
		pygame.draw.rect(self.screen, WHITE, (3 * WIDTH // 4, 0, WIDTH // 4, HEIGHT))

		for i in range(1, 10):
			pygame.draw.line(self.screen, WHITE, (WIDTH // 4 + i*SQUARE, 0), (WIDTH // 4 + i*SQUARE, HEIGHT))

		for i in range(1, HEIGHT // SQUARE):
			pygame.draw.line(self.screen, WHITE, (WIDTH // 4, i*SQUARE), (3*WIDTH // 4, i*SQUARE))

		for i in range(3):
			self.draw_text(left_banner[i], WHITE, (0, i*HEIGHT // 3), True)
			self.draw_text(right_banner[i], WHITE, (3 * WIDTH // 4, i*HEIGHT // 3), True)
			self.draw_text(str(self.scores[i]), BLACK, (0, i*HEIGHT // 3 + 2*FONT_INFO_SIZE))

	## @brief Handles occurance of all events	
	def event_handler(self):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				self.running = False

	## @brief Main game loop
	def loop(self):
		while(self.running):
			self.event_handler()

			self.draw_background()

			pygame.display.update()

			self.clock.tick(40)


game = Game()

game.loop()

pygame.quit()	

