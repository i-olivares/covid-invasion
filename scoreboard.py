#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame.font
from ship import Ship
from lives import Live
from mask import Mask
from pygame.sprite import Group

class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()
        self.prep_mask_score()
        
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Draw score and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.lives.draw(self.screen)
        self.masks.draw(self.screen)


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
        
    def prep_lives(self):
        """Show how many ships are left."""
        self.lives = Group()
        for lives_number in range(self.stats.lives_left):
            live = Live(self.ai_settings, self.screen)
            live.rect.x = 5 + lives_number * live.rect.width
            live.rect.y = 5
            self.lives.add(live)
            
    def prep_mask_score(self):
        """Show how many masks are left."""
        self.masks = Group()
        for masks_number in range(self.stats.masks_left):
            mask = Mask(self.ai_settings,self.screen)
            mask.rect.x = 5 + masks_number * mask.rect.width
            mask.rect.y = 40
            self.masks.add(mask)