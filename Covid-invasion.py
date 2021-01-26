#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pygame
from settings import Settings
from ship import Ship
from lives import Live
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from mask import Mask


# In[2]:


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    # Create an instance to store game statistics.
    pygame.display.set_caption("Covid Invasion")
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship.
    ship = Ship(ai_settings, screen, stats)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    masks = Group()
    tissues = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    running = True
    # Start the main loop for the game.
    while running:
        
        # Whatch for keyboard and mouse events.
        running = gf.check_events(running, ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            # Get rid of bullets that have disappeared.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            if stats.score % 1000 == 0 and ai_settings.last_mask_score != stats.score:
                ai_settings.last_mask_score = stats.score
                gf.create_mask(ai_settings, screen, masks)
            elif stats.score != 0 and stats.score % 600 == 0 and ai_settings.last_tissue_score != stats.score:
                ai_settings.last_tissue_score = stats.score
                gf.create_tissue(ai_settings, screen, tissues)
            
            gf.update_masks_tissues(ai_settings, screen, stats, sb, ship, aliens, bullets, masks,tissues)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, masks, tissues, play_button)
        # Make the most recentrly drawn screen visible
        #pygame.display.flip()


# In[3]:


run_game()


# In[ ]:




