import pygame
from settings import *

class Level0:
    def __init__(self):
        self.slides = [Slide1(), Slide2()]  # List of slides
        self.current_slide = 0  # Index of the current slide
        self.font = pygame.font.Font(None, 50)  # Load pixel fonts
        self.text_speed = 0.1  # Speed of text rendering (in seconds per letter)
        self.text_index = 0  # Index of the current letter being rendered
        self.text_timer = 0  # Timer for controlling text rendering speed
        self.text_rendered = False  # Flag to track if text rendering is complete
        pygame.mixer.music.load('vibe.mp3')  # Load background music
        pygame.mixer.music.play(-1)  # Play background music indefinitely

    def run(self):
        pygame.display.get_surface().fill((0, 0, 0))  # Fill screen with black background
        self.slides[self.current_slide].draw()  # Draw the current slide

        if not self.text_rendered:
            self.render_text()  # Render text if not already rendered

    def render_text(self):
        current_text = self.slides[self.current_slide].get_text()  # Get text for current slide
        if self.text_index < len(current_text):
            if pygame.time.get_ticks() - self.text_timer > self.text_speed * 1000:
                self.text_timer = pygame.time.get_ticks()
                self.text_index += 1
        else:
            self.text_rendered = True

        rendered_text = current_text[:self.text_index]  # Partial text to render
        text_surface = self.font.render(rendered_text, True, (255, 255, 255))  # Render text surface
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 100))  # Position text at the bottom
        pygame.display.get_surface().blit(text_surface, text_rect)  # Blit text surface to screen

    def next_slide(self):
        self.text_rendered = False  # Reset text rendering flag
        self.text_index = 0  # Reset text index
        self.current_slide += 1  # Move to the next slide
        if self.current_slide >= len(self.slides):
            self.current_slide = len(self.slides) - 1  # Ensure not to exceed slide count

    def is_complete(self):
        return self.current_slide >= len(self.slides) - 1  # Check if animation is complete

class Slide:
    def __init__(self):
        pass

    def draw(self):
        pass

    def get_text(self):
        pass

class Slide1(Slide):
    def __init__(self):
        super().__init__()
        # Load image for the slide
        self.image = pygame.image.load("trippyboy1.jpeg").convert()
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the image

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)  # Blit image to screen

    def get_text(self):
        return "Welcome to the Trdddfjhbjshbrfjhskvjmha brdkvhmsmvhsdrv v vakhbrvkajhr bv  ajshebvkishbdvkhf skdhbvjsh  ijkhbsdvjhsbdvippy Adventure!"

class Slide2(Slide):
    def __init__(self):
        super().__init__()
        # Load image for the slide
        self.image = pygame.image.load("city.jpeg").convert()
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the image

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)  # Blit image to screen

    def get_text(self):
        return "Embark on a journey like no sdvxdvsevsevjh svjhb sejvhbsdjhv nxdhjcbshdjcn shjdc other."

