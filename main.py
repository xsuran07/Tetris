#!/bin/python3

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

		#sets boundaries
		for i in range(18):
			self.ocuppied[-1, i] = cons.BLACK
			self.ocuppied[10, i] = cons.BLACK
			if(i < 10):
				self.ocuppied[i, 18] = cons.BLACK

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

		for key in self.ocuppied:
			color = self.ocuppied[key]
			if(color != cons.BLACK):
				self.draw_block(key[0], key[1], cons.WHITE, color)

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

	## @brief Checks, if there are new full lines (if so, removes them)
	## @return Number of removes lines + index of topmost removed line
	def full_lines(self):
		cnt = 0
		top_line = 42

		tmp = self.active.get_active_blocks()

		#finds out, if there is a continuos lines
		for item in tmp:
			line_out = True

			for i in range(10):
				if((i, item[1]) not in self.ocuppied):
					line_out = False
					break		

			#if so, removes them
			if(not line_out):
				continue

			cnt += 1
			top_line = min(top_line, item[1])

			for i in range(10):
				del self.ocuppied[(i, item[1])]

		return [cnt, top_line]

	## @brief Moves every block above removed lines down
	def move_blocks(self, to_remove, count):
		if(count == 0):
			return
		
		i = to_remove

		while(i >= 0):
			for j in range(10):
				if((j, i) in self.ocuppied):
					if(self.ocuppied[(j, i)] == cons.BLACK):
						continue
					else:
						self.ocuppied[(j, i + count)] = self.ocuppied[(j, i)]	
						del self.ocuppied[(j, i)]
			i -= 1

	## @brief Checks if blocks didn't reach the top
	## @brief Returns True if so, False otherwise
	def above_top(self):
		if(self.active.get_y() == 0):
			return True
		else:
			return False

	## @brief Checks if active object didn't colide with other blocks or edges
	## @brief Returns True if so, False otherwise
	def collision(self):
		tmp = self.active.get_active_blocks()
		for item in tmp:
			if item in self.ocuppied:
				return True

		return False	

	## @brief Main game loop
	def loop(self):
		while(self.running):
			self.event_handler()		

			#checks if active object didn't hit ocuppied square (left-right direction)
			for i in range(2):
				if(self.collision()):
					self.active.add_x(-self.last_x_dif)

			if(self.counter % self.y_speed == 0):
				self.active.add_y(1)

			#checks if active object didn't hit ocuppied square (down direction)
			if(self.collision()):
				if(self.above_top()):
					self.running = False	

				self.active.add_y(-1)
				self.active.add_active_blocks(self.ocuppied)

				cnt, top_line = self.full_lines()					
	
				self.move_blocks(top_line - 1, cnt)

				self.active = self.picker.pick()

			self.draw_layout()

			pygame.display.update()

			self.counter += 1

			self.clock.tick(40)

game = Game()

game.loop()

pygame.quit()	

