import pygame

class Level:
    def __init__(self):
        self.displaySurf = pygame.display.get_surface()
        
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
    
    def run(self):
        pass