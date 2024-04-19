import pygame
import os
from settings import *

class Levelf:
    def __init__(self):
        self.slides = [
            {"image": "outrologi/downidle.png", "text": "Where am I ?"},
            {"image": "black.jpeg", "text": "Your laughter was music to my ears, and your smile could brighten even the darkest of days."},
            {"image": "outrologi/hoax.png", "text": "I watched you grow, taking your first steps, saying your first words, each moment etched into my heart forever."},
            {"image": "outrologi/hoax.png", "text": "But as time passed, I saw a change in you, a darkness creeping into your soul, clouding the light that once shone so brightly."},
            {"image": "outrologi/image2.png", "text": "My beloved child, as your mother, I remember holding you in my arms, feeling the warmth of your tiny body against mine."},
            {"image": "outrologi/image3.png", "text": "You were my greatest blessing, my little ray of sunshine in a world filled with shadows."},
            {"image": "outrologi/image4.png", "text": "But as you grew older, I watched helplessly as the shadows closed in, stealing away the light and leaving only darkness behind."},
            {"image": "outrologi/image5.png", "text": "My heart breaks to see you suffer, to see the pain etched into your face and the emptiness in your eyes."},
            {"image": "outrologi/image1.png", "text": "My child, I long to see you free from the grip of addiction, to see the sparkle return to your eyes and the joy to your heart."},
            {"image": "outrologi/image6.png", "text": "But know this, my child, you are not alone. We are here for you, waiting with open arms and unconditional love, ready to help you find your way back home."},
            {"image": "outrologi/image7.png", "text": "COME BACK TO US"},
            {"image": "outrologi/image7.png", "text": "COME BACK TO US", "font_size": 48},  # Bigger font size
            {"image": "black.jpeg", "text": "The end","font_size": 96},
            {"image": "black.jpeg", "text": ""}
            
        ]

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

        current_text = self.slides[self.current_slide]["text"]
        text_surface = self.font.render(current_text, True, (0, 0, 0))  # Render text surface
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - self.text_box_height // 2))  # Position text at the center of the text box
        pygame.display.get_surface().blit(text_surface, text_rect)
        
    def render_image(self):
        image_path = self.slides[self.current_slide]["image"]
        if image_path == "black.jpeg":
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
        current_text = self.slides[self.current_slide]["text"]
        if self.text_index < len(current_text):
            if pygame.time.get_ticks() - self.text_timer > self.text_speed * 1000:
                self.text_timer = pygame.time.get_ticks()
                self.text_index += 1
        else:
            self.text_rendered = True
