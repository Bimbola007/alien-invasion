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
            self._check_updates()
            self._update_screen()
            self.ship.update_movement()
    def _check_updates(self):
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    #To move the ship to the right and left as it is been pressed down
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    #To stop the ship once the user stops pressing the right or left key
                   if event.key == pygame.K_RIGHT:
                       self.ship.moving_right = False
                   if event.key == pygame.K_LEFT:
                       self.ship.moving_left = False
    def _update_screen(self):
            #set background color for every page
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()