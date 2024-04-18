import pygame as pg

class Weapon(pg.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player = player
        self.direction = player.currdir

        # graphic
        full_path = f'./graphics/player/sword/{self.direction}.png'
        self.image = pg.image.load(full_path).convert_alpha()
        
        # placement
        if self.direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pg.math.Vector2(0, 16))
        elif self.direction == 'left': 
            self.rect = self.image.get_rect(midright=player.rect.midleft + pg.math.Vector2(0, 16))
        elif self.direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pg.math.Vector2(-10, 0))
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pg.math.Vector2(-10, 0))
        
        self.attack_start_time = pg.time.get_ticks()

    def update(self):
        # Check if it's time to switch back to the player's normal image
        if pg.time.get_ticks() - self.attack_start_time >= 250:
            self.player.attacking = False  # Switch back to normal image
            self.kill()  # Remove the weapon sprite
