import pygame
from math import cos, pi

class BasePlayer(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.frame_idx = 0
        self.animation_speed = 0.15
        
    def move(self, speed):
        self.rectify('x', speed)
        self.collision('horizontal')
        self.rectify('y', speed)
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        if self.rect.center[0] < 0:
            self.rect.center = (0, self.rect.center[1])
        elif self.rect.center[0] > 3200:
            self.rect.center = (3200, self.rect.center[1])
        if self.rect.center[1] < -50:
            self.rect.center = (self.rect.center[0], -50)
        elif self.rect.center[1] > 1500:
            self.rect.center = (self.rect.center[0], 1500)
        self.hitbox.center = self.rect.center
        
    def rectify(self, axis, speed):
        if axis == 'x':
            self.hitbox.x += self.direction.x * speed
        if axis == 'y':
            self.hitbox.y += self.direction.y * speed
    
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom
    
    def phase(self):
        value = cos(pi/2 - pygame.time.get_ticks())
        if value >= 0: 
            return 255
        else: 
            return 0