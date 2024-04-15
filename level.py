import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        self.displaySurf = pygame.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()

    def run(self):
        self.visible_sprites.draw(self.displaySurf)
        self.visible_sprites.update()
        debug(self.player.direction)
    
    def create_map(self):
        # Iterate over the indices of the rows
        for row_idx in range(len(WORLD_MAP)):
            row = WORLD_MAP[row_idx]  # Get the row
            
            # Iterate over the indices of the columns
            for col_idx in range(len(row)):
                col = row[col_idx]  # Get the column value
                
                # Calculate the position of the tile
                x = col_idx * TILESIZE
                y = row_idx * TILESIZE
                
                # Create a tile based on the value in the map
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'p':
                    # Create the player at this position
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width, self.half_height = self.display_surface.get_size()[0] // 2,self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('./graphics/test/wall.png').convert_alpha()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def calculate_offset(self, player_rect):
        self.offset.x = player_rect.centerx - self.half_width
        self.offset.y = player_rect.centery - self.half_height

    def draw_floor(self):
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

    def custom_draw(self, player):
        self.calculate_offset(player.rect)
        self.draw_floor()

        sorted_sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)
        for sprite in sorted_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
