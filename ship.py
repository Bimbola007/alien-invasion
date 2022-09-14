import pygame


class Ship:
    """create a ship"""

    def __init__(self , ai):
        """initialize the ship and set its position"""
        self.screen = ai.screen
        self.get_screen_rect = ai.screen.get_rect()

        #load the image and get its surface rect
        self.imagee = pygame.image.load('images/ship.bmp')
        self.get_image_rect = self.imagee.get_rect()
        # make all new ships be formed at the mid bottom of the screen
        self.get_screen_rect.centerx = self.get_screen_rect.centerx
        self.get_screen_rect.bottom = self.get_screen_rect.bottom - 5
        #self.screen_rect = self.get_image_rect.midbottom



    def blitme(self):
        """draw the image at the current location"""
        self.screen.blit(self.imagee, self.get_image_rect)