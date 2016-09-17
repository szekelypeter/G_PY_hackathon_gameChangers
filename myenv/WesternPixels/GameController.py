

import pygame

from Maps import Map
from Scenes import *
from Shared import GameConstants

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')
if not pygame.joystick: print('Warning, joystick disabled')


class GameController:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.joystick.init()
        pygame.key.set_repeat(100, 5)

        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)
        self.__background = pygame.Surface(self.__screen.get_size()).convert()
        self.__background.fill(GameConstants.BLACK)
        self.__currentSound = None
        self.__sounds = \
            [
                pygame.mixer.Sound(GameConstants.SOUND_FILE_SCENE_START_LOADING_HORSE),
                pygame.mixer.Sound(GameConstants.SOUND_FILE_SCENE_MENU),
            ]
        self.__gameMode = GameConstants.GAME_MODE_SINGLE_PLAYER
        self.__currentDifficulty = GameConstants.DIFFICULTY_NORMAL
        self.__difficulties = []
        self.__players = []
        self.__enemies = []
        self.__currentScene = GameConstants.SCENE_START
        self.__scenes = \
        [
            StartScene(self),
            MenuScene(self),
            OptionPlayerModeScene(self),
            HighScoreScene(self),
            PlaySceneSingle(self),
            PlaySceneMulti(self),
            GameOverScene(self)
        ]


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

    def playSound(self, soundClip, indefinitely=0):
        sound = self.__sounds[soundClip]
        self.__currentSound = sound
        sound.play(indefinitely)

    def stopSound(self):
        self.__currentSound.stop()

    def getClock(self):
        return self.__clock

    def getScreen(self):
        return self.__screen

    def fillBackGround(self):
        self.__screen.blit(self.__background, (0, 0))
GameController().start()
