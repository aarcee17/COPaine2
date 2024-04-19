import pygame 
from settings import *
from tile import Tile
from player import Player
from enemy import Enemy
from debug import debug
import pandas as pd
import os
from mini_game import main as mini_game_main
from two64 import main as two64_main
from tictactoe import main as tictactoe_main

def import_csv_layout(path):
    terrain_map = pd.read_csv(path, header=None).astype(str).values.tolist()
    return terrain_map

class Level:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup(self)
		self.obstacle_sprites = pygame.sprite.Group()
		self.weapon_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		#self.mini_game_active = [True, True, True, True, True, True, True, True, True, True]
		self.mini_game_active = [False,False,False,False,False,False,False,False,False,True]
		# sprite setup
		self.enemies = []
		self.create_map()


    # def is_complete(self):
    #     if self.mini_game_active[-1]== True:
    #         return True
    #     else:
    #         return False


	def create_map(self):
		layouts = {
			'base': import_csv_layout('./map/DrugMap_Base.csv'),
			'road': import_csv_layout('./map/DrugMap_Roads.csv'),
			'homes': import_csv_layout('./map/DrugMap_Homes.csv'),
			'entities': import_csv_layout('./map/DrugMap_Entities.csv')
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
		for _, layout in layouts.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if col == '1001':
							self.enemies.append(Enemy((x, y), [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, [10, 10, 4, 10, 3, 40, 300], self.damage_player))

						elif col == '1002':
							self.enemies.append(Enemy((x, y), [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, [100, 10, 4, 5, 4, 20, 340], self.damage_player))
						elif col == '1003':
							self.enemies.append(Enemy((x, y), [self.visible_sprites, self.attackable_sprites], self.obstacle_sprites, [25, 10, 4, 8, 10, 10, 400], self.damage_player))
						elif len(mapItems[col]) > 1:
							Tile((x, y), [self.visible_sprites], mapItems[col][0])
						else:
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites], mapItems[col][0])
		self.player = Player((200, 140), [self.visible_sprites], self.obstacle_sprites)
		self.weapon_sprites = self.player.weapon_sprites

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		# debug([self.player.rect.center, self.player.health, self.player.high, self.player.exp])
		self.visible_sprites.update()

		self.check_mini_game()
		self.visible_sprites.update_enemy_sprites(self.player)
		self.execute_player_attack()

	def execute_player_attack(self):
		if self.weapon_sprites:
			for attack_sprite in self.weapon_sprites:
				colliding_with = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
				print(colliding_with)
				if colliding_with:
					for target_sprite in colliding_with:
						target_sprite.receive_damage(self.player, self.player.exp)
						self.player.exp += 1

	def get_mini_game_number(self, player_pos):
		x, y = player_pos[0], player_pos[1]

		mini_game_conditions = [
			# Condition 0
			x >= 9 and x <= 110 and y == 590,
			# Condition 1
			x >= 1500 and x <= 1600 and y == 206,
			# Condition 2
			x == 1888 and y >= 1350 and y <= 1450,
			# Condition 3
			x >= 2900 and x <= 3000 and y == 590,
			# Condition 4
			x >= 3000 and x <= 3200 and y >= 1000 and y <= 1400,
			# Condition 5
			x == 2528 and y >= 1350 and y <= 1440,
			# Condition 6
			x >= 2050 and x <= 2400 and y >= 35 and y <= 50,
			# Condition 7
			x == 1632 and y >= 380 and y <= 480,
			# Condition 8
			y == 1422 and x >= 270 and x <= 370,
			# Condition 9
			y == 78 and x >= 3080 and x <= 3200
		]
		
		for game_number, condition in enumerate(mini_game_conditions):
			if condition:
				return game_number

	def check_mini_game(self):
		original_caption = pygame.display.get_caption()  # Store the original caption
		
		if ((self.player.rect.center[0] >= 9 and self.mini_game_active[0] and self.player.rect.center[0] <= 110 and self.player.rect.center[1] == 590 and self.player.currdir == "up") or (self.player.rect.center[0] >= 1500 and self.player.rect.center[0] <= 1600 and self.player.rect.center[1] == 206 and self.player.currdir == "up" and self.mini_game_active[1]) or (self.player.rect.center[0] == 1888 and self.player.rect.center[1] <= 1450 and self.player.rect.center[1] >= 1350 and self.player.currdir == "right" and self.mini_game_active[2]) or (self.player.rect.center[0] >= 2900 and self.player.rect.center[0] <= 3000 and self.player.rect.center[1] == 590 and self.player.currdir == "up" and self.mini_game_active[3]) or (self.player.rect.center[0] >= 3000 and self.player.rect.center[0] <= 3200 and self.player.rect.center[1] >= 1000 and self.player.rect.center[1] <= 1400 and self.mini_game_active[4]) or (self.player.rect.center[0] == 2528 and self.player.rect.center[1] >= 1350 and self.player.rect.center[1] <= 1440 and self.mini_game_active[5]) or (self.player.rect.center[0] >= 2050 and self.player.rect.center[0] <= 2400 and self.player.rect.center[1] >= 35 and self.player.rect.center[1] <= 50 and self.mini_game_active[6]) or (self.player.rect.center[0] == 1632 and self.player.rect.center[1] >= 380 and self.player.rect.center[1] <= 480 and self.mini_game_active[6]) or (self.player.rect.center[1] == 1422 and self.player.rect.center[0] >= 270 and self.player.rect.center[0] <= 370 and self.mini_game_active[7]) or (self.player.rect.center[1] == 1422 and self.player.rect.center[0] >= 270 and self.player.rect.center[0] <= 370 and self.mini_game_active[8]) or (((not self.mini_game_active[0]) and (not self.mini_game_active[1]) and (not self.mini_game_active[2]) and (not self.mini_game_active[3]) and (not self.mini_game_active[4]) and (not self.mini_game_active[5]) and (not self.mini_game_active[6]) and (not self.mini_game_active[7]) and (not self.mini_game_active[8])) and self.player.rect.center[0] >= 3080 and self.player.rect.center[0] <= 3200 and self.player.rect.center[1] == 78)) and pygame.key.get_pressed()[pygame.K_PERIOD]:
			two64_main()
			# final_score = tictactoe_main()
			self.mini_game_active[self.get_mini_game_number(self.player.rect.center)] = False
			self.player.rect.center = (self.player.rect.center[0], self.player.rect.center[1])
			# if final_score >= 10:
			# 	self.player.exp += 10
			# 	self.player.high -= 10
			# 	self.player.health += 10
			self.visible_sprites.custom_draw(self.player)

			self.display_surface = pygame.display.get_surface()
			pygame.display.set_mode((WIDTH, HEIGHT))

			pygame.display.set_caption(original_caption[0])
			self.player.high -= 10

			# print("Final Score from Mini-Game:", final_score)
			print(self.mini_game_active) 
            #play_sound("graphics/sound/vending.wav")
            
            
	def is_complete(self):
		return self.mini_game_active[-1] == False

	def damage_player(self,amount):
		self.player.health -= amount
		self.player.vulnerable = False

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, level):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width, self.half_height = self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('./CityTiles/(1,16).png').convert_alpha()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))
        self.level = level

    def calculate_offset(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        player_offset_pos = player.rect.topleft - self.offset
        self.display_surface.blit(player.image, player_offset_pos)

    def draw_floor(self):
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

    def custom_draw(self, player):
        self.draw_floor()
        sorted_sprites = sorted(self.sprites(), key = lambda sprite: sprite.rect.centery)
        for sprite in sorted_sprites:
            if sprite not in self.level.enemies and sprite not in self.level.weapon_sprites:
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
        for sprite in self.level.enemies:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        for sprite in self.level.weapon_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        self.calculate_offset(player)


        # Draw meters
        health_meter_rect = pygame.Rect(40, 10, player.health * 2.5, 20)
        pygame.draw.rect(self.display_surface, (255, 0, 0), health_meter_rect)

        high_o_meter_rect = pygame.Rect(40, 40, player.high * 2.5, 20)
        pygame.draw.rect(self.display_surface, (0, 255, 0), high_o_meter_rect)

        exp_meter_rect = pygame.Rect(40, 70, player.exp * 0.25, 20)
        pygame.draw.rect(self.display_surface, (0, 0, 255), exp_meter_rect)

        self.font_path = os.path.join(os.path.dirname(__file__), "pixel_font.ttf")
        font = pygame.font.SysFont(self.font_path, 42)
        strr= "H " + str(player.health) 
        st = "D " + str(player.high)
        strrr = "E " + str(player.exp)
        health_text = font.render(strr, True, (255, 255, 255))
        self.display_surface.blit(health_text, (health_meter_rect.right + 10, health_meter_rect.top))

        high_o_text = font.render(st, True, (255, 255, 255))
        self.display_surface.blit(high_o_text, (high_o_meter_rect.right + 10, high_o_meter_rect.top))

        exp_text = font.render(strrr, True, (255, 255, 255))
        self.display_surface.blit(exp_text, (exp_meter_rect.right + 10, exp_meter_rect.top))

        # Update and draw the weapon
        for sprite in self.sprites():
            if isinstance(sprite, Player):
                sprite.attack()
    def update_enemy_sprites(self, player):
        print("Updating enemy sprites")
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        
        for idx, enemy in enumerate(enemy_sprites):
            print(idx)
            enemy.update_enemy(player)

