import pygame


class Ship:
    """create a ship"""

    def __init__(self , ai):
        """initialize the ship and set its position"""
        self.screen = ai.screen
        self.get_screen_rect = ai.screen.get_rect()
        #flag for moving the ship to the right direction
        self.moving_right = False
        self.moving_left = False

        #load the image and get its surface rect
        self.image = pygame.image.load('images/ship.bmp')
        self.get_image_rect = self.image.get_rect()
        # make all new ships be formed at the mid bottom of the screen
        #self.get_screen_rect.centerx = self.get_screen_rect.centerx
        #self.get_screen_rect.bottom = self.get_screen_rect.bottom - 5
        self.get_image_rect.midbottom = self.get_screen_rect.midbottom


    def update_movement(self):
            """updates the user right key and left key movement as it is been pressed"""
            if self.moving_right == True:
                self.get_image_rect.x += 1
            if self.moving_left == True:
                self.get_image_rect.x -= 1

    def blitme(self):
        """draw the image at the current location"""
        self.screen.blit(self.image, self.get_image_rect)

