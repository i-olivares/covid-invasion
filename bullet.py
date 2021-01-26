#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from pygame.sprite import Sprite


# In[ ]:


class Bullet(Sprite):
    #"""A class to manage bullets fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
    #"""Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        
        self.rect_needle = pygame.Rect(0, 0, ai_settings.bullet_width/3,ai_settings.bullet_height*1.5)
        self.rect_needle.centerx = ship.rect.centerx
        self.rect_needle.top = ship.rect.top
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.blue = ai_settings.bullet_blue
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        #"""Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y
        self.rect_needle.y = self.y - 7
        
    def draw_bullet(self):
        #"""Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect_needle)
        pygame.draw.rect(self.screen, self.blue, self.rect)

