import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.transform.scale(pg.image.load('./graphics/test/player.png').convert_alpha(), (64, 64))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pg.math.Vector2()
        self.base_speed = 1.5  # Define the base speed
        self.speed = self.base_speed  # Set the initial speed to the base speed
        self.obstacle_sprites = obstacle_sprites
        self.dodging = False
        self.dodge_speed = 5  # Define the dodge speed
        self.dodge_duration = 100  # Duration of the dodge in milliseconds
        self.dodge_timer = 0  # Timer to track dodge duration

    def input(self):
        keys = pg.key.get_pressed()
        # Check if shift is pressed to adjust speed
        if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
            self.speed = self.base_speed * 1.5  # Double the speed
        else:
            self.speed = self.base_speed  # Reset speed to base speed
        
        # Set the direction based on the pressed keys
        self.direction.y = -1 if keys[pg.K_UP] else (1 if keys[pg.K_DOWN] else 0)
        self.direction.x = -1 if keys[pg.K_LEFT] else (1 if keys[pg.K_RIGHT] else 0)

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # Check if space is pressed to initiate dodge
        if keys[pg.K_SPACE]:
            self.start_dodge()

    def start_dodge(self):
        self.dodging = True
        self.dodge_timer = pg.time.get_ticks()

    def update(self):
        self.input()

        # If dodging, move at dodge speed
        if self.dodging:
            self.move(self.dodge_speed)
            # Check if dodge duration is over
            if pg.time.get_ticks() - self.dodge_timer >= self.dodge_duration:
                self.dodging = False
        else:
            self.move(self.speed)

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Move horizontally and check collision
        self.rectify('x', speed)
        self.collision('horizontal')

        # Move vertically and check collision
        self.rectify('y', speed)
        self.collision('vertical')
        self.rect.center = self.hitbox.center
		

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom
    
    def collision(self, direction):
        for sprite in self.obstacle_sprites:
            if self.rect.colliderect(sprite.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0:  # Moving right
                        self.rect.right = min(self.rect.right, sprite.rect.left)
                    elif self.direction.x < 0:  # Moving left
                        self.rect.left = max(self.rect.left, sprite.rect.right)
                elif direction == 'vertical':
                    if self.direction.y > 0:  # Moving down
                        self.rect.bottom = min(self.rect.bottom, sprite.rect.top)
                    elif self.direction.y < 0:  # Moving up
                        self.rect.top = max(self.rect.top, sprite.rect.bottom)

    def update(self):
        self.input()
        self.move(self.speed)
       