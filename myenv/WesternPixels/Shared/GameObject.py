
import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__sprite = None
        self.__mask = None
        self.__sound = None

    def update(self):
        pass