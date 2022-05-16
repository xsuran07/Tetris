#!/usr/bin/env python3

'''
Author(s): Jakub Šuráň

Main executable script of the whole game.
'''

import pygame

from tetris_sources.game import Game


if __name__ == '__main__':
    pygame.init()

    game = Game()
    game.loop()

    pygame.quit()
