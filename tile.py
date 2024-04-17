import pygame
from settings import *
from debug import debug

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load(surface).convert_alpha(), (64, 64))
        self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        self.hitbox = self.rect.inflate(0,-10)