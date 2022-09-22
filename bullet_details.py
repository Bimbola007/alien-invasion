import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """class that manages the bullet settings"""

    def __init__(self , ai):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.setting
        self.color =  self.settings.bullet_color

        # create a bullet rect and fix it just above the ship
        self.bullet_rect = pygame.Rect(0,0, self.settings.bullet_width , self.settings.bullet_height)
        self.bullet_rect.midtop = ai.ship.get_image_rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.bullet_rect.y)

    def update(self):
        """move the bullet up the screen"""
        # update the bullets position
        self.y -= self.settings.bullet_speed

        # Update the rect position.
        self.bullet_rect.y = self.y


    def draw_bullet(self):
        """draw the bullet"""
        pygame.draw.rect(self.screen , self.color , self.bullet_rect)