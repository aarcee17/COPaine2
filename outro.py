import pygame
from settings import *
from levelf import Levelf
import main  # Import main.py

class Outro:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The vision")
        self.clock = pygame.time.Clock()
        self.levelf = Levelf()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.levelf.next_slide()  # Move to the next slide on spacebar press
            
            self.screen.fill((0, 0, 0))  # Fill screen with black color
            self.levelf.run()  # Run the current slide of the outro animation
            pygame.display.update()
            self.clock.tick(FPS)

            # If the outro animation is complete, transition to main.py
            if self.levelf.is_complete():
                
                pygame.quit()


if __name__ == "__main__":
    outro = Outro()
    outro.run()
