## @brief Constants used in other moudules.
## @author Jakub Šuráň

#game parameters
WIDTH = 1000
HEIGHT = 900
TEXT_SIZE = 50
SQUARE = WIDTH // 20
OFFSET = WIDTH // 4
Y_SPEED_SLOW = 40
Y_SPEED_FAST = 2
SCORE = 0
LINES = 1
LEVEL = 2
T_SCORE = 2
T_LINES = 5
T_LEVEL = 8
NEXT1_X = (WIDTH - 2*OFFSET) // SQUARE + (OFFSET // (2*SQUARE))
NEXT1_Y = ((HEIGHT // 3 - 2*TEXT_SIZE) // SQUARE)
NEXT2_X = (WIDTH - 2*OFFSET) // SQUARE + (OFFSET // (2*SQUARE))
NEXT2_Y = (WIDTH // (3*SQUARE)) + NEXT1_Y
NEXT3_X = (WIDTH - 2*OFFSET) // SQUARE + (OFFSET // (2*SQUARE))
NEXT3_Y = (2*WIDTH // (3*SQUARE)) - 2*TEXT_SIZE // SQUARE + NEXT1_Y 
START = 1
GAME = 2
GAME_OVER = 3
PAUSE = 4
HELP = 5
ER_WIDTH = 450
ER_HEIGHT = 400
LOGO_SIZE = 100
BUTTON_WIDTH = 170
BUTTON_HEIGHT = 75

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALMOST_BLACK = (40, 40, 40)
GRAY = (102, 102, 153)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_PURPLE = (128, 0,128)
LIGHT_PURPLE = (255,140, 222)
LIGHT_ORANGE = (255, 200, 0)
DARK_ORANGE = (255, 150, 0)
LIGHT_YELLOW = (255, 255, 153)
LIGHT_BLUE = (153, 204, 255)
