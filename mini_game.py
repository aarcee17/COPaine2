import pygame
import random
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
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

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

def spawn_fruit():
    fruit = Fruit()
    all_sprites.add(fruit)
    fruits.add(fruit)

def spawn_bomb():
    bomb = Bomb()
    all_sprites.add(bomb)
    bombs.add(bomb)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Catch the Fruit")
    clock = pygame.time.Clock()

    basket = Basket()
    all_sprites.add(basket)

    score = 0
    running = True
    fruit_timer = 0
    bomb_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Spawn fruit every 0.5 seconds
        fruit_timer += clock.get_rawtime()
        if fruit_timer >= 150:
            spawn_fruit()
            fruit_timer = 0

        # Spawn bomb every 2 seconds
        bomb_timer += clock.get_rawtime()
        if bomb_timer >= 500:
            spawn_bomb()
            bomb_timer = 0

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
        score_font = pygame.font.SysFont(None, 36)
        score_text = score_font.render("Score: {}".format(score), True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

        # Check winning condition
        if score >= 60:
            running = False

    pygame.quit()
    return score

if __name__ == "__main__":
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    final_score = main()
    print("Final Score:", final_score)
