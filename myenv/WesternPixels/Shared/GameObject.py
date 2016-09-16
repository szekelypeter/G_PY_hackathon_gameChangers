
import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.__sprite = image
        self.__rect = image.get_rect()
        self.__position = position
        self.__mask = None
        self.__sound = None

    def update(self):
        pass
