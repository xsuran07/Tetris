'''
Author(s): Jakub Šuráň

Implementation of button.
'''

import pygame
from pathlib import Path

from . import constants as const


class Button:
    '''
    Implementation of simle button - changes color when hovered, calls event handler when pressed
    '''

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
        self.size = self.height - 20
        self.font = pygame.font.Font(Path(__file__).parent / 'fonts' / 'UbuntuMono-Regular.ttf', self.size)

    def draw(self, display):
        '''
        Displays button on the screen (when button is hovered, it changes color)
        '''

        BLACK = (0, 0, 0)

        pygame.draw.rect(display, BLACK, (self.x, self.y, self.width, self.height))
        if(self.active):
            pygame.draw.rect(display, self.colorActive, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        else:
            pygame.draw.rect(display, self.color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))

        text = self.font.render(self.text, True, (0, 0, 0))
        display.blit(text, (self.x + (self.width - len(self.text)*self.size // 2) // 2, self.y + 10))

    def eventHandler(self):
        '''
        Perform given action when button is pressed
        '''

        self.handler()


class Keys:
    '''
    Representation of arraw keys for animation
    '''

    def __init__(self, x, y, fun, color=const.BLACK):
        self.x = x
        self.y = y
        self.fun = fun
        self.colors = [color, color, color, color]

    def set_all_black(self):
        for i in range(4):
            self.colors[i] = const.BLACK

    def set_color(self, num, color):
        '''
        Sets color of the chosen arrow
        '''

        self.colors[num] = color

    def draw(self):
        '''
        Draws all keys
        '''

        self.fun(self.x, self.y, const.WHITE, self.colors[0], 0)
        self.fun(self.x, self.y+const.SQUARE, const.WHITE, self.colors[1], 1)
        self.fun(self.x-const.SQUARE, self.y+const.SQUARE, const.WHITE, self.colors[2], 2)
        self.fun(self.x+const.SQUARE, self.y+const.SQUARE, const.WHITE, self.colors[3], 3)
