import pygame as pg
from settings import *
from debug import debug

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type=None, surface=pg.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface

        position_functions = {
            'object': self.calculate_object_position
 
        }

        position_function = position_functions.get(sprite_type, self.calculate_default_position)
        self.rect = position_function(pos)

        self.hitbox = self.rect.inflate(0, -10)
    
    def calculate_object_position(self, pos):
        return self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
    
    def calculate_default_position(self, pos):
        return self.image.get_rect(topleft=pos)
