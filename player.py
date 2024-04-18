import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        # Load images for each direction and state
        self.images = {
            'left': {
                'lleg': pg.transform.scale(pg.image.load('./graphics/player/leftlleg.png').convert_alpha(), (64, 64)),
                'rleg': pg.transform.scale(pg.image.load('./graphics/player/leftrleg.png').convert_alpha(), (64, 64)),
                'idle': pg.transform.scale(pg.image.load('./graphics/player/leftidle.png').convert_alpha(), (64, 64))
            },
            'right': {
                'lleg': pg.transform.scale(pg.image.load('./graphics/player/rightlleg.png').convert_alpha(), (64, 64)),
                'rleg': pg.transform.scale(pg.image.load('./graphics/player/rightrleg.png').convert_alpha(), (64, 64)),
                'idle': pg.transform.scale(pg.image.load('./graphics/player/rightidle.png').convert_alpha(), (64, 64))
            },
            'up': {
                'lleg': pg.transform.scale(pg.image.load('./graphics/player/uplleg.png').convert_alpha(), (64, 64)),
                'rleg': pg.transform.scale(pg.image.load('./graphics/player/uprleg.png').convert_alpha(), (64, 64)),
                'idle': pg.transform.scale(pg.image.load('./graphics/player/upidle.png').convert_alpha(), (64, 64))
            },
            'down': {
                'lleg': pg.transform.scale(pg.image.load('./graphics/player/downlleg.png').convert_alpha(), (64, 64)),
                'rleg': pg.transform.scale(pg.image.load('./graphics/player/downrleg.png').convert_alpha(), (64, 64)),
                'idle': pg.transform.scale(pg.image.load('./graphics/player/downidle.png').convert_alpha(), (64, 64))
            }
        }
        
        self.currdir = 'right'
        self.direction = pg.math.Vector2()
        self.direction.x = 1  # Initial direction
        self.direction.y = 0
        self.state = 'idle'  # Initial state
        self.image = self.images[self.currdir][self.state]
        self.rect = self.image.get_rect(topleft=pos)
        
        # Other attributes
        self.base_speed = 6
        self.speed = self.base_speed
        self.obstacle_sprites = obstacle_sprites
        self.dodging = False
        self.dodge_speed = 12
        self.dodge_duration = 1000
        self.dodge_timer = 0
        self.state_timer = 0  # Timer for state switching
        self.state_interval = 250  # Interval for state switching in milliseconds
        self.hitbox = self.rect.inflate(0, -26)
        self.health = 40
        self.high = 40
        self.exp = 40

    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
            self.speed = self.base_speed * 1.5
        else:
            self.speed = self.base_speed
        
        # Determine direction based on pressed keys
        if keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
            self.direction.x = -1 if keys[pg.K_LEFT] else 1
            self.direction.y = 0
            self.currdir = 'left' if keys[pg.K_LEFT] else 'right'
            self.state = 'lleg' if self.state == 'idle' else self.state
        elif keys[pg.K_UP] or keys[pg.K_DOWN]:
            self.direction.x = 0
            self.direction.y = -1 if keys[pg.K_UP] else 1
            self.currdir = 'up' if keys[pg.K_UP] else 'down'
            self.state = 'lleg' if self.state == 'idle' else self.state
        else:
            self.direction.x = 0
            self.direction.y = 0
            if self.state != 'idle':  # Only reset the state if it's not already idle
                self.state = 'idle'

        if keys[pg.K_SPACE]:
            self.start_dodge()


    def start_dodge(self):
        self.dodging = True
        self.dodge_timer = pg.time.get_ticks()

    def update(self):
        self.input()

        if self.dodging:
            self.move(self.dodge_speed)
            if pg.time.get_ticks() - self.dodge_timer >= self.dodge_duration:
                self.dodging = False
        else:
            self.move(self.speed)

        # Check if it's time to switch the state (only if moving)
        if self.direction.x != 0 or self.direction.y != 0:
            if pg.time.get_ticks() - self.state_timer >= self.state_interval:
                self.state = 'lleg' if self.state == 'rleg' else 'rleg'
                self.state_timer = pg.time.get_ticks()

        # Update image based on direction and state
        self.image = self.images[self.currdir][self.state]
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, speed):
        self.rectify('x', speed)
        self.collision('horizontal')
        self.rectify('y', speed)
        self.collision('vertical')
        self.rect.center = self.hitbox.center
		
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

    def draw_health_meter(self, screen):
        health_bar_width = 100
        health_bar_height = 10
        health_bar = pygame.Rect(10, 10, health_bar_width, health_bar_height)
        pygame.draw.rect(screen, (255, 0, 0), health_bar)
        current_health = min(max(self.health, 0), 100)
        health_bar.width = health_bar_width * current_health / 100
        pygame.draw.rect(screen, (0, 255, 0), health_bar)

    def draw_high_o_meter(self, screen):
        high_o_meter_height = 10
        high_o_meter = pygame.Rect(10, 30, self.high_o_meter, high_o_meter_height)
        pygame.draw.rect(screen, (255, 0, 0), high_o_meter)

    def draw_exp_meter(self, screen):
        exp_meter_width = 100
        exp_meter_height = 10
        exp_meter = pygame.Rect(WIDTH - 110, 10, exp_meter_width, exp_meter_height)
        pygame.draw.rect(screen, (255, 255, 0), exp_meter)