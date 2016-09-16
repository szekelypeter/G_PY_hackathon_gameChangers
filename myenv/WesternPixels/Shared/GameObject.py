__author__ = "Knapecz Ádám"
__date__ = "9/16/2016"

import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = None
        self.mask = None
        self.sound = None

    def update(self):
        pass