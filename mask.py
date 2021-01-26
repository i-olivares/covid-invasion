#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random
from pygame.sprite import Sprite


# In[ ]:


class Mask(Sprite):
    def __init__(self, ai_settings, screen):
        super(Mask,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/mask.png')
        self.rect = self.image.get_rect()
        # Start each new mask in a new random position.
        self.rect.x = float(self.rect.width) 
        self.rect.y = float(self.rect.height)
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        #"""Draw the mask at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.y += self.ai_settings.mask_drop_speed
        #self.y += 0.5
        self.rect.y = self.y
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        

