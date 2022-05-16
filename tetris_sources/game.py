'''
Author(s): Jakub Šuráň

Implementation of main game logic.
'''

import pygame

from . import objects as ob
from . import constants as const
from . import text
from . import picker
from . import button


class Game:
    '''
    Main class handling controling of the whole game.
    '''

    def __init__(self):
        self.last_x_dif = 0  # stores last change of x coordidate of active object
        self.counter = 0  # conter of cycles in game loop
        self.y_speed = const.Y_SPEED_DEMO  # determines, how often active object fall one block down
        self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))  # main window of the game
        pygame.display.set_caption('Tetris')
        self.state = const.START  # state of game (START, GAME, GAME_OVER)
        self.clock = pygame.time.Clock()  # determines FPS
        self.texts = []  # array with all text labels on side banners
        self.end_report = []  # array with texts on ending screen
        self.scores = [0, 0, 1]  # values of SCORE, LINES and LEVEL
        self.picker = picker.Picker()  # object thats perform picking random game object
        self.active = ob.Shape3(4, 0)  # active game object
        self.ocuppied = {}  # hash map of all ocuppied blocks
        self.next1 = self.picker.pick(const.NEXT1_X, const.NEXT1_Y)  # first next game object
        self.next2 = self.picker.pick(const.NEXT2_X, const.NEXT2_Y)  # second next game object
        self.next3 = self.picker.pick(const.NEXT3_X, const.NEXT3_Y)  # third next game object
        self.running = True  # determines wheater game is running
        self.center_x = (const.WIDTH - const.ER_WIDTH) // 2  # x-coordinate of box on start and ending screens
        self.center_y = (const.HEIGHT - const.ER_HEIGHT) // 2  # y-coordinate of box on start and ending screens
        self.left_banner = ['SCORE', 'LINES', 'LEVEL']  # texts displayed on the left banner
        self.right_banner = ['FIRST', 'SECOND', 'THIRD']  # texts displayed on the right banner
        self.pause_text = text.Text('PAUSE', self.center_x, self.center_y, const.WHITE, self.screen,
                                    const.ER_WIDTH, const.TEXT_SIZE, True)  # Header of the pause screen
        self.study_phase = 0  # determines current state of 'How to play'
        self.keys = button.Keys(
            const.WIDTH // 2 - const.SQUARE//2, 3 * const.HEIGHT // 4, self.draw_key)  # part of animation - arrows
        self.animation_counter = 0  # counter controling animation behavior
        self.change = [False, 0]  # flag and counter controling animation behavior
        self.help_text = text.Text('1/3', const.OFFSET, const.HEIGHT//2, const.BLACK, self.screen,
                                   const.WIDTH - 2*const.OFFSET,
                                   const.TEXT_SIZE, False)  # text which displays current state of 'How to play'
        self.infos = ['You can move with the falling object using right and left arrow - see the animation.',
                      'You can rotate the falling object using up arraw - see the animation.',
                      'You can speed up movement of the falling object using down arraw - see the '
                      'animation.']  # texts for 'How to play'
        self.help_info = text.Text(self.infos[self.study_phase], const.OFFSET, const.HEIGHT//2 + const.TEXT_SIZE,
                                   const.BLACK, self.screen, const.WIDTH - 2*const.OFFSET, const.TEXT_SIZE2,
                                   False, False)  # displays currnt info in 'How to play'

        # sets boundaries
        for i in range(18):
            self.ocuppied[-1, i] = const.BLACK
            self.ocuppied[10, i] = const.BLACK
            if(i < 10):
                self.ocuppied[i, 18] = const.BLACK

        # initialize buttons
        x_coor = (const.WIDTH - const.BUTTON_WIDTH) // 2

        self.play_button = button.Button(x_coor, self.center_y + 4*const.TEXT_SIZE, const.BUTTON_WIDTH,
                                         const.BUTTON_HEIGHT, 'PLAY', const.RED, const.BLUE, self.start)
        self.help_button = button.Button(x_coor, self.center_y + 6*const.TEXT_SIZE, const.BUTTON_WIDTH,
                                         const.BUTTON_HEIGHT, 'HELP', const.RED, const.BLUE, self.help)
        self.retry_button = button.Button(x_coor, self.center_y + 6*const.TEXT_SIZE, const.BUTTON_WIDTH,
                                          const.BUTTON_HEIGHT, 'RETRY', const.RED, const.BLUE, self.retry)
        self.pause_button = button.Button((const.OFFSET-const.BUTTON_WIDTH) // 2,
                                          const.HEIGHT - const.BUTTON_HEIGHT - 10,
                                          const.BUTTON_WIDTH, const.BUTTON_HEIGHT, 'PAUSE', const.RED, const.BLUE,
                                          self.pause)
        self.resume_button = button.Button(x_coor, self.center_y + 4*const.TEXT_SIZE, const.BUTTON_WIDTH,
                                           const.BUTTON_HEIGHT, 'RESUME', const.RED, const.BLUE, self.resume)
        self.menu_button = button.Button(x_coor, self.center_y + 2*const.TEXT_SIZE, const.BUTTON_WIDTH,
                                         const.BUTTON_HEIGHT, 'MENU', const.RED, const.BLUE, self.menu)
        self.prev_button = button.Button(const.OFFSET, const.HEIGHT - const.BUTTON_HEIGHT - 10, const.BUTTON_WIDTH,
                                         const.BUTTON_HEIGHT, 'PREV', const.RED, const.BLUE, self.prev)
        self.next_button = button.Button(const.WIDTH - const.OFFSET - const.BUTTON_WIDTH,
                                         const.HEIGHT - const.BUTTON_HEIGHT - 10, const.BUTTON_WIDTH,
                                         const.BUTTON_HEIGHT, 'NEXT', const.RED, const.BLUE, self.next)
        self.help_end_button = button.Button(const.WIDTH - const.OFFSET - const.BUTTON_WIDTH,
                                             const.HEIGHT - const.BUTTON_HEIGHT - 10, const.BUTTON_WIDTH,
                                             const.BUTTON_HEIGHT, 'MENU', const.RED, const.BLUE, self.menu)

        # INITIALIZE ALL TEXTS
        # logo on starting screen
        self.logo = text.Logo(self.center_x, self.center_y, self.screen, const.ER_WIDTH, const.LOGO_SIZE)

        # on side banners
        for i in range(3):
            self.texts.append(text.Text(self.left_banner[i], 0, i*const.HEIGHT // 3, const.WHITE, self.screen,
                              const.OFFSET, const.TEXT_SIZE, True))
            self.texts.append(text.Text(self.right_banner[i], const.WIDTH - const.OFFSET, i*const.HEIGHT // 3,
                              const.WHITE, self.screen, const.OFFSET, const.TEXT_SIZE, True))
            self.texts.append(text.Text(str(self.scores[i]), 0, i*const.HEIGHT // 3 + 2*const.TEXT_SIZE,
                              const.BLACK, self.screen, const.OFFSET, const.TEXT_SIZE))

        # on ending screen
        self.end_report.append(text.Text('GAME OVER', self.center_x, self.center_y, const.WHITE, self.screen,
                               const.ER_WIDTH, const.TEXT_SIZE, True))
        for i in range(3):
            y_coor = self.center_y + (i+2)*const.TEXT_SIZE
            self.end_report.append(text.Text('Final ' + self.left_banner[i]+':' + str(self.scores[i]),
                                   self.center_x, y_coor, const.BLACK, self.screen,  const.ER_WIDTH, const.TEXT_SIZE))

    def start(self):
        '''
        Setup game when PLAY button is pressed
        '''
        self.play_button.active = False
        self.state = const.GAME
        self.y_speed = const.Y_SPEED_SLOW
        self.active = self.picker.pick(4, 0)

    def help(self):
        '''
        Handles transition when HELP button is pressed
        '''

        self.help_button.active = False
        self.state = const.HELP
        self.animation_counter = 0
        self.study_phase = 0
        self.help_text.set_text(str(self.study_phase+1) + '/3')
        self.active = ob.Shape3(4, 0)

    def pause(self):
        '''
        Handles transition when PAUSE button is pressed
        '''

        self.pause_button.active = False
        self.state = const.PAUSE

    def resume(self):
        '''
        Handles transition when RESUME button is pressed
        '''

        self.resume_button.active = False
        self.state = const.GAME

    def menu(self):
        '''
        Handles transition when MENU button is pressed
        '''
        self.retry()
        self.help_end_button.active = False
        self.menu_button.active = False
        self.next_button.active = False
        self.state = const.START
        self.prev_button.active = False

    def prev(self):
        '''
        Handles transition when PREV button is pressed
        '''

        self.study_phase -= 1
        self.animation_counter = 0
        self.active.x = 4
        self.active.y = 0
        self.active.pos = 0
        self.keys.set_all_black()
        self.help_text.set_text(str(self.study_phase+1) + '/3')
        self.help_info.set_text(self.infos[self.study_phase])

    def next(self):
        '''
        Handles transition when NEXT button is pressed
        '''
        self.study_phase += 1
        self.animation_counter = 0
        self.active.x = 4
        self.active.y = 0
        self.active.pos = 0
        self.keys.set_all_black()
        self.help_text.set_text(str(self.study_phase+1) + '/3')
        self.help_info.set_text(self.infos[self.study_phase])

    def retry(self):
        '''
        Setup game when RETRY button is pressed
        '''

        self.retry_button.active = False
        self.next1 = self.picker.pick(const.NEXT1_X, const.NEXT1_Y)
        self.next2 = self.picker.pick(const.NEXT2_X, const.NEXT2_Y)
        self.next3 = self.picker.pick(const.NEXT3_X, const.NEXT3_Y)
        self.active = self.picker.pick(4, 0)
        self.state = const.GAME
        self.scores = [0, 0, 1]
        self.ocuppied.clear()
        self.y_speed = const.Y_SPEED_SLOW

        # set texts
        for i in range(3):
            self.texts[2 + i*3].set_text(str(self.scores[i]))

        # sets boundaries
        for i in range(18):
            self.ocuppied[-1, i] = const.BLACK
            self.ocuppied[10, i] = const.BLACK
            if(i < 10):
                self.ocuppied[i, 18] = const.BLACK

    def draw_block(self, x, y, color1, color2):
        '''
        Draws one block of play field.
        '''

        x_cor = const.OFFSET + x*const.SQUARE
        y_cor = y*const.SQUARE
        pygame.draw.rect(self.screen, color1, (x_cor, y_cor, const.SQUARE, const.SQUARE))

        x_cor = const.OFFSET + x*const.SQUARE + 2
        y_cor = y*const.SQUARE + 2
        pygame.draw.rect(self.screen, color2, (x_cor, y_cor, const.SQUARE - 4, const.SQUARE - 4))

    def draw_key(self, x_cor, y_cor, color1, color2, ar):
        '''
        Draws arrows for animation in 'How to play'
        '''

        pygame.draw.rect(self.screen, color1, (x_cor, y_cor, const.SQUARE, const.SQUARE))

        pygame.draw.rect(self.screen, color2, (x_cor+2, y_cor+2, const.SQUARE - 4, const.SQUARE - 4))

        if(ar == 0):
            pygame.draw.lines(self.screen, const.WHITE, False, ((x_cor+8, y_cor+const.SQUARE-15),
                              ((x_cor+const.SQUARE // 2), y_cor+10), (x_cor + const.SQUARE-8, y_cor+const.SQUARE-15)))
        elif(ar == 2):
            pygame.draw.lines(self.screen, const.WHITE, False, ((x_cor+const.SQUARE-8, y_cor+10),
                              (x_cor+8, y_cor+const.SQUARE // 2), (x_cor+const.SQUARE-8, y_cor+const.SQUARE-15)))
        elif(ar == 3):
            pygame.draw.lines(self.screen, const.WHITE, False, ((x_cor+8, y_cor+10),
                              (x_cor+const.SQUARE-8, y_cor+const.SQUARE // 2), (x_cor+8, y_cor+const.SQUARE-15)))
        else:
            pygame.draw.lines(self.screen, const.WHITE, False, ((x_cor+8, y_cor+10),
                              ((x_cor+const.SQUARE // 2), y_cor+const.SQUARE-15), (x_cor + const.SQUARE-8, y_cor+10)))

    def draw_layout(self):
        '''
        Draws whole layout.
        '''

        # draws two side banners
        pygame.draw.rect(self.screen, const.LIGHT_YELLOW, (0, 0, const.OFFSET, const.HEIGHT))
        pygame.draw.rect(self.screen, const.LIGHT_YELLOW, (const.WIDTH - const.OFFSET, 0, const.OFFSET, const.HEIGHT))

        # draws main play field (empty)
        for i in range(const.HEIGHT // const.SQUARE):
            for j in range(10):
                self.draw_block(j, i, const.GRAY, const.BLACK)

        # draws texts on side banners
        for sign in self.texts:
            sign.draw()

        # draws all ocouppied squares
        for key in self.ocuppied:
            color = self.ocuppied[key]
            if(color != const.BLACK):
                self.draw_block(key[0], key[1], const.WHITE, color)

        # draws logo + buttons on starting screen (START)
        if(self.state == const.START):
            pygame.draw.rect(self.screen, const.LIGHT_BLUE,
                             (self.center_x, self.center_y, const.ER_WIDTH, const.ER_HEIGHT))
            self.logo.draw()

            self.play_button.draw(self.screen)
            self.help_button.draw(self.screen)
        # draws layout for 'How to play' state(HELP)
        elif(self.state == const.HELP):
            pygame.draw.rect(self.screen, const.LIGHT_BLUE, (const.OFFSET, (const.HEIGHT//const.SQUARE)//2*const.SQUARE,
                             const.WIDTH - 2*const.OFFSET, const.HEIGHT))

            self.keys.draw()

            self.active.draw(self.draw_block)

            if(self.study_phase > 0):
                self.prev_button.draw(self.screen)

            if(self.study_phase < 2):
                self.next_button.draw(self.screen)

            if(self.study_phase == 2):
                self.help_end_button.draw(self.screen)

            self.help_text.draw()
            self.help_info.draw()
        # draws 3 next game objects + active game object (GAME)
        elif(self.state == const.GAME):
            self.next1.draw(self.draw_block)
            self.next2.draw(self.draw_block)
            self.next3.draw(self.draw_block)
            self.active.draw(self.draw_block)
            self.pause_button.draw(self.screen)
        # draws layout for pause state state(PAUSE)
        elif(self.state == const.PAUSE):
            self.next1.draw(self.draw_block)
            self.next2.draw(self.draw_block)
            self.next3.draw(self.draw_block)
            self.active.draw(self.draw_block)
            self.pause_button.draw(self.screen)

            pygame.draw.rect(self.screen, const.LIGHT_BLUE, (self.center_x, self.center_y, const.ER_WIDTH,
                             const.ER_HEIGHT))
            self.pause_text.draw()
            self.retry_button.draw(self.screen)
            self.resume_button.draw(self.screen)
            self.menu_button.draw(self.screen)
        # draws texts + button on ending screen (GAME_OVER)
        else:
            pygame.draw.rect(self.screen, const.LIGHT_BLUE, (self.center_x, self.center_y, const.ER_WIDTH,
                             const.ER_HEIGHT))
            for sign in self.end_report:
                sign.draw()

            self.retry_button.draw(self.screen)

    def event_handler(self):
        '''
        Handles occurance of all events.
        '''

        # close main window if chosen
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.running = False
            elif(event.type == pygame.MOUSEMOTION):
                if(self.state == const.START):
                    # check if PLAY button should become active
                    if(self.play_button.x <= event.pos[0] <= self.play_button.x + self.play_button.width
                       and self.play_button.y <= event.pos[1] <= self.play_button.y + self.play_button.height):
                        self.play_button.active = True
                    else:
                        self.play_button.active = False

                    # check if HELP button should become active
                    if(self.help_button.x <= event.pos[0] <= self.help_button.x + self.help_button.width
                       and self.help_button.y <= event.pos[1] <= self.help_button.y + self.help_button.height):
                        self.help_button.active = True
                    else:
                        self.help_button.active = False
                elif(self.state == const.GAME_OVER):
                    # check if RETRY button should become active
                    if(self.retry_button.x <= event.pos[0] <= self.retry_button.x + self.retry_button.width
                       and self.retry_button.y <= event.pos[1] <= self.retry_button.y + self.retry_button.height):
                        self.retry_button.active = True
                    else:
                        self.retry_button.active = False
                elif(self.state == const.GAME):
                    # check if PAUSE button should become active
                    if(self.pause_button.x <= event.pos[0] <= self.pause_button.x + self.pause_button.width
                       and self.pause_button.y <= event.pos[1] <= self.pause_button.y + self.pause_button.height):
                        self.pause_button.active = True
                    else:
                        self.pause_button.active = False
                elif(self.state == const.PAUSE):
                    # check if RESUME button should become active
                    if(self.resume_button.x <= event.pos[0] <= self.resume_button.x + self.resume_button.width
                       and self.resume_button.y <= event.pos[1] <= self.resume_button.y + self.resume_button.height):
                        self.resume_button.active = True
                    else:
                        self.resume_button.active = False

                    # check if RETRY button should become active
                    if(self.retry_button.x <= event.pos[0] <= self.retry_button.x + self.retry_button.width
                       and self.retry_button.y <= event.pos[1] <= self.retry_button.y + self.retry_button.height):
                        self.retry_button.active = True
                    else:
                        self.retry_button.active = False

                    # check if MENU button should become active
                    if(self.menu_button.x <= event.pos[0] <= self.menu_button.x + self.menu_button.width
                       and self.menu_button.y <= event.pos[1] <= self.menu_button.y + self.menu_button.height):
                        self.menu_button.active = True
                    else:
                        self.menu_button.active = False
                elif(self.state == const.HELP):
                    # check if PREV button should become active
                    if(self.prev_button.x <= event.pos[0] <= self.prev_button.x + self.prev_button.width
                       and self.prev_button.y <= event.pos[1] <= self.prev_button.y + self.prev_button.height):
                        self.prev_button.active = True
                    else:
                        self.prev_button.active = False

                    # check if NEXT button should become active
                    if(self.next_button.x <= event.pos[0] <= self.next_button.x + self.next_button.width
                       and self.next_button.y <= event.pos[1] <= self.next_button.y + self.next_button.height):
                        self.next_button.active = True
                    else:
                        self.next_button.active = False

                    # check if 'back to menu' button should become active
                    if(self.help_end_button.x <= event.pos[0] <= self.next_button.x + self.next_button.width
                       and self.help_end_button.y <= event.pos[1] <= self.help_end_button.y +
                       self.help_end_button.height):
                        self.help_end_button.active = True
                    else:
                        self.help_end_button.active = False

            elif(event.type == pygame.MOUSEBUTTONDOWN):
                # check if play is pressed
                if(self.play_button.active and self.state == const.START):
                    self.play_button.eventHandler()
                # check if retry is pressed
                elif(self.retry_button.active and (self.state == const.GAME_OVER or self.state == const.PAUSE)):
                    self.retry_button.eventHandler()
                # check if pause is pressed
                elif(self.pause_button.active and self.state == const.GAME):
                    self.pause_button.eventHandler()
                # check if resume is pressed
                elif(self.resume_button.active and self.state == const.PAUSE):
                    self.resume_button.eventHandler()
                # check if menu is pressed
                elif(self.menu_button.active and self.state == const.PAUSE):
                    self.menu_button.eventHandler()
                # check if help is pressed
                elif(self.help_button.active and self.state == const.START):
                    self.help_button.eventHandler()
                # check if prev is pressed
                elif(self.study_phase != 0 and self.prev_button.active and self.state == const.HELP):
                    self.prev_button.eventHandler()
                # check if next is pressed
                elif(self.study_phase != 2 and self.next_button.active and self.state == const.HELP):
                    self.next_button.eventHandler()
                # check if 'back to menu' is pressed
                elif(self.study_phase == 2 and self.help_end_button.active and self.state == const.HELP):
                    self.help_end_button.eventHandler()

            elif(event.type == pygame.KEYDOWN and self.state == const.GAME):
                # change position of active objet
                if(event.key == pygame.K_UP):
                    self.active.pos = (self.active.pos + 1) % 4
                # speeds down-movement of active object
                elif(event.key == pygame. K_DOWN):
                    self.y_speed = const.Y_SPEED_FAST
                # moves active object to the left
                elif(event.key == pygame.K_LEFT):
                    self.active.add_x(-1)
                    self.last_x_dif = -1
                # moves active object to the right
                elif(event.key == pygame.K_RIGHT):
                    self.active.add_x(1)
                    self.last_x_dif = 1

            # sets down-movementa of active object to normal
            elif(event.type == pygame.KEYUP and self.state == const.GAME):
                if(event.key == pygame.K_DOWN):
                    self.y_speed = const.Y_SPEED_SLOW - (self.scores[const.LEVEL] - 1) * 8

    def move_line(self, y, cnt):
        '''
        Moves one line of playing fielf down.

        Parameters
        ----------
        y : int
            y-coordinate of line we are moving.
        cnt : int
            How far down we're moving the line.
        '''

        for i in range(10):
            if((i, y) in self.ocuppied):
                if(self.ocuppied[(i, y)] == const.BLACK):
                    continue
        else:
            self.ocuppied[(i, y + cnt)] = self.ocuppied[(i, y)]
            del self.ocuppied[(i, y)]

    def full_lines(self):
        '''
        Checks, if there are new full lines (if so, removes them).

        Returns
        -------
        int
            Number of removes lines + index of topmost removed line.
        '''

        cnt = 0
        top_line = 42
        problem = -1

        tmp = self.active.get_active_blocks()

        # finds out, if there is a continuos lines
        for item in tmp:
            line_out = True

            for i in range(10):
                if((i, item[1]) not in self.ocuppied):
                    line_out = False
                    break

            if(not line_out):
                # if we don't remove this line, but line above was removed, we remember,
                # problem might occure
                if(cnt > 0):
                    problem = item[1]
                continue

            # else remove the line
            cnt += 1
            top_line = min(top_line, item[1])

            for i in range(10):
                del self.ocuppied[(i, item[1])]

            # if above current line is a problem line, we move the problem line down
            if(problem > 0):
                self.move_line(problem, 1)
                problem = -1

        return [cnt, top_line]

    def move_blocks(self, to_remove, count):
        '''
        Moves every block above removed lines down.
        '''

        if(count == 0):
            return

        i = to_remove

        while(i >= 0):
            for j in range(10):
                self.move_line(i, count)
            i -= 1

    def collision(self):
        '''
        Checks if active object didn't colide with other blocks or edges.
        Returns
        -------
        bool
            True if so, False otherwise.
        '''

        tmp = self.active.get_active_blocks()
        for item in tmp:
            if item in self.ocuppied:
                return True

        return False

    def loop(self):
        '''
        Main game loop.
        '''

        while(self.running):
            self.event_handler()

            # animation in 'How to play'
            if(self.state == const.HELP):
                # controls end of part of animation
                if(self.change[0] and (self.animation_counter - self.change[1] == 15)):
                    self.keys.set_all_black()
                    self.change[0] = False

                # handles falling of the object
                if(self.counter % self.y_speed == 0):
                    self.active.add_y(1)

                # first 'active event'
                if(self.animation_counter == 2*self.y_speed):
                    self.change[0] = True
                    self.change[1] = self.animation_counter

                    if(self.study_phase == 0):
                        self.active.add_x(1)
                        self.keys.set_color(3, const.RED)
                    elif(self.study_phase == 1):
                        self.active.pos = (self.active.pos + 1) % 4
                        self.keys.set_color(0, const.RED)
                    elif(self.study_phase == 2):
                        self.y_speed = const.Y_SPEED_FAST
                        self.keys.set_color(1, const.RED)

                # second 'active event'
                if(self.animation_counter == 4*self.y_speed):
                    self.change[0] = True
                    self.change[1] = self.animation_counter

                    if(self.study_phase == 0):
                        self.active.add_x(-1)
                        self.keys.set_color(2, const.RED)
                    elif(self.study_phase == 1):
                        self.active.pos = (self.active.pos + 1) % 4
                        self.keys.set_color(0, const.RED)

                # third 'active event'
                if(self.animation_counter == 5*self.y_speed):
                    self.change[0] = True
                    self.change[1] = self.animation_counter

                    if(self.study_phase == 0):
                        self.active.add_x(-1)
                        self.keys.set_color(2, const.RED)
                    elif(self.study_phase == 1):
                        self.active.pos = (self.active.pos + 1) % 4
                        self.keys.set_color(0, const.RED)

                # fourth 'active event'
                if(self.animation_counter == 7*self.y_speed):
                    self.change[0] = True
                    self.change[1] = self.animation_counter

                    if(self.study_phase == 0):
                        self.active.add_x(1)
                        self.keys.set_color(3, const.RED)
                    elif(self.study_phase == 1):
                        self.active.pos = (self.active.pos + 1) % 4
                        self.keys.set_color(0, const.RED)

                # controls, if object hit the bottom
                if(self.active.y > (const.HEIGHT//const.SQUARE)//2 - 1):
                    self.active.y = 0
                    self.active.x = 4
                    self.active.pos = 0
                    self.animation_counter = 0
                    self.change[0] = False
                    self.y_speed = const.Y_SPEED_DEMO
                    self.keys.set_all_black()

            # main game
            if(self.state == const.GAME):
                # checks if active object didn't hit ocuppied square (left-right direction)
                for i in range(2):
                    if(self.collision()):
                        self.active.add_x(-self.last_x_dif)

                if(self.counter % self.y_speed == 0):
                    self.active.add_y(1)

                # checks if active object didn't hit ocuppied square (down direction)
                if(self.collision()):
                    self.scores[const.SCORE] += 5
                    self.texts[const.T_SCORE].set_text(str(self.scores[const.SCORE]))

                    self.active.add_y(-1)

                    # checking if game can continue + add new ocuppied blocks
                    if(not self.active.add_active_blocks(self.ocuppied)):
                        self.texts[const.T_SCORE].set_text('')
                        self.texts[const.T_LINES].set_text('')
                        self.texts[const.T_LEVEL].set_text('')
                        self.state = const.GAME_OVER
                        for i in range(1, 4):
                            self.end_report[i].set_text('Final ' + self.left_banner[i-1] + ':' + str(self.scores[i-1]))

                        continue

                    cnt, top_line = self.full_lines()

                    self.scores[const.LINES] += cnt
                    self.texts[const.T_LINES].set_text(str(self.scores[const.LINES]))
                    self.scores[const.SCORE] += 50*cnt
                    self.texts[const.T_SCORE].set_text(str(self.scores[const.SCORE]))

                    self.move_blocks(top_line, cnt)

                    self.active = self.next1
                    self.active.set_cor(4, 0)

                    self.next1 = self.next2
                    self.next1.set_cor(const.NEXT1_X, const.NEXT1_Y)

                    self.next2 = self.next3
                    self.next2.set_cor(const.NEXT2_X, const.NEXT2_Y)

                    self.next3 = self.picker.pick(const.NEXT3_X, const.NEXT3_Y)

                    if(self.scores[const.SCORE] > self.scores[const.LEVEL] * 500 and self.scores[const.LEVEL <= 5]):
                        self.scores[const.LEVEL] += 1
                        self.texts[const.T_LEVEL].set_text(str(self.scores[const.LEVEL]))
                        self.y_speed -= 8

            self.draw_layout()

            pygame.display.update()

            self.counter += 1
            self.animation_counter += 1

            self.clock.tick(40)
