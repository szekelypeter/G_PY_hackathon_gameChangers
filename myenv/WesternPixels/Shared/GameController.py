

import pygame
from Scenes import *
from Shared import GameConstants

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')
if not pygame.joystick: print('Warning, joystick disabled')


class GameController:

    def __init__(self):
        self.__currentScene = GameConstants.SCENE_START
        self.__scenes = \
            [
            StartScene(self),
            MenuScene(self),
            OptionScene(self),
            HighScoreScene(self),
            PlayScene(self),
            GameOverScene(self)
            ]
        self.__gameMode = GameConstants.GAME_MODE_SINGLE_PLAYER
        self.__currentDifficulty = GameConstants.DIFFICULTY_NORMAL
        self.__difficulties = []
        self.__sounds = []
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)
        self.__players = []
        self.__enemies = []

        pygame.init()
        pygame.mixer.init()
        pygame.joystick.init()

    def start(self):
        while True:
            self.__clock.tick(GameConstants.FPS)
            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

    def getScene(self, scene):
        return self.__currentScene

    def setScene(self, scene):
        self.__currentScene = scene

    def getPlayer(self):
        pass

    def playSound(self):
        pass


GameController().start()
