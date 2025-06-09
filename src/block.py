import pygame

from constants import *

class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0
        self.rotation = 0
        
    def rotate(self):
        """Rotate the block 90 degrees clockwise"""
        rows = len(self.shape)
        cols = len(self.shape[0])
        rotated = [[0 for _ in range(rows)] for _ in range(cols)]  # create a new rotated matrix rotated[cols][rows]
        for r in range(rows):
            for c in range(cols):
                rotated[c][rows -r - 1 ] = self.shape[r][c]
    
        return rotated

    def draw(self, surface):
        """Draw the block on the surface"""
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        GRID_OFFSET_X + (self.x + x) * BLOCK_SIZE,
                        GRID_OFFSET_Y + (self.y + y) * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE
                    )
                    pygame.draw.rect(surface, self.color, rect)
                    pygame.draw.rect(surface, WHITE, rect, 1)
            
    def move(self, dx, dy):
        """Move the block by dx and dy"""
        self.x += dx
        self.y += dy
    
    def get_position(self):
        """Get all position of the block"""
        positions = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    positions.append((self.x + x, self.y + y))
        print(positions)    
        return positions
    


    

        
