__author__ = "Knapecz Ádám"
__date__ = "9/16/2016"

import pygame

class GameController:

    def __init__(self):
        self.currentScene = 0
        self.scenes = []
        self.gameMode = 0
        self.currentDifficulty = 1
        self.difficulties = []
        self.sounds = []
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode()
        self.players = []
        self.enemies = []

    def start(self):
        pass

    def getScene(self, scene):
        return self.currentScene

    def setScene(self, scene):
        self.__currentScene = scene

    def getPlayer(self):
        pass

    def playSound(self):
        pass


GameController().start()

