import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        self.displaySurf = pygame.display.get_surface()
        
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()
    
    def run(self):
        self.visible_sprites.draw(self.displaySurf)
    
    def create_map(self):
        for row_idx, row in enumerate(WORLD_MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILESIZE
                y = row_idx * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites])