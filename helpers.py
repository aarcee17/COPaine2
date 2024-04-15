from csv import reader
from os import walk
import pygame as pg

def import_csv_layout(path):
    with open(path) as level_map:
        layout = csv.reader(level_map, delimiter=',')
        terrain_map = [list(row) for row in layout]
    return terrain_map

def import_folder(path):
    surface_list = []
    for _, _, img_files in os.walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            image_surf = load_image(full_path)
            surface_list.append(image_surf)
    return surface_list

def load_image(image_path):
    return pygame.image.load(image_path).convert_alpha()
