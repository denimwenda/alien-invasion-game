class Settings():
    """A class to store all settings for alien invasion."""
    def __init__(self):
        """Initialize the game settings."""
        #Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullets settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colo = 60, 60, 60
        self.bullets_allowed = 3