# Screen size
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 600


FPS = 60

BLOCK_SIZE = 30 # pixels (size of each cell)

# Game settings
GRID_WIDTH = 10  # Number of squares in each columns
GRID_HEIGHT = 20 # Number of squares in each rows
GRID_OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH * BLOCK_SIZE - 200 ) // 2 # distance from left to right of the screen
GRID_OFFSET_Y = (SCREEN_HEIGHT - GRID_HEIGHT * BLOCK_SIZE + 100 ) // 2 # distance from top to bottom of the screen

# GRID_OFFSET_X = (400 - 10 * 30) // 2 = 150
# GRID_OFFSET_Y = (600 - 20 * 30) // 2 = 250



# Màu sắc
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

#  Các hình dạng của khối
SHAPES = [
    [[1, 1, 1, 1],
     [0, 0, 0, 0]],  #I
    
    [[1, 0, 0],
     [1, 1, 1]],  #J    
    
    [[0, 0, 1],
     [1, 1, 1]],  #L
    
    [[1, 1],
     [1, 1]],  #O
    
    [[0, 1, 0],
     [1, 1, 1]],  #T
    
    [[0, 1, 1],
     [1, 1, 0]],  #S
    
    [[1, 1, 0],
     [0, 1, 1]],  #Z
        
]

# Scoring
SCORE_PER_LINE = [0, 40, 100, 300, 1200]  # Points for 0, 1, 2, 3, 4 lines
LEVEL_UP_SCORE = 1000  # Score needed to level up

# Drop speed
DROP_INTERVAL = 500 
MIN_DROP_SPEED = 100
SPEED_INCREASE = 100  # Speed increase per level

