import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
import pandas as pd
import os
def import_csv_layout(path):
    terrain_map = pd.read_csv(path, header=None).astype(str).values.tolist()
    return terrain_map

class Level:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.weapon_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		layouts = {
			'base': import_csv_layout('./map/DrugMap_Base.csv'),
			'road': import_csv_layout('./map/DrugMap_Roads.csv'),
			'homes': import_csv_layout('./map/DrugMap_Homes.csv')
		}
		mapItems = {
			'1057': ['./CityTiles/(1,16).png','no'],
			'604': ['./graphics/test/cover.jpeg','no'],
			'940': ['./graphics/test/road.png','no'],
			'1295': ['./CityTiles/(40,20).png', 'no'],
			'401': ['./CityTiles/(6,5).png'],
			'1084': ['./CityTiles/(2,3).png'],
			'4': ['./Machine/(4,0).png'],
			'5': ['./Machine/(5,0).png'],
			'12': ['./Machine/(4,1).png'],
			'13': ['./Machine/(5,1).png'],
			'20': ['./Machine/(4,2).png'],
			'21': ['./Machine/(5,2).png'],
			'28': ['./Machine/(4,3).png'],
			'29': ['./Machine/(5,3).png'],
			'203': ['./CityTiles/(5,3).png'],
			'823': ['./CityTiles/(31,12).png'],
			'824': ['./CityTiles/(32,12).png'],
			'889': ['./CityTiles/(31,13).png'],
			'890': ['./CityTiles/(32,13).png'],
			'1326': ['./CityTiles/(0,7).png', 'no'],
			'1004': ['./CityTiles/(0,7).png', 'no'],
			'1077': ['./CityTiles/(21,16).png'],
			'1078': ['./CityTiles/(22,16).png'],
			'1079': ['./CityTiles/(23,16).png'],
			'1080': ['./CityTiles/(24,16).png'],
			'1204': ['./CityTiles/(16,18).png'],
			'1270': ['./CityTiles/(16,19).png'],
			'925': ['./CityTiles/(0,7).png'],
			'1200': ['./CityTiles/(12,18).png'],
			'1201': ['./CityTiles/(13,18).png'],
			'1202': ['./CityTiles/(14,18).png'],
			'1203': ['./CityTiles/(15,18).png'],
			'1266': ['./CityTiles/(12,19).png'],
			'1267': ['./CityTiles/(13,19).png'],
			'1268': ['./CityTiles/(14,19).png'],
			'1269': ['./CityTiles/(15,19).png'],
			'927': ['./CityTiles/(3,14).png'],
			'67': ['./CityTiles/(1,1).png'],
			'68': ['./CityTiles/(2,1).png'],
			'475': ['./CityTiles/(13,7).png'],
			'541': ['./CityTiles/(13,8).png'],
			'2': ['./Machine/(2,0).png'],
			'3': ['./Machine/(3,0).png'],
			'10': ['./Machine/(2,1).png'],
			'11': ['./Machine/(3,1).png'],
			'18': ['./Machine/(2,2).png'],
			'19': ['./Machine/(3,2).png'],
			'26': ['./Machine/(2,3).png'],
			'27': ['./Machine/(3,3).png'],
			'599': ['./CityTiles/(5,9).png', 'no'],
			'680': ['./CityTiles/(20,10).png'],
			'36': ['./Machine/(6,4).png'],
			'37': ['./Machine/(7,4).png'],
			'44': ['./Machine/(6,5).png'],
			'45': ['./Machine/(7,5).png'],
			'52': ['./Machine/(6,6).png'],
			'53': ['./Machine/(7,6).png'],
			'60': ['./Machine/(6,7).png'],
			'61': ['./Machine/(7,7).png'],
			'232': ['./CityTiles/(34,3).png'],
			'298': ['./CityTiles/(34,4).png'],
			'32': ['./Machine/(0,4).png'],
			'33': ['./Machine/(1,4).png'],
			'40': ['./Machine/(0,5).png'],
			'41': ['./Machine/(1,5).png'],
			'48': ['./Machine/(0,6).png'],
			'49': ['./Machine/(1,6).png'],
			'56': ['./Machine/(0,7).png'],
			'57': ['./Machine/(1,7).png'],
			'800': ['./CityTiles/(8,12).png'],
			'801': ['./CityTiles/(9,12).png'],
			'866': ['./CityTiles/(8,13).png'],
			'867': ['./CityTiles/(9,13).png'],
		}
		for style, layout in layouts.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if len(mapItems[col]) > 1:
							Tile((x, y), [self.visible_sprites], mapItems[col][0])
						else:
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites], mapItems[col][0])
		self.player = Player((200, 140), [self.visible_sprites], self.obstacle_sprites)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		debug(self.player.rect.center)
		self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width, self.half_height = self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('./CityTiles/(1,16).png').convert_alpha()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def calculate_offset(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        player_offset_pos = player.rect.topleft - self.offset
        self.display_surface.blit(player.image, player_offset_pos)

    def draw_floor(self):
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

    def custom_draw(self, player):
        sorted_sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)
        for sprite in sorted_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        self.draw_floor()
        self.calculate_offset(player)

        # Draw meters
        health_meter_rect = pygame.Rect(100, 10, player.health, 20)
        pygame.draw.rect(self.display_surface, (255, 0, 0), health_meter_rect)

        high_o_meter_rect = pygame.Rect(100, 40, player.high, 20)
        pygame.draw.rect(self.display_surface, (0, 255, 0), high_o_meter_rect)

        exp_meter_rect = pygame.Rect(100, 70, player.exp, 20)
        pygame.draw.rect(self.display_surface, (0, 0, 255), exp_meter_rect)

        self.font_path = os.path.join(os.path.dirname(__file__), "pixel_font.ttf")
        font = pygame.font.SysFont(self.font_path, 42)  # Load font
        health_text = font.render("H", True, (255, 255, 255))
        self.display_surface.blit(health_text, (health_meter_rect.right + 10, health_meter_rect.top))

        high_o_text = font.render("D", True, (255, 255, 255))
        self.display_surface.blit(high_o_text, (high_o_meter_rect.right + 10, high_o_meter_rect.top))

        exp_text = font.render("E", True, (255, 255, 255))
        self.display_surface.blit(exp_text, (exp_meter_rect.right + 10, exp_meter_rect.top))

        # Update and draw the weapon
        for sprite in self.sprites():
            if isinstance(sprite, Player):
                sprite.attack()
        