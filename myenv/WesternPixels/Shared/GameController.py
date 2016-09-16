

import pygame

class GameController:

    def __init__(self):
        self.__currentScene = 0
        self.__scenes = []
        self.__gameMode = 0
        self.__currentDifficulty = 1
        self.__difficulties = []
        self.__sounds = []
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode()
        self.__players = []
        self.__enemies = []

    def start(self):
        pass

    def getScene(self, scene):
        return self.__currentScene

    def setScene(self, scene):
        self.__currentScene = scene

    def getPlayer(self):
        pass

    def playSound(self):
        pass


GameController().start()
