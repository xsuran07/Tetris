#!/usr/bin/env python3

import pygame
import objects as ob
import constants as cons
import text
import picker

pygame.init()

class Game:
	def __init__(self):
		self.last_x_dif = 0 #stores last change of x coordidate of active object
		self.counter = 0 #conter of cycles in game loop
		self.y_speed = cons.Y_SPEED_SLOW #determines, how often active object fall one block down
		self.screen = pygame.display.set_mode((cons.WIDTH, cons.HEIGHT)) #main window of the game
		pygame.display.set_caption("Tetris")
		self.running = True #determines, if game loop should run
		self.clock = pygame.time.Clock() #determines FPS
		self.texts = [] #array with all text labels
		self.scores = [0, 0, 1] #values of SCORE, LINES and LEVEL
		self.picker = picker.Picker() #object thats perform picking random game object
		self.active = self.picker.pick() #randomly picked game object
		self.ocuppied = {} #hash map of all ocuppied blocks
		self.objects = [] #array of all game non active objects TODO this is redundant

		#sets boundaries
		for i in range(18):
			self.ocuppied[-1, i] = 1
			self.ocuppied[10, i] = 1
			self.ocuppied[i, 18] = 1

		#initialize all texts
		left_banner = ["SCORE", "LINES", "LEVEL"]
		right_banner = ["FIRST", "SECOND", "THIRD"]
		
		for i in range(3):
			self.texts.append(text.Text(left_banner[i], 0, i*cons.HEIGHT // 3, cons.WHITE, self.screen, True))
			self.texts.append(text.Text(right_banner[i], cons.WIDTH - cons.OFFSET, i*cons.HEIGHT // 3, cons.WHITE, self.screen, True))
			self.texts.append(text.Text(str(self.scores[i]), 0, i*cons.HEIGHT // 3 + 2*cons.FONT_INFO_SIZE, cons.BLACK, self.screen, False))

	# @brief Draws one block of play field
	def draw_block(self, x, y, color1, color2):
		x_cor = cons.OFFSET + x*cons.SQUARE
		y_cor =  y*cons.SQUARE
		pygame.draw.rect(self.screen, color1, (x_cor, y_cor, cons.SQUARE, cons.SQUARE))
   	
		x_cor = cons.OFFSET + x*cons.SQUARE+ 2
		y_cor =  y*cons.SQUARE + 2
		pygame.draw.rect(self.screen, color2, (x_cor, y_cor, cons.SQUARE - 4, cons.SQUARE - 4))

	## @brief Draws whole layout
	def draw_layout(self):
		#draws two side banners
		pygame.draw.rect(self.screen, cons.BLUE, (0, 0, cons.OFFSET, cons.HEIGHT))
		pygame.draw.rect(self.screen, cons.BLUE, (cons.WIDTH - cons.OFFSET, 0, cons.OFFSET, cons.HEIGHT))

		#draws main play field (empty)
		for i in range(cons.HEIGHT // cons.SQUARE):
			for j in range(10):
				self.draw_block(j, i, cons.WHITE, cons.BLACK)

		#draws all texts
		for text in self.texts:
			text.draw()

		#draws all non active objects
		for item in self.objects:
			item.draw(self.draw_block)

		self.active.draw(self.draw_block)

	## @brief Handles occurance of all events	
	def event_handler(self):
		#close main window if chosen
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				self.running = False
		
			elif(event.type == pygame.KEYDOWN):
				#change position of active objet
				if(event.key == pygame.K_UP):
					self.active.pos = (self.active.pos + 1) % 4
				#speeds down-movement of active object
				elif(event.key == pygame. K_DOWN):
					self.y_speed = cons.Y_SPEED_FAST
				#moves active object to the left
				elif(event.key == pygame.K_LEFT):
					self.active.add_x(-1)
					self.last_x_dif = -1
				#moves active object to the right
				elif(event.key == pygame.K_RIGHT):
					self.active.add_x(1)
					self.last_x_dif = 1
	
			#sets down-movementa of active object to normal
			elif(event.type == pygame.KEYUP):
				if(event.key == pygame.K_DOWN):
					self.y_speed = cons.Y_SPEED_SLOW
			
	## @brief Main game loop
	def loop(self):
		while(self.running):
			self.event_handler()	

			#checks if active object didn't hit ocuppied square (left-right direction)
			tmp = self.active.get_active_blocks()
			for item in tmp:
				if item in self.ocuppied:
					self.active.add_x(-self.last_x_dif)
					break

			if(self.counter % self.y_speed == 0):
				self.active.add_y(1)

			#checks if active object didn't hit ocuppied square (down direction)
			tmp = self.active.get_active_blocks()
			for item in tmp:
				if item in self.ocuppied:
					self.active.add_y(-1)
					self.active.add_active_blocks(self.ocuppied)
					self.objects.append(self.active)
					self.active = self.picker.pick()
					break

			self.draw_layout()

			pygame.display.update()

			self.counter += 1

			self.clock.tick(40)

game = Game()

game.loop()

pygame.quit()	

