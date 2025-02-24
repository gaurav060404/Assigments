import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Game dimensions
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 8)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.fall_speed = 1000  # milliseconds
        self.last_fall = pygame.time.get_ticks()

    def new_piece(self):
        # Choose a random shape
        shape_idx = random.randint(0, len(SHAPES) - 1)
        return {
            'shape': SHAPES[shape_idx],
            'color': COLORS[shape_idx],
            'x': GRID_WIDTH // 2 - len(SHAPES[shape_idx][0]) // 2,
            'y': 0
        }

    def valid_move(self, piece, x_offset=0, y_offset=0):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece['x'] + x + x_offset
                    new_y = piece['y'] + y + y_offset
                    if (new_x < 0 or new_x >= GRID_WIDTH or 
                        new_y >= GRID_HEIGHT or 
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True

    def rotate_piece(self):
        # Create a new rotated shape
        rows = len(self.current_piece['shape'])
        cols = len(self.current_piece['shape'][0])
        rotated = [[self.current_piece['shape'][rows-1-j][i] 
                   for j in range(rows)] for i in range(cols)]
        
        old_shape = self.current_piece['shape']
        self.current_piece['shape'] = rotated
        
        # If rotation is invalid, revert back
        if not self.valid_move(self.current_piece):
            self.current_piece['shape'] = old_shape

    def merge_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = self.current_piece['color']

    def clear_lines(self):
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if all(self.grid[y]):
                lines_cleared += 1
                # Move all lines above down
                for move_y in range(y, 0, -1):
                    self.grid[move_y] = self.grid[move_y - 1][:]
                self.grid[0] = [0] * GRID_WIDTH
            else:
                y -= 1
        
        # Update score and level
        if lines_cleared:
            self.score += (lines_cleared * 100) * self.level
            self.level = self.score // 1000 + 1
            self.fall_speed = max(100, 1000 - (self.level * 50))

    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x],
                                  (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                                   BLOCK_SIZE - 1, BLOCK_SIZE - 1))
        
        # Draw current piece
        if self.current_piece:
            for y, row in enumerate(self.current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, self.current_piece['color'],
                                      ((self.current_piece['x'] + x) * BLOCK_SIZE,
                                       (self.current_piece['y'] + y) * BLOCK_SIZE,
                                       BLOCK_SIZE - 1, BLOCK_SIZE - 1))
        
        # Draw score and level
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        level_text = font.render(f'Level: {self.level}', True, WHITE)
        self.screen.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 10, 10))
        self.screen.blit(level_text, (GRID_WIDTH * BLOCK_SIZE + 10, 50))
        
        if self.game_over:
            game_over_text = font.render('Game Over!', True, WHITE)
            self.screen.blit(game_over_text, 
                           (GRID_WIDTH * BLOCK_SIZE + 10, 100))
        
        pygame.display.flip()

    def run(self):
        while not self.game_over:
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.valid_move(self.current_piece, x_offset=-1):
                            self.current_piece['x'] -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_move(self.current_piece, x_offset=1):
                            self.current_piece['x'] += 1
                    elif event.key == pygame.K_DOWN:
                        if self.valid_move(self.current_piece, y_offset=1):
                            self.current_piece['y'] += 1
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()
                    elif event.key == pygame.K_SPACE:
                        # Hard drop
                        while self.valid_move(self.current_piece, y_offset=1):
                            self.current_piece['y'] += 1
            
            # Handle automatic falling
            if current_time - self.last_fall > self.fall_speed:
                if self.valid_move(self.current_piece, y_offset=1):
                    self.current_piece['y'] += 1
                else:
                    self.merge_piece()
                    self.clear_lines()
                    self.current_piece = self.new_piece()
                    if not self.valid_move(self.current_piece):
                        self.game_over = True
                self.last_fall = current_time
            
            self.draw()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Tetris()
    game.run()
    pygame.quit()