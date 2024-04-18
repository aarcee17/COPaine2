import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 50

# Set up the screen

# Font
font = pygame.font.Font(None, FONT_SIZE)

# Board
board = [['' for _ in range(3)] for _ in range(3)]

# Function to draw the grid lines
def draw_grid(screen):
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SCREEN_HEIGHT // 3), (SCREEN_WIDTH, i * SCREEN_HEIGHT // 3), 2)
        pygame.draw.line(screen, LINE_COLOR, (i * SCREEN_WIDTH // 3, 0), (i * SCREEN_WIDTH // 3, SCREEN_HEIGHT), 2)

# Function to draw X or O on the board
def draw_board(screen):
    for row in range(3):
        for col in range(3):
            center_x = col * SCREEN_WIDTH // 3 + SCREEN_WIDTH // 6
            center_y = row * SCREEN_HEIGHT // 3 + SCREEN_HEIGHT // 6
            if board[row][col] == 'X':
                text_surface = font.render('X', True, LINE_COLOR)
                text_rect = text_surface.get_rect(center=(center_x, center_y))
                screen.blit(text_surface, text_rect)
            elif board[row][col] == 'O':
                text_surface = font.render('O', True, LINE_COLOR)
                text_rect = text_surface.get_rect(center=(center_x, center_y))
                screen.blit(text_surface, text_rect)

# Function to check for a winner
def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Function to check if the board is full
def is_board_full():
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

# Function to make the computer's move
def computer_move():
    available_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == '']
    if available_cells:
        row, col = random.choice(available_cells)
        board[row][col] = 'O'

def main():
# Main game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    running = True
    current_player = 'X'

    while running:
        screen.fill(WHITE)
        draw_grid(screen)
        draw_board(screen)
        pygame.display.flip()

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 'X':
                x, y = pygame.mouse.get_pos()
                col = x // (SCREEN_WIDTH // 3)
                row = y // (SCREEN_HEIGHT // 3)
                if board[row][col] == '':
                    board[row][col] = 'X'
                    current_player = 'O'

        winner = check_winner()
        if winner:
            print(f"Player {winner} wins!")
            running = False
        elif is_board_full():
            print("It's a tie!")
            running = False

        # Computer's move
        if current_player == 'O' and running:
            computer_move()
            current_player = 'X'
    return True if winner and winner == 'X' else False


# Quit Pygame
if __name__ == "__main__":
    main()
