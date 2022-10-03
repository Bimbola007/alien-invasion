import sys
import pygame
from settings import Settings
from ship import Ship
from bullet_details import Bullets
from alien import Alien


class Alien_invasion:
    """alien invasion game"""
    def __init__(self):
        """initialize the game settings"""
        pygame.init()
        self.setting = Settings()
        #self.screen = pygame.display.set_mode((self.setting.width,self.setting.height))

        #full screen mode
        self.screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
        self.setting.width = self.screen.get_rect().width
        self.setting.height = self.screen.get_rect().height


        #set background color
        self.bg_color = self.setting.bg_color
        pygame.display.set_caption("alien invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


    def run_game(self):
        """main loop for the game"""
        event = ''
        while event != pygame.QUIT:
            self._check_updates()
            self._update_screen()
            self._create_fleets()
            self.ship.update_movement()
            self.bullets.update()
            self._update_aliens()



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
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))

        if len(self.bullets) < self.setting.allowed_bullets:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)


    def _create_fleets(self):
        """create fleets of aliens"""
        alien = Alien(self)
        ship_height = self.ship.get_image_rect.height
        # alien_width = alien.rect.width
        alien_width , alien_height = alien.rect.size
        available_space_x = self.setting.width - (2 * alien_width)
        number_aliens = available_space_x // (2 * alien_width)
        # cal the available vertical space and number of rows it can fit
        available_space_y = self.setting.height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row in range(number_rows):
            for alien_position in range(number_aliens):
                self._create_alien(alien_position, row)


    def _create_alien(self, alien_position , row):
            """Create an alien and place it in the row."""
            alien = Alien(self)
            # alien_width = alien.rect.width
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_position
            alien.rect.x = alien.x
            alien.y = alien_height + 2 * alien_height * row
            alien.rect.y = alien.y
            self.aliens.add(alien)

    def _update_aliens(self):
        """update aliens movement"""
        self._check_for_edges()
        self.aliens.update()

    def _check_for_edges(self):
        """check if the fleet is at an edge and change their direction"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop each alien down and change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_dropspeed
        self.setting.fleet_direction *= -1






    def _update_screen(self):
            #set background color for every page
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()