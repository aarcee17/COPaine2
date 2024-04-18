import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 4
TILE_SIZE = 100
PADDING = 10
SCREEN_WIDTH = GRID_SIZE * (TILE_SIZE + PADDING) + PADDING
SCREEN_HEIGHT = GRID_SIZE * (TILE_SIZE + PADDING) + PADDING
FONT_SIZE = 36
WINNING_TILE = 64

# Colors
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Helper functions
def draw_text(surface, text, color, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def move_and_generate(grid, direction):
    if direction == "left":
        new_grid = move_left(grid)
    elif direction == "right":
        new_grid = move_right(grid)
    elif direction == "up":
        new_grid = move_up(grid)
    elif direction == "down":
        new_grid = move_down(grid)
    else:
        return grid, False  # Invalid direction
    
    if new_grid != grid:  # Check if the grid changed after the move
        add_new_tile(new_grid)
        return new_grid, True
    else:
        return grid, False  # No new tile generated

def draw_grid(surface):
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(surface, (0, 0, 0), (i * (TILE_SIZE + PADDING) + PADDING, PADDING),
                         (i * (TILE_SIZE + PADDING) + PADDING, SCREEN_HEIGHT - PADDING))
        pygame.draw.line(surface, (0, 0, 0), (PADDING, i * (TILE_SIZE + PADDING) + PADDING),
                         (SCREEN_WIDTH - PADDING, i * (TILE_SIZE + PADDING) + PADDING))

def draw_tile(surface, value, row, col):
    color = TILE_COLORS.get(value, (255, 255, 255))
    rect = pygame.Rect(col * (TILE_SIZE + PADDING) + PADDING, row * (TILE_SIZE + PADDING) + PADDING, TILE_SIZE,
                       TILE_SIZE)
    pygame.draw.rect(surface, color, rect)
    draw_text(surface, str(value), (0, 0, 0), FONT_SIZE, rect.centerx, rect.centery)

def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = 2  # New tile is always 2 or 4 (90% chance of 2, 10% chance of 4)

def merge_tiles(row):
    merged_row = []
    skip_next = False
    for i in range(len(row)):
        if skip_next:
            skip_next = False
            continue
        if i < len(row) - 1 and row[i] == row[i + 1]:
            merged_row.append(row[i] * 2)
            skip_next = True
        else:
            merged_row.append(row[i])
    while len(merged_row) < len(row):
        merged_row.append(0)
    return merged_row

def move_left(grid):
    new_grid = []
    for row in grid:
        new_row = merge_tiles([val for val in row if val != 0])
        new_row += [0] * (GRID_SIZE - len(new_row))
        new_grid.append(new_row)
    return new_grid

def move_right(grid):
    reversed_grid = [row[::-1] for row in grid]
    new_grid = []
    for row in reversed_grid:
        new_row = merge_tiles([val for val in row if val != 0])
        new_row += [0] * (GRID_SIZE - len(new_row))
        new_grid.append(new_row[::-1])
    return new_grid

def move_up(grid):
    transposed_grid = list(map(list, zip(*grid)))
    new_grid = []
    for row in transposed_grid:
        new_row = merge_tiles([val for val in row if val != 0])
        new_row += [0] * (GRID_SIZE - len(new_row))
        new_grid.append(new_row)
    new_grid = list(map(list, zip(*new_grid)))
    return new_grid

def move_down(grid):
    transposed_grid = list(map(list, zip(*grid)))
    new_grid = []
    for row in transposed_grid:
        new_row = merge_tiles([val for val in row[::-1] if val != 0])[::-1]
        new_row += [0] * (GRID_SIZE - len(new_row))
        new_grid.append(new_row)
    if new_grid != transposed_grid:
        add_new_tile(new_grid)
    return list(map(list, zip(*new_grid)))

def check_win(grid):
    for row in grid:
        for value in row:
            if value >= WINNING_TILE:
                return True
    return False

def main():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_new_tile(grid)
    add_new_tile(grid)

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Weird 2048(64)")

    # Main game loop
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Handle events
        moved = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not moved:
                if event.key == pygame.K_LEFT:
                    grid, moved = move_and_generate(grid, "left")
                elif event.key == pygame.K_RIGHT:
                    grid, moved = move_and_generate(grid, "right")
                elif event.key == pygame.K_UP:
                    grid, moved = move_and_generate(grid, "up")
                elif event.key == pygame.K_DOWN:
                    grid, moved = move_and_generate(grid, "down")
                if moved and check_win(grid):
                    print("You win!")
                    running = False

        # Draw the grid and tiles
        draw_grid(screen)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                draw_tile(screen, grid[i][j], i, j)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    # pygame.quit()
if __name__ == "__main__":
    main()