import pygame
import random
import time
from pygame.locals import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed

class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

def spawn_fruits_and_bombs():
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    for x in range(2):
        # Spawn 5 batches
        for _ in range(20):
            # Spawn 5 fruits and 5 bombs in each batch
            fruit = Fruit()
            fruits.add(fruit)
            all_sprites.add(fruit)

            bomb = Bomb()
            bombs.add(bomb)
            all_sprites.add(bomb)

        yield all_sprites, fruits, bombs
        # time.sleep(4)
  # Wait for 4 seconds between batches

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Catch the Fruit")
    clock = pygame.time.Clock()

    basket = Basket()

    running = True
    score = 0
    
    while score < 10:
        batch_generator = spawn_fruits_and_bombs()
        for all_sprites, fruits, bombs in batch_generator:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if not running:
                break

            all_sprites.add(basket)

            score_font = pygame.font.SysFont(None, 36)

            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False

                screen.fill(WHITE)

                all_sprites.update()
                all_sprites.draw(screen)

                # Check for collisions between basket and fruits
                fruit_collisions = pygame.sprite.spritecollide(basket, fruits, True)
                for _ in fruit_collisions:
                    score += 10  # Increase score for catching fruit

                # Check for collisions between basket and bombs
                bomb_collisions = pygame.sprite.spritecollide(basket, bombs, True)
                for _ in bomb_collisions:
                    score -= 20  # Decrease score for catching bomb

                # Render score
                score_text = score_font.render("Score: {}".format(score), True, BLACK)
                screen.blit(score_text, (10, 10))

                # Check winning condition
                if score >= 10:
                    # Player wins
                    # pygame.quit()
                    return score

                pygame.display.flip()
                clock.tick(60)

    # pygame.quit()


if __name__ == "__main__":
    final_score = main()
    print("Final Score:", final_score)
