import pygame
from settings import *
import os
class Level0:
    def __init__(self):
        self.slides = [
            {"image": "intologi/intro.png", "message": "READY TO BEGIN? PRESS SPACE TO BEGIN THE JOURNEY!"},
{"image": "intologi/im1.jpeg", "message": "SAKSHAL, A TEENAGER FROM NEVADA, STUMBLED UPON DRUGS IN THE STREETS."},
{"image": "intologi/im2.jpeg", "message": "INITIALLY, DRUGS SEEMED LIKE AN ESCAPE FROM HIS TROUBLES."},
{"image": "intologi/im3.jpeg", "message": "CARL'S DRUG USE ESCALATED AS HE SOUGHT MORE INTENSE HIGHS."},
{"image": "intologi/im4.jpeg", "message": "HE BEGAN TO NEGLECT HIS RESPONSIBILITIES AND RELATIONSHIPS."},
{"image": "intologi/im4.jpeg", "message": "AS HIS ADDICTION DEEPENED, CARL'S HEALTH AND WELL-BEING SUFFERED."},
{"image": "intologi/im5.jpeg", "message": "CARL ENTERED A WORLD OF DARKNESS AND DESPAIR, RULED BY ADDICTION."},
{"image": "intologi/im5.jpeg", "message": "THE DRUGS CONSUMED HIM, DRIVING HIM TO THE EDGE OF SANITY."},
{"image": "intologi/im8.jpeg", "message": ""},
{"image": "plain_black.jpeg", "message": ""}

        ]

    #     self.current_slide = 0  # Index of the current slide
    #     self.font_path = os.path.join(os.path.dirname(__file__), "pixel_font.ttf")
    #     self.font = pygame.font.SysFont(self.font_path, 42)  # Load font
    #     self.text_speed = 0.05  # Speed of text rendering (in seconds per letter)
    #     self.text_index = 0  # Index of the current letter being rendered
    #     self.text_timer = 0  # Timer for controlling text rendering speed
    #     self.text_rendered = False  # Flag to track if text rendering is complete
    #     pygame.mixer.music.load('intologi/vibe.mp3')  # Load background music
    #     pygame.mixer.music.play(-1)  # Play background music indefinitely

    # def run(self):
    #     pygame.display.get_surface().fill((0, 0, 0))  # Fill screen with black background
    #     self.draw_current_slide()  # Draw the current slide

    #     if not self.text_rendered:
    #         self.render_text()  # Render text if not already rendered
    #     else:
    #         text_surface = self.font.render(self.full_rendered_text, True, (255, 255, 255))  # Render full text surface
    #         text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 100))  # Position text at the bottom
    #         pygame.display.get_surface().blit(text_surface, text_rect)  # Blit text surface to screen


    #     if not self.text_rendered:
    #         self.render_text()  # Render text if not already rendered

    # def draw_current_slide(self):
    #     current_slide = self.slides[self.current_slide]
    #     if current_slide["image"] != "plain_black.jpeg":
    #         image = pygame.image.load(current_slide["image"]).convert()
    #         rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Position image at the top
    #         pygame.display.get_surface().blit(image, rect)  # Blit image to screen
    #     else:
    #         pygame.display.get_surface().fill((0, 0, 0))  # Fill screen with black background

    # def render_text(self):
    #     current_message = self.slides[self.current_slide]["message"]
    #     if self.text_index < len(current_message):
    #         if pygame.time.get_ticks() - self.text_timer > self.text_speed * 1000:
    #             self.text_timer = pygame.time.get_ticks()
    #             self.text_index += 1
    #     else:
    #         self.text_rendered = True

    #     rendered_text = current_message[:self.text_index]  # Partial text to render
    #     self.full_rendered_text = current_message  # Store fully rendered text
    #     text_surface = self.font.render(rendered_text, True, (255, 255, 255))  # Render text surface
    #     text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 100))  # Position text at the bottom
    #     pygame.display.get_surface().blit(text_surface, text_rect)  # Blit text surface to screen


    # def next_slide(self):
    #     self.text_rendered = False  # Reset text rendering flag
    #     self.text_index = 0  # Reset text index
    #     self.current_slide += 1  # Move to the next slide
    #     if self.current_slide >= len(self.slides):
    #         self.current_slide = len(self.slides) - 1  # Ensure not to exceed slide count

    # def is_complete(self):
    #     return self.current_slide >= len(self.slides) - 1  # Check if animation is complete

        self.current_slide = 0  # Index of the current slide
        self.font_path = os.path.join(os.path.dirname(__file__), "pixel_font.ttf")
        self.font = pygame.font.SysFont(self.font_path, 32, bold=True)  # Load font and make it bold
        self.text_speed = 0.05  # Speed of text rendering (in seconds per letter)
        self.text_index = 0  # Index of the current letter being rendered
        self.text_timer = 0  # Timer for controlling text rendering speed
        self.text_rendered = False  # Flag to track if text rendering is complete
        self.text_box_height = HEIGHT * 0.25  # Height of the text box
        self.image_height = HEIGHT - self.text_box_height  # Height of the image display area
        # self.background_music_path = os.path.join(os.path.dirname(__file__), "intologi/vibe.mp3")
        # pygame.mixer.music.load(self.background_music_path)  # Load background music
        # pygame.mixer.music.play(-1)  # Play background music indefinitely

    def run(self):
        pygame.display.get_surface().fill((255, 255, 255))  # Fill screen with white background
        self.render_image()  # Render image for the current slide
        self.render_text_box()  # Render text box for the current slide

    def render_text_box(self):
        text_box_rect = pygame.Rect(0, HEIGHT - self.text_box_height, WIDTH, self.text_box_height)
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), text_box_rect, 3)  # Draw the border of the text box

        current_text = self.slides[self.current_slide]["message"]
        text_surface = self.font.render(current_text, True, (0, 0, 0))  # Render text surface
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - self.text_box_height // 2))  # Position text at the center of the text box
        pygame.display.get_surface().blit(text_surface, text_rect)
        
    def render_image(self):
        image_path = self.slides[self.current_slide]["image"]
        if image_path == "plain_black.jpeg":
            image = pygame.Surface((WIDTH, self.image_height))  # Create a blank white surface
            image.fill((255, 255, 255))  # Fill the surface with white color
        else:
            image = pygame.image.load(image_path).convert()  # Load image
            # Resize image to fit the image display area
            image = pygame.transform.scale(image, (WIDTH, self.image_height))

        image_rect = image.get_rect(topleft=(0, 0))  # Position image at the top-left corner
        pygame.display.get_surface().blit(image, image_rect)  # Blit image to screen

    def next_slide(self):
        self.text_rendered = False  # Reset text rendering flag
        self.text_index = 0  # Reset text index
        self.current_slide += 1  # Move to the next slide
        if self.current_slide >= len(self.slides):
            self.current_slide = len(self.slides) - 1  # Ensure not to exceed slide count

    def is_complete(self):
        return self.current_slide >= len(self.slides) - 1  # Check if animation is complete

    def update_text(self):
        current_text = self.slides[self.current_slide]["message"]
        if self.text_index < len(current_text):
            if pygame.time.get_ticks() - self.text_timer > self.text_speed * 1000:
                self.text_timer = pygame.time.get_ticks()
                self.text_index += 1
        else:
            self.text_rendered = True
