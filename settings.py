class Settings:
    """settings for alien invasion  game"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.width = 800
        self.height = 400
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        # bullet details
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_speed = 1
        self.bullet_color = (60,60,60)