#!/bin/python3

import pygame
import objects as ob
import constants as cons
import text
import picker

pygame.init()

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((cons.WIDTH, cons.HEIGHT))
		pygame.display.set_caption("Tetris")
		self.running = True
		self.clock = pygame.time.Clock()
		self.texts = []
		self.scores = [0, 0, 1]
		self.font_info = pygame.font.SysFont("ubuntumono", cons.FONT_INFO_SIZE) 
		self.picker = picker.Picker()
		self.active = self.picker.pick()

		#initialize all texts
		left_banner = ["SCORE", "LINES", "LEVEL"]
		right_banner = ["FIRST", "SECOND", "THIRD"]
		
		for i in range(3):
			self.texts.append(text.Text(left_banner[i], 0, i*cons.HEIGHT // 3, cons.WHITE, self.screen, True))
			self.texts.append(text.Text(right_banner[i], cons.WIDTH - cons.OFFSET, i*cons.HEIGHT // 3, cons.WHITE, self.screen, True))
			self.texts.append(text.Text(str(self.scores[i]), 0, i*cons.HEIGHT // 3 + 2*cons.FONT_INFO_SIZE, cons.BLACK, self.screen, False))

	def draw_block(self, x, y, color1, color2):
		x_cor = cons.OFFSET + x*cons.SQUARE
		y_cor =  y*cons.SQUARE
		pygame.draw.rect(self.screen, color1, (x_cor, y_cor, cons.SQUARE, cons.SQUARE))
   	
		x_cor = cons.OFFSET + x*cons.SQUARE+ 2
		y_cor =  y*cons.SQUARE + 2
		pygame.draw.rect(self.screen, color2, (x_cor, y_cor, cons.SQUARE - 4, cons.SQUARE - 4))

	## @breif Draws whole background
	def draw_background(self):
		pygame.draw.rect(self.screen, cons.BLUE, (0, 0, cons.OFFSET, cons.HEIGHT))
		pygame.draw.rect(self.screen, cons.BLUE, (cons.WIDTH - cons.OFFSET, 0, cons.OFFSET, cons.HEIGHT))

		for i in range(cons.HEIGHT // cons.SQUARE):
			for j in range(10):
				self.draw_block(j, i, cons.WHITE, cons.BLACK)

		for text in self.texts:
			text.draw()

		self.active.draw(self.draw_block)

	## @brief Handles occurance of all events	
	def event_handler(self):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				self.running = False
			elif(event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_UP):
					self.active.pos = (self.active.pos + 1) % 4

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

