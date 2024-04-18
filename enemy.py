import pygame
from settings import *
from basePlayer import BasePlayer
import os

class Enemy(BasePlayer):
    def __init__(self, pos, groups, obstacle_sprites, monster_info, damage_player):
        super().__init__(groups)
        self.sprite_type = 'enemy'
        
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites
        
        self.health = monster_info[0]
        self.exp = monster_info[1]
        self.speed = monster_info[2]
        self.attack_damage = monster_info[3]
        self.resistance = monster_info[4]
        self.attack_radius = monster_info[5]
        self.notice_radius = monster_info[6]
        
        self.animation = {
            'idle': [],
            'move': [],
            'attack': []
        }
        
        for animation in self.animation.keys():
            self.animation[animation] = [file for file in os.walk('./graphics/monsters/{animation}')[2]]
        
    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return (distance, direction)
