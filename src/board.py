import pygame

from block import Block
from constants import *

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # matrix[y][x]
        self.colors = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    
    def is_valid_position(self, blocks):
        """Check if the piece can be placed on the board"""
        for x, y in blocks.get_position():
            if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or (y >= 0 and self.grid[y][x] != 0): 
                return False
        return True
    
    def merge_block(self, block):
        """Merge the block on the board"""
        for x, y in block.get_position():
            if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                self.grid[y][x] = block.color
                self.colors[y][x] = block.color
 
    def clear_lines(self):
        """Clear the lines that are full"""
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if all(self.grid[y]): # check if the line is full
                lines_cleared += 1
                # Move all lines above down
                for y_clear in range(y, 0, -1):
                    self.grid[y_clear] = self.grid[y_clear - 1][:]
                    self.colors[y_clear] = self.colors[y_clear - 1][:]
                # Clear top line
                self.grid[0] = [0] * GRID_WIDTH
                self.colors[0] = [BLACK] * GRID_WIDTH
            else:
                y -= 1
        return lines_cleared
    
    def is_game_over(self):
        """Check if the game is over"""
        return any(self.grid[0])
    
    def draw(self, screen):
        """Draw the board on the screen"""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(
                    GRID_OFFSET_X + x * BLOCK_SIZE,
                    GRID_OFFSET_Y + y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
                pygame.draw.rect(screen, self.colors[y][x], rect)
                pygame.draw.rect(screen, GRAY, rect, 1)
        
        pygame.draw.rect(
            screen,
            GRAY, 
                (
                GRID_OFFSET_X,
                GRID_OFFSET_Y,
                GRID_WIDTH * BLOCK_SIZE,
                GRID_HEIGHT * BLOCK_SIZE
            ),
            3
        )
        
