import pygame

pygame.init()
font = pygame.font.Font(None, 30)
debug_position = (10, 10)

def debug(info):
    display_surface = pygame.display.get_surface()
    
    debug_surf = font.render(str(info), True, pygame.Color('white'))
    debug_rect = debug_surf.get_rect(topleft=debug_position)
    
    pygame.draw.rect(display_surface, pygame.Color('black'), debug_rect)
    display_surface.blit(debug_surf, debug_rect)

