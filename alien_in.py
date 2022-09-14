import  sys
import pygame
from settings import Settings
from ship import  Ship

class Alien_invasion:
    """alien invasion game"""
    def __init__(self):
        """initialize the game settings"""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.width,self.setting.height))
        #set background color
        self.bg_color = self.setting.bg_color
        pygame.display.set_caption("alien invasion")
        self.ship = Ship(self)

    def run_game(self):
        """main loop for the game"""
        event = ''
        while event != pygame.QUIT:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
            #set background color for every page
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()