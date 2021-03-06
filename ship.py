#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from pygame.sprite import Sprite
    
class Ship(Sprite):
    def __init__(self, ai_settings, screen, stats):
        # """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.last_image = 0
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #"""Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
            if self.stats.masks_left>0:
            
                if self.last_image == 0:
                    self.image = pygame.image.load('images/ship-right-mask-v1.png')
                    self.last_image = 1
                else:
                    self.image = pygame.image.load('images/ship-right-mask-v0.png')
                    self.last_image = 0
                
            else:
            
                if self.last_image == 0:
                    self.image = pygame.image.load('images/ship-right-v1.png')
                    self.last_image = 1
                else:
                    self.image = pygame.image.load('images/ship-right-v0.jpg')
                    self.last_image = 0
                
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
            if self.stats.masks_left>0:
            
                if self.last_image == 0:
                    self.image = pygame.image.load('images/ship-left-mask-v1.png')
                    self.last_image = 1
                else:
                    self.image = pygame.image.load('images/ship-left-mask-v0.png')
                    self.last_image = 0
                
            else:
            
                if self.last_image == 0:
                    self.image = pygame.image.load('images/ship-left-v1.png')
                    self.last_image = 1
                else:
                    self.image = pygame.image.load('images/ship-left-v0.jpg')
                    self.last_image = 0
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        # """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
        
    def center_ship(self):
        #"""Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        

        
            
                    
            
    

