import pygame
from settings import *
from level0 import Level0
import main  # Import main.py

class Intro:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Trippy Adventure Intro")
        self.clock = pygame.time.Clock()
        self.level0 = Level0()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level0.next_slide()  # Move to the next slide on spacebar press
            
            self.screen.fill((0, 0, 0))  # Fill screen with black color
            self.level0.run()  # Run the current slide of the intro animation
            pygame.display.update()
            self.clock.tick(FPS)

            # If the intro animation is complete, transition to main.py
            if self.level0.is_complete():
                
                pygame.quit()
                main.main()  # Call the main function from main.py

if __name__ == "__main__":
    intro = Intro()
    intro.run()
