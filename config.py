SCREEN_SIZE = (600, 400)
DOT_SIZE = 20
COLUMNS = SCREEN_SIZE[0] / DOT_SIZE
ROWS = SCREEN_SIZE[1] / DOT_SIZE

FONT = "DejaVuSans"  # the only font supported by the app I used to code this
FONT_SIZE = 128

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (210, 20, 20)
ORANGE = (255, 117, 20)
YELLOW = (255, 255, 0)
LGREEN = (30, 205, 110)
DGREEN = (0, 175, 80)
CYAN = (80, 187, 162)
BLUE = (34, 113, 179)
PURPLE = (207, 52, 118)
PINK = (226, 53, 80)

FOOD_COLOURS = {0: PINK, 1: ORANGE, 2: BLUE}

# directions
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

# food types
NORMAL = 0
SHORT = 1
SLOW = 2

BASE_FPS = 7
MAX_FPS = 25
WALLS = 0
# walls modeds:
# 0 - no walls
# 1 - walls with gaps
# 2 - whole walls
