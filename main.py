#!/bin/python3

## @brief Implementation of main game logic.
## @author Jakub Šuráň (xsuran07)

import pygame
import objects as ob
import constants as const
import text
import picker
import button

pygame.init()

## @brief Main class handling controling of the whole game.
class Game:
	def __init__(self):
		x = const.WIDTH // 2 - const.ER_WIDTH // 2
		y = const.HEIGHT // 2 - const.ER_HEIGHT // 2

		self.last_x_dif = 0 #stores last change of x coordidate of active object
		self.counter = 0 #conter of cycles in game loop
		self.y_speed = const.Y_SPEED_SLOW #determines, how often active object fall one block down
		self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT)) #main window of the game
		pygame.display.set_caption("Tetris")
		self.state = const.START
		self.clock = pygame.time.Clock() #determines FPS
		self.texts = [] #array with all text labels
		self.end_report = []
		self.logo = text.Logo("TETRIS", x, y, self.screen, const.ER_WIDTH, 80)
		self.scores = [0, 0, 1] #values of SCORE, LINES and LEVEL
		self.picker = picker.Picker() #object thats perform picking random game object
		self.active = self.picker.pick(4, 0) #randomly picked game object
		self.ocuppied = {} #hash map of all ocuppied blocks
		self.next1 = self.picker.pick(const.NEXT1_X, const.NEXT1_Y)
		self.next2 = self.picker.pick(const.NEXT2_X, const.NEXT2_Y)
		self.next3 = self.picker.pick(const.NEXT3_X, const.NEXT3_Y)	
		self.running = True
		self.start_button = button.Button(x + const.ER_WIDTH // 2 - 75, y + 6*const.FONT_INFO_SIZE, 150, 75, "PLAY", const.RED, const.BLUE, self.start)
		self.retry_button = button.Button(x + const.ER_WIDTH // 2 - 75, y + 6*const.FONT_INFO_SIZE, 150, 75, "RETRY", const.RED, const.BLUE, self.retry)

		#sets boundaries
		for i in range(18):
			self.ocuppied[-1, i] = const.BLACK
			self.ocuppied[10, i] = const.BLACK
			if(i < 10):
				self.ocuppied[i, 18] = const.BLACK

		#initialize all texts
		left_banner = ["SCORE", "LINES", "LEVEL"]
		right_banner = ["FIRST", "SECOND", "THIRD"]
		
		for i in range(3):
			self.texts.append(text.Text(left_banner[i], 0, i*const.HEIGHT // 3, const.WHITE, self.screen, const.OFFSET, const.FONT_INFO_SIZE, True))
			self.texts.append(text.Text(right_banner[i], const.WIDTH - const.OFFSET, i*const.HEIGHT // 3, const.WHITE, self.screen, const.OFFSET, const.FONT_INFO_SIZE, True))
			self.texts.append(text.Text(str(self.scores[i]), 0, i*const.HEIGHT // 3 + 2*const.FONT_INFO_SIZE, const.BLACK, self.screen, const.OFFSET, const.FONT_INFO_SIZE))

		
		self.end_report.append(text.Text("GAME OVER", x, y, const.WHITE, self.screen, const.ER_WIDTH, True))
		for i in range(3):
			self.end_report.append(text.Text("Final " + left_banner[i]+":" + str(self.scores[i]), x, y + (i+2)*const.FONT_INFO_SIZE, const.BLACK, self.screen,  const.ER_WIDTH, const.FONT_INFO_SIZE))

	def start(self):
		self.state = const.GAME

	def retry(self):
		self.next1 = self.picker.pick(const.NEXT1_X, const.NEXT1_Y)
		self.next2 = self.picker.pick(const.NEXT2_X, const.NEXT2_Y)
		self.next3 = self.picker.pick(const.NEXT3_X, const.NEXT3_Y)
		self.active = self.picker.pick(4, 0)
		self.state = const.GAME
		self.scores = [0, 0, 1]
		self.ocuppied.clear()
		self.y_speed = const.Y_SPEED_SLOW
	
		for i in range(3):
			self.texts[2 + i*3].set_text(str(self.scores[i]))

	
		#sets boundaries
		for i in range(18):
			self.ocuppied[-1, i] = const.BLACK
			self.ocuppied[10, i] = const.BLACK
			if(i < 10):
				self.ocuppied[i, 18] = const.BLACK



	## @brief Draws one block of play field.
	def draw_block(self, x, y, color1, color2):
		x_cor = const.OFFSET + x*const.SQUARE
		y_cor =  y*const.SQUARE
		pygame.draw.rect(self.screen, color1, (x_cor, y_cor, const.SQUARE, const.SQUARE))
   	
		x_cor = const.OFFSET + x*const.SQUARE+ 2
		y_cor =  y*const.SQUARE + 2
		pygame.draw.rect(self.screen, color2, (x_cor, y_cor, const.SQUARE - 4, const.SQUARE - 4))

	## @brief Draws whole layout.
	def draw_layout(self):
		#draws two side banners
		pygame.draw.rect(self.screen, const.BLUE, (0, 0, const.OFFSET, const.HEIGHT))
		pygame.draw.rect(self.screen, const.BLUE, (const.WIDTH - const.OFFSET, 0, const.OFFSET, const.HEIGHT))

		#draws main play field (empty)
		for i in range(const.HEIGHT // const.SQUARE):
			for j in range(10):
				self.draw_block(j, i, const.WHITE, const.BLACK)

		#draws all texts
		for text in self.texts:
			text.draw()

		for key in self.ocuppied:
			color = self.ocuppied[key]
			if(color != const.BLACK):
				self.draw_block(key[0], key[1], const.WHITE, color)

		if(self.state == const.START):
			pygame.draw.rect(self.screen, const.WHITE, (const.WIDTH // 2 - const.ER_WIDTH // 2, const.HEIGHT // 2 - const.ER_HEIGHT // 2, const.ER_WIDTH, const.ER_HEIGHT))
			self.logo.draw()

			self.start_button.draw(self.screen)
		elif(self.state == const.GAME):
			self.next1.draw(self.draw_block)
			self.next2.draw(self.draw_block)
			self.next3.draw(self.draw_block)
			self.active.draw(self.draw_block)

		else:
			pygame.draw.rect(self.screen, const.WHITE, (const.WIDTH // 2 - const.ER_WIDTH // 2, const.HEIGHT // 2 - const.ER_HEIGHT // 2, const.ER_WIDTH, const.ER_HEIGHT))
			for text in self.end_report:
				text.draw()

			self.retry_button.draw(self.screen)

	## @brief Handles occurance of all events.
	def event_handler(self):
		#close main window if chosen
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				self.running = False
			elif(event.type == pygame.MOUSEMOTION):
				if(self.state == const.START):
					if(self.start_button.x <=event.pos[0] <=self.start_button.x + self.start_button.width and self.start_button.y <= event.pos[1] <= self.start_button.y + self.start_button.height):
						self.start_button.active = True
					else:
						self.start_button.active = False
				elif(self.state == const.GAME_OVER):	
					if(self.retry_button.x <=event.pos[0] <=self.retry_button.x + self.retry_button.width and self.retry_button.y <= event.pos[1] <= self.retry_button.y + self.retry_button.height):
						self.retry_button.active = True
					else:
						self.retry_button.active = False	
			elif(event.type == pygame.MOUSEBUTTONDOWN):
				if(self.start_button.active and self.state == const.START):
					self.start_button.eventHandler()
				elif(self.retry_button.active and self.state == const.GAME_OVER):
					self.retry_button.eventHandler()
	
			elif(event.type == pygame.KEYDOWN and self.state == const.GAME):
				#change position of active objet
				if(event.key == pygame.K_UP):
					self.active.pos = (self.active.pos + 1) % 4
				#speeds down-movement of active object
				elif(event.key == pygame. K_DOWN):
					self.y_speed = const.Y_SPEED_FAST
				#moves active object to the left
				elif(event.key == pygame.K_LEFT):
					self.active.add_x(-1)
					self.last_x_dif = -1
				#moves active object to the right
				elif(event.key == pygame.K_RIGHT):
					self.active.add_x(1)
					self.last_x_dif = 1
	
			#sets down-movementa of active object to normal
			elif(event.type == pygame.KEYUP and self.state == const.GAME):
				if(event.key == pygame.K_DOWN):
					self.y_speed = const.Y_SPEED_SLOW

	## @brief Checks, if there are new full lines (if so, removes them).
	## @return Number of removes lines + index of topmost removed line.
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

	## @brief Moves every block above removed lines down.
	def move_blocks(self, to_remove, count):
		if(count == 0):
			return
		
		i = to_remove

		while(i >= 0):
			for j in range(10):
				if((j, i) in self.ocuppied):
					if(self.ocuppied[(j, i)] == const.BLACK):
						continue
					else:
						self.ocuppied[(j, i + count)] = self.ocuppied[(j, i)]	
						del self.ocuppied[(j, i)]
			i -= 1

	## @brief Checks if active object didn't colide with other blocks or edges.
	## @brief Returns True if so, False otherwise.
	def collision(self):
		tmp = self.active.get_active_blocks()
		for item in tmp:
			if item in self.ocuppied:
				return True

		return False	

	## @brief Main game loop.
	def loop(self):
		while(self.running):
			self.event_handler()		

			if(self.state == const.GAME):
				#checks if active object didn't hit ocuppied square (left-right direction)
				for i in range(2):
					if(self.collision()):
						self.active.add_x(-self.last_x_dif)

				if(self.counter % self.y_speed == 0):
					self.active.add_y(1)

				#checks if active object didn't hit ocuppied square (down direction)
				if(self.collision()):

					self.active.add_y(-1)
					if(not self.active.add_active_blocks(self.ocuppied)):
						self.texts[const.T_SCORE].set_text("")
						self.texts[const.T_LINES].set_text("")
						self.texts[const.T_LEVEL].set_text("")
						self.state = const.GAME_OVER
						continue

					cnt, top_line = self.full_lines()					
					self.scores[const.LINES] += cnt
					self.texts[const.T_LINES].set_text(str(self.scores[const.LINES]))
	
					self.move_blocks(top_line - 1, cnt)

					self.active = self.next1
					self.active.set_cor(4, 0)

					self.next1 = self.next2
					self.next1.set_cor(const.NEXT1_X, const.NEXT1_Y)	

					self.next2 = self.next3
					self.next2.set_cor(const.NEXT2_X, const.NEXT2_Y)

					self.next3 = self.picker.pick(const.NEXT3_X, const.NEXT3_Y)

			self.draw_layout()

			pygame.display.update()

			self.counter += 1

			self.clock.tick(40)

game = Game()

game.loop()

pygame.quit()	

