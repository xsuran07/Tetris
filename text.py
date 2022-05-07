'''
Author(s): Jakub Šuráň

Implementation of class for displaying text.
'''

import pygame
import constants as const


class Text:
    '''
    Class for displaying text.
    '''

    def __init__(self, text, x, y, color, screen, width, size, box=False, center=True):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.width = width
        self.box = box
        self.size = size
        self.font = pygame.font.SysFont("ubuntumono", self.size)
        self.center = center

    def draw(self):
        '''
        Displays given text.
        '''

        if(self.box):
            pygame.draw.rect(self.screen, const.ALMOST_BLACK, (self.x, self.y, self.width, self.size))

        start = 0
        end = 1
        i = 0

        # displays whole text
        while(end < len(self.text)):
            # finds part of the text which fits on one line(may be even whole text)
            while(self.width > (len(self.text[start: end])+1) * self.size//2 and end < len(self.text)):
                end += 1

            # handles case, when whole text doesn't fit on one line
            if(end < len(self.text)):
                original = end

                # finds last spase
                while(self.text[end] != " " and end > 0):
                    end -= 1

                # text doesn't include space - have to split some word
                if(end == 0):
                    end = original
                    tmp = self.font.render(self.text[start: end] + "-", True, self.color)
                    self.screen.blit(tmp, (self.x + self.width //
                                     2 - (len(self.text[start: end])+1)*self.size//4, self.y + i*self.size))
                # text  includes at least one space - it is easy to split text
                else:
                    padded = self.text[start: end] + " " * (2*self.width // self.size - len(self.text[start:end]))
                    tmp = self.font.render(padded, True, self.color)
                    self.screen.blit(tmp, (self.x + self.width // 2 - len(padded)*self.size//4, self.y + i*self.size))
                    end += 1
            # handles case, when whole text fits on one line
            else:
                # if chosen, centers text
                if(self.center):
                    tmp = self.font.render(self.text[start: end], True, self.color)
                    self.screen.blit(tmp, (self.x + self.width //
                                     2 - len(self.text[start: end])*self.size//4, self.y + i*self.size))
                # else pads text with spaces
                else:
                    padded = self.text[start: end] + " " * (2*self.width // self.size - len(self.text[start:end]))
                    tmp = self.font.render(padded, True, self.color)
                    self.screen.blit(tmp, (self.x + self.width // 2 - len(padded)*self.size//4, self.y + i*self.size))

            start = end
            end += 1
            i += 1

    def set_text(self, new_text):
        '''
        Sets new value to the text atribute.
        '''

        self.text = new_text


class Logo(Text):
    '''
    Class for displaying logo.
    '''

    def __init__(self, x, y, screen, width, size):
        super().__init__("TETRIS", x, y, const.BLACK, screen, width, size, box=False)

        self.color = [(255, 0, 0), (51, 204, 51), (0, 0, 255), (128, 0, 128), (255, 200, 0), (255, 150, 0)]

    def draw(self):
        '''
        Displays given logo.
        '''

        for i in range(len(self.text)):
            text = self.font.render(str(self.text[i]), True, self.color[i])
            self.screen.blit(text, (i * self.size//2 + self.x + self.width //
                             2 - len(self.text)*self.size // 4, self.y))
