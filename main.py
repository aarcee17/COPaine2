import pygame
from settings import *
from level import Level
from level0 import Level0  # Import Level0 from level0.py
from levelf import Levelf
import math
import os
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
        self.outro = Levelf()
        self.music1 = os.path.join(os.path.dirname(__file__), "intologi/vibe.mp3")
        self.music3 = os.path.join(os.path.dirname(__file__), "intologi/vibe.mp3")
        self.music2 = os.path.join(os.path.dirname(__file__), "audio/main.mp3")

    def daddy(self):
        pygame.mixer.music.load(self.music1)  # Load background music
        pygame.mixer.music.play(-1)

        
        self.run_intro()  # Run the intro animation
        
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
                pygame.mixer.music.stop()
                self.run()

    def run_outro(self):
        running = True
        pygame.mixer.music.load(self.music3)  # Load background music
        pygame.mixer.music.play(-1)    
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.outro.next_slide()  # Move to the next slide on spacebar press
            
            self.screen.fill((0, 3, 54))  # Fill screen with black color
            
            # Apply the filter with a specific color (e.g., black) and transparency level (e.g., 128)
            apply_filter(self.screen, (22, 34, 54), 63)
            
            self.outro.run()  # Run the current slide of the outro animation
            pygame.display.update()
            self.clock.tick(FPS)
            if self.outro.is_complete():
                running = False
                pygame.mixer.music.stop()
                pygame.quit()  # Once outro is complete, close the game screen and exit

            
    def run(self):
        pygame.mixer.music.load(self.music2)  # Load background music
        pygame.mixer.music.play(-1)    
        runn = True
        # Load the base tile image
        base_tile = pygame.transform.scale(pygame.image.load("base.png"), (64, 64))
        base_tile_width, base_tile_height = base_tile.get_width(), base_tile.get_height()

        # Transition to the main game loop
        while runn:

            pygame.mixer.music.load(self.music3)  # Load background music
            pygame.mixer.music.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Clear the screen
            self.screen.fill((0, 0, 0))
            bhand = 30
            # Calculate the transparency using a sine function
            transparency = (math.sin(pygame.time.get_ticks()/(30000/bhand)) + 1) * 128  # Adjust speed with division

            # Create a surface to hold the tiled background
            tiled_background = pygame.Surface((WIDTH, HEIGHT))

            # Tile the background
            for y in range(0, HEIGHT, base_tile_height):
                for x in range(0, WIDTH, base_tile_width):
                    tiled_background.blit(base_tile, (x, y))

            # Apply transparency to the background image
            tiled_background.set_alpha(transparency)

            # Fill any remaining space on the right and bottom edges
            for y in range(HEIGHT - base_tile_height, HEIGHT, base_tile_height):
                tiled_background.blit(base_tile, (WIDTH - base_tile_width, y))

            for x in range(WIDTH - base_tile_width, WIDTH, base_tile_width):
                tiled_background.blit(base_tile, (x, HEIGHT - base_tile_height))

            self.screen.blit(tiled_background, (0, 0))  # Draw the tiled background
            self.level.run()  # Run the main game loop
            pygame.display.update()

            self.clock.tick(FPS)
            if self.level.is_complete():
                running = False
                pygame.mixer.music.stop()
                self.run_outro()




if __name__ == "__main__":
    game = Game()
    game.daddy()
