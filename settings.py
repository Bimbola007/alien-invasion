class Settings:
    """settings for alien invasion  game"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.width = 800
        self.height = 400
        self.bg_color = (230,230,230)
        self.ship_speed = 20  #1.5
        # bullet details
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_speed = 20 #1
        self.bullet_color = (60,60,60)
        self.allowed_bullets = 3
        # alien details
        self.alien_speed = 3.0
        # fleet details
        # fleet drop speed
        self.fleet_dropspeed = 10
        #fleet direction  ;  1 represents right while -1 represents left.
        self.fleet_direction = 1