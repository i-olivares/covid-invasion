#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Settings():
    # """A class to store all settings for Alien Invasion."""
    def __init__(self):
        #"""Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        
        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_blue = 70,130,180
        self.bullets_allowed = 3
        self.total_bullets_allowed = 50
        
        # Ship settings
        self.ship_speed_factor = 1
        self.ship_limit = 3
        
        # Mask settings
        self.mask_drop_speed = 0.5
        self.last_mask_score = 999
        self.mask_limit = 3
        
        self.last_tissue_score = 999
        self.tissue_points = 100
        
        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the alien point values increase
        self.score_scale = 1.2
        
        self.initialize_dynamic_settings()
        
        # Scoring
        self.alien_points = 50
        

        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1 # 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5
        self.mask_drop_speed = 0.5 
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
        
        
        
        
        
        
        
        
        
        
