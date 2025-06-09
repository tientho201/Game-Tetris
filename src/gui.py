import pygame
import time
import random
from block import Block
from board import Board
from constants import *

class GUI:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + 100, SCREEN_HEIGHT + 100  ))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        self.board = Board()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        
        self.current_block = self.new_block()
        self.next_block = self.new_block()
        
        self.fps = FPS
        self.last_drop_time = time.time()
        self.drop_speed = DROP_INTERVAL
        
    def new_block(self):
        """Create a new block"""
        shape_idx = random.randint(0, len(SHAPES) - 1)
        block = Block(SHAPES[shape_idx], COLORS[shape_idx])
        return block
    
    def lock_block(self):
        """Lock the current piece and create a new one"""
        self.board.merge_block(self.current_block)
        lines_cleared = self.board.clear_lines()
        if lines_cleared > 0:
            self.update_score(lines_cleared)

        # Tạo block mới ở y = 0
        self.current_block = self.next_block
        self.current_block.x = GRID_WIDTH // 2 - len(self.current_block.shape[0]) // 2
        self.current_block.y = 0

        if not self.board.is_valid_position(self.current_block):
         
            # Nếu tại y = 0 đã va chạm, di chuyển lên y = -1
            self.current_block.y = -1
            if not self.board.is_valid_position(self.current_block):
               
                # Nếu y = -1 cũng không hợp lệ => thật sự game over
                self.game_over = True
                return  
            else:
                # Nếu y = -1 hợp lệ => khóa luôn block ở vị trí này và game over
          
                self.game_over = True
                self.draw_block()

        self.next_block = self.new_block()
        self.last_drop_time = time.time()


    def draw_block(self):
        rect = pygame.Rect(
            GRID_OFFSET_X + (self.current_block.x ) * BLOCK_SIZE,
            GRID_OFFSET_Y + (self.current_block.y ) * BLOCK_SIZE,
            BLOCK_SIZE,
            BLOCK_SIZE
            )
        print(rect)
        pygame.draw.rect(self.screen, self.current_block.color, rect)
        pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def update_score(self, lines_cleared):
        """Update score and level based on lines cleared"""
        if lines_cleared > 0:
            self.score += SCORE_PER_LINE[lines_cleared] * self.level
            self.lines_cleared += lines_cleared
            self.level = self.lines_cleared // 10 + 1
            self.drop_speed = max(MIN_DROP_SPEED, 
                                DROP_INTERVAL - (self.level - 1) * SPEED_INCREASE)

    def handle_events(self):
        """Handle events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                if not self.paused and not self.game_over:
                    if event.key == pygame.K_LEFT:
                        self.current_block.move(-1,0)
                        if not self.board.is_valid_position(self.current_block):
                            self.current_block.move(1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.current_block.move(1, 0)
                        if not self.board.is_valid_position(self.current_block):
                            self.current_block.move(-1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.current_block.move(0,1)
                        if not self.board.is_valid_position(self.current_block):
                            self.current_block.move(0, -1)
                            self.lock_block()
                    elif event.key == pygame.K_UP:
                        rotated_shape = self.current_block.rotate()
                        original_shape = self.current_block.shape
                        self.current_block.shape = rotated_shape

                        if not self.board.is_valid_position(self.current_block):
                            # move left
                            self.current_block.move(-1, 0)
                            if self.board.is_valid_position(self.current_block):
                                pass  
                            else:
                                
                                self.current_block.move(-1, 0)
                                if self.board.is_valid_position(self.current_block):
                                    pass  
                                else:
                                   
                                    self.current_block.move(2, 0)  
                                    self.current_block.shape = original_shape

                    elif event.key == pygame.K_SPACE:
                        while self.board.is_valid_position(self.current_block):
                            self.current_block.move(0, 1)
                        self.current_block.move(0, -1)
                        self.lock_block()

        # Handle key hold for fast drop
        if not self.paused and not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                # Tăng tốc độ rơi khi giữ phím xuống
                self.drop_speed = max(MIN_DROP_SPEED, DROP_INTERVAL - (self.level - 1) * SPEED_INCREASE)
                self.current_block.move(0, 1)
                if not self.board.is_valid_position(self.current_block):
                    self.current_block.move(0, -1)
                    self.lock_block()
                self.last_drop_time = time.time()  # Reset drop timer when manually moving down
        return True

    def draw_game_over(self):
        # Draw game over or paused message
        if self.game_over:
            self.draw_message("GAME OVER")
            self.draw_message("Press R to reset", 50)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.reset_game()
        elif self.paused:
            self.draw_message("PAUSED")
            self.draw_message("Press P to resume", 50)
            keys = pygame.key.get_pressed()
            if not keys[pygame.K_p]:
                self.paused = False 

    def draw(self):
        """Draw the game"""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw game board
        self.board.draw(self.screen)
        
        # Draw current block (will be drawn even if partially outside screen)
        self.current_block.draw(self.screen)
 
        # Draw next piece preview
        preview_x = GRID_OFFSET_X + GRID_WIDTH * BLOCK_SIZE + 50
        preview_y = GRID_OFFSET_Y + 50
        next_block = self.next_block
        next_block.x = preview_x // BLOCK_SIZE + 1
        next_block.y = preview_y // BLOCK_SIZE + 0.1
        next_block.draw(self.screen)
        
        # Draw preview box
        pygame.draw.rect(self.screen, WHITE, (preview_x, preview_y + 10, BLOCK_SIZE * 4 + 50, BLOCK_SIZE * 4), 3)
        
        # Draw score and level
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        pause_text = self.font.render(f"Press P to resume", True, WHITE)
        self.screen.blit(score_text, (preview_x, preview_y + 150))
        self.screen.blit(level_text, (preview_x, preview_y + 200))
        self.screen.blit(pause_text, (preview_x, preview_y + 250))
        
        self.draw_game_over()
        # Update display
        pygame.display.flip()
        
    def draw_message(self, message, y_offset=0):
        """Draw a message on the screen"""
        text = self.font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
        self.screen.blit(text, text_rect)
    
    def reset_game(self):
        self.board = Board()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.current_block = self.new_block()
        self.next_block = self.new_block()
        self.last_drop_time = time.time()
        self.drop_speed = DROP_INTERVAL
        
    def run(self):
        """Run the game"""
        running = True
        while running:
            running = self.handle_events()
            
            if not self.game_over and not self.paused:
                current_time = time.time()
                # Tính toán tốc độ rơi dựa trên level
                self.drop_speed = max(MIN_DROP_SPEED, 
                                    DROP_INTERVAL - (self.level - 1) * SPEED_INCREASE)          
                if current_time - self.last_drop_time > self.drop_speed / 1000:
                    self.current_block.move(0, 1)
                    if not self.board.is_valid_position(self.current_block):
                        self.current_block.move(0, -1)
                        self.lock_block()
                    self.last_drop_time = current_time
            
            self.draw()
            self.clock.tick(self.fps)  # limits FPS to 60
            # Nếu game over ⇒ cho delay 1-2s rồi thoát game
        pygame.quit()
                
            