import pygame
from pygame.sprite import  Sprite

class Alien(Sprite):
    """creating an alien"""
    def __init__(self , ai):
        """initialize the alien settings"""
        super().__init__()
        self.screen = ai.screen
        self.get_screen_rect = ai.screen.get_rect()
        self.settings = ai.setting
        # import the alien image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #set the alien position at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #get the float value of the horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """check for edges by returning True if the condition stated is true """
        if self.rect.right >= self.get_screen_rect.right or self.rect.left <= 0 :
            return  True


    def update(self):
        """update the aliens position to the right or left with the aliens speed"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction

        # update the horizontal value with the x attr
        self.rect.x = self.x