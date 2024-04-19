import pygame
from settings import *
from basePlayer import BasePlayer
from math import log10

class Enemy(BasePlayer):
    def __init__(self, pos, groups, obstacle_sprites, monster_info, damage_player, type):
        super().__init__(groups)
        self.sprite_type = 'enemy'
        
        self.animation = {'simple':{
            'idle': ['./graphics/monsters/idle/0.png'],
            'move': ['./graphics/monsters/move/1.png', './graphics/monsters/move/2.png', './graphics/monsters/move/3.png', './graphics/monsters/move/2.png'],
            'attack': ['./graphics/monsters/attack/0 copy.png'],
            'speed': 3,
            'damage': 4
        },
        'wizard':{
            'idle': ['./graphics/monsters/wizard/0.png'],
            'move': ['./graphics/monsters/wizard/5.png', './graphics/monsters/wizard/6.png', './graphics/monsters/wizard/7.png', './graphics/monsters/wizard/8.png', './graphics/monsters/wizard/9.png'],
            'attack': ['./graphics/monsters/wizard/1.png'],
            'speed': 4,
            'damage': 12
        },
        'spider' : {
            'idle': ['./graphics/monsters/spider/0.png'],
            'move': ['./graphics/monsters/spider/0.png'],
            'attack': ['./graphics/monsters/spider/0.png'],
            'speed': 5,
            'damage': 5
        },
        'racoon' : {
            'idle': ['./graphics/monsters/racoon/idle/0.png', './graphics/monsters/racoon/idle/1.png', './graphics/monsters/racoon/idle/2.png', './graphics/monsters/racoon/idle/3.png', './graphics/monsters/racoon/idle/4.png', './graphics/monsters/racoon/idle/5.png'],
            'move': ['./graphics/monsters/racoon/move/0.png', './graphics/monsters/racoon/move/1.png', './graphics/monsters/racoon/move/2.png', './graphics/monsters/racoon/move/3.png', './graphics/monsters/racoon/move/4.png'],
            'attack': ['./graphics/monsters/racoon/attack/0.png', './graphics/monsters/racoon/attack/1.png', './graphics/monsters/racoon/attack/2.png', './graphics/monsters/racoon/attack/3.png'],
            'speed': 2,
            'damage': 20
        },
        }
        self.attack_damage = self.animation[type]['damage']
        self.speed = self.animation[type]['speed']
        self.status = 'idle'
        self.type = type
        self.image = pygame.image.load(self.animation[self.type][self.status][self.frame_idx], 'rb').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites
        self.hurtsound = pygame.mixer.Sound("audio/sword.wav")
        self.health = monster_info[0]
        self.exp = monster_info[1]
        self.resistance = monster_info[2]
        self.attack_radius = monster_info[3]
        self.notice_radius = monster_info[4]
        self.can_attack = True
        self.vulnerable = True
        self.attack_time = 0
        self.attack_cooldown = 500
        self.invincibility_duration = 300
        
        self.damage_player = damage_player
        
    def determine_player_distance_direction(self, player):
        enemy_pos = pygame.math.Vector2(self.rect.center)
        player_pos = pygame.math.Vector2(player.rect.center)
        distance = (player_pos - enemy_pos).magnitude()
        if distance > 0:
            direction = (player_pos - enemy_pos).normalize()
        else:
            direction = pygame.math.Vector2()
        return (distance, direction)

    def determine_status(self, player):
        distance = self.determine_player_distance_direction(player)[0]
        print("Distance: ", distance)
        print("Attack radius: ", self.attack_radius)
        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_idx = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def perform_actions(self, player):
        if self.status == 'attack' and self.can_attack:
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage)
            self.can_attack = False
        elif self.status == 'move':
            self.direction = self.determine_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate_movement(self):
        animation = self.animation[self.type][self.status]
        print(animation)
        self.frame_idx += self.animation_speed
        if self.frame_idx >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_idx = 0
        self.image = pygame.image.load(animation[int(self.frame_idx)], 'rb').convert_alpha()
        self.rect = self.image.get_rect(center=self.hitbox.center)
        if not self.vulnerable:
            alpha = self.phase()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def handle_cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def receive_damage(self, player, exp):
        if self.vulnerable:
            self.direction = self.determine_player_distance_direction(player)[1]
            self.hurtsound.play()
            print("Enemy hit and got damage")
            self.health -= 2*log10(exp) + 5
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def verify_death(self):
        if self.health <= 0:
            self.kill()
            self.image = pygame.image.load('./graphics/monsters/trans.png', 'rb').convert_alpha()

    def react_to_hit(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update_status(self):
        self.react_to_hit()
        self.move(self.speed)
        self.animate_movement()
        self.handle_cooldowns()
        self.verify_death()

    def update_enemy(self, player):
        print("Updating enemy")
        self.determine_status(player)
        self.perform_actions(player)
        self.update_status()
