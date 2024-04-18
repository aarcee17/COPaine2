import pygame
from settings import *
from level import Level
from level0 import Level0  # Import Level0 from level0.py

def apply_filter(screen, filter_color, alpha):
    filter_surface = pygame.Surface(screen.get_size())  # Create a surface with the same size as the screen
    filter_surface.set_alpha(alpha)  # Set the transparency level of the filter surface
    filter_surface.fill(filter_color)  # Fill the filter surface with the filter color
    screen.blit(filter_surface, (0, 0))  # Blit the filter surface onto the screen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("COPaine")
        self.clock = pygame.time.Clock()
        self.level = Level()  # Initialize the main game level
        self.intro = Level0()  # Initialize the intro animation level

    def run_intro(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.intro.next_slide()  # Move to the next slide on spacebar press
            
            self.screen.fill((0, 3, 54))  # Fill screen with black color
            
            # Apply the filter with a specific color (e.g., black) and transparency level (e.g., 128)
            apply_filter(self.screen, (22, 34, 54), 63)
            
            self.intro.run()  # Run the current slide of the intro animation
            pygame.display.update()
            self.clock.tick(FPS)

            # If the intro animation is complete, transition to the main game loop
            if self.intro.is_complete():
                running = False

    def run(self):
        self.run_intro()  # Run the intro animation
        # Transition to the main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.screen.fill((0, 0, 0))  # Fill screen with black color
            self.level.run()  # Run the main game loop
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
