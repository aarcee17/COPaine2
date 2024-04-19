
import pygame
TITLE = "COPaine"
WIDTH = 1440
HEIGHT = 847
FPS = 60
TILESIZE = 64
WHITE = (255, 255, 255)

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()