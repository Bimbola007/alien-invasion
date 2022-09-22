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
        self.moving_up = False
        self.moving_down = False
        self.settings = ai.setting



        #load the image and get its surface rect
        self.image = pygame.image.load('images/ship.bmp')
        self.get_image_rect = self.image.get_rect()

        # make all new ships be formed at the mid bottom of the screen
        self.get_image_rect.midbottom = self.get_screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.get_image_rect.x)
        # Store a decimal value for the ship's vertical position.
        self.y = float(self.get_image_rect.y)



    def update_movement(self):
        """updates the user key movements as it is been pressed"""
        if self.moving_right == True and self.get_image_rect.right < self.get_screen_rect.right:
            #self.get_image_rect.x += 1
            self.x += self.settings.ship_speed

        if self.moving_left == True and self.get_image_rect.left > self.get_screen_rect.left:
            #self.get_image_rect.x -= 1
            self.x -= self.settings.ship_speed

        if self.moving_up == True and self.get_image_rect.top > 0 :
            self.y -= self.settings.ship_speed

        if self.moving_down == True and self.get_image_rect.bottom < self.get_screen_rect.bottom:
            self.y += self.settings.ship_speed

        #Update rect object from self.x
        self.get_image_rect.x = self.x
        self.get_image_rect.y = self.y

    def blitme(self):
        """draw the image at the current location"""
        self.screen.blit(self.image, self.get_image_rect)

