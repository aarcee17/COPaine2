import pygame
from settings import *
import os
class Level0:
    def __init__(self):
        self.slides = [
{"image": "intulogi/im1.jpeg", "message": "CARL, A TEENAGER FROM NEVADA, STUMBLED UPON DRUGS IN THE STREETS."},
{"image": "intulogi/im2.jpeg", "message": "INITIALLY, DRUGS SEEMED LIKE AN ESCAPE FROM HIS TROUBLES."},
{"image": "intulogi/im3.jpeg", "message": "CARL'S DRUG USE ESCALATED AS HE SOUGHT MORE INTENSE HIGHS."},
{"image": "intulogi/im4.jpeg", "message": "HE BEGAN TO NEGLECT HIS RESPONSIBILITIES AND RELATIONSHIPS."},
{"image": "intulogi/im5.jpeg", "message": "AS HIS ADDICTION DEEPENED, CARL'S HEALTH AND WELL-BEING SUFFERED."},
{"image": "plain_black.jpeg", "message": "CARL ENTERED A WORLD OF DARKNESS AND DESPAIR, RULED BY ADDICTION."},
{"image": "plain_black.jpeg", "message": "THE DRUGS CONSUMED HIM, DRIVING HIM TO THE EDGE OF SANITY."},
{"image": "intulogi/im8.jpeg", "message": ""},
{"image": "plain_black.jpeg", "message": "THE END"}

        ]

        self.current_slide = 0  # Index of the current slide
        self.font_path = os.path.join(os.path.dirname(__file__), "pixel_font.ttf")
        self.font = pygame.font.SysFont(self.font_path, 42)  # Load font
        self.text_speed = 0.1  # Speed of text rendering (in seconds per letter)
        self.text_index = 0  # Index of the current letter being rendered
        self.text_timer = 0  # Timer for controlling text rendering speed
        self.text_rendered = False  # Flag to track if text rendering is complete
        pygame.mixer.music.load('intologi/vibe.mp3')  # Load background music
        pygame.mixer.music.play(-1)  # Play background music indefinitely

    def run(self):
        pygame.display.get_surface().fill((0, 0, 0))  # Fill screen with black background
        self.draw_current_slide()  # Draw the current slide

        if not self.text_rendered:
            self.render_text()  # Render text if not already rendered
        else:
            text_surface = self.font.render(self.full_rendered_text, True, (255, 255, 255))  # Render full text surface
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 100))  # Position text at the bottom
            pygame.display.get_surface().blit(text_surface, text_rect)  # Blit text surface to screen


        if not self.text_rendered:
            self.render_text()  # Render text if not already rendered

    def draw_current_slide(self):
        current_slide = self.slides[self.current_slide]
        if current_slide["image"] != "plain_black.jpeg":
            image = pygame.image.load(current_slide["image"]).convert()
            rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Position image at the top
            pygame.display.get_surface().blit(image, rect)  # Blit image to screen
        else:
            pygame.display.get_surface().fill((0, 0, 0))  # Fill screen with black background

    def render_text(self):
        current_message = self.slides[self.current_slide]["message"]
        if self.text_index < len(current_message):
            if pygame.time.get_ticks() - self.text_timer > self.text_speed * 1000:
                self.text_timer = pygame.time.get_ticks()
                self.text_index += 1
        else:
            self.text_rendered = True

        rendered_text = current_message[:self.text_index]  # Partial text to render
        self.full_rendered_text = current_message  # Store fully rendered text
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
