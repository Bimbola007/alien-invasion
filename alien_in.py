import  sys
import pygame
from settings import Settings
from ship import  Ship
from bullet_details import Bullets

class Alien_invasion:
    """alien invasion game"""
    def __init__(self):
        """initialize the game settings"""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.width,self.setting.height))

        #full screen mode
        #self.screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
        #self.setting.width = self.screen.get_rect().width
        #self.setting.height = self.screen.get_rect().height


        #set background color
        self.bg_color = self.setting.bg_color
        pygame.display.set_caption("alien invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """main loop for the game"""
        event = ''
        while event != pygame.QUIT:
            self._check_updates()
            self._update_screen()
            self.ship.update_movement()
          #  self.bullets.update()
            self.bullets.update()
    def _check_updates(self):
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
                # To move the ship to the right and left as it is been pressed down
                elif event.type == pygame.KEYDOWN:
                    self._check_key_down_events(event)
                #To stop the ship once the user stops pressing the right or left key
                elif event.type == pygame.KEYUP:
                    self._check_key_up_events(event)

    def _check_key_down_events(self,event):
        """check for keydown events"""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        if event.key == pygame.K_UP:
                self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()


        # To quit out of the game
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_key_up_events(self, event):
        """check for keyup events"""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
                self.ship.moving_left = False
        if event.key == pygame.K_UP:
                self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
                self.ship.moving_down = False


    def _fire_bullets(self):
        """create bullets once the spacebar key is pressed and add the bullets to the group"""
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
            #set background color for every page
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()