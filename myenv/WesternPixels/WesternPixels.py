

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
        # pygame.mixer.init()
        pygame.joystick.init()
        pygame.mouse.set_visible(0)
        pygame.key.set_repeat(100, 5)

        # self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        # for joy in self.joysticks:
        #     joy.init()
        # self.joy1 = self.joysticks[0]
        # # joy2 = joysticks[1]
        # self.buttons = self.joy1.get_numbuttons()
        # joy_buttons = []
        # for i in range(self.buttons):
        #     joy_buttons.append(self.joy1.get_button(i))

        self.__info = pygame.display.Info()
        GameConstants.ACTUAL_SCREEN_SIZE = (self.__info.current_w, self.__info.current_h)
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(GameConstants.ACTUAL_SCREEN_SIZE, pygame.FULLSCREEN)
        self.__background = pygame.Surface(self.__screen.get_size()).convert()
        self.__background.fill(GameConstants.BLACK)

        self.__currentSound = None
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

    def playSound(self, soundClip, indefinitely=0, gun=False):
        self.__currentSound = soundClip
        if gun:
            soundClip.set_volume(0.5)
            soundClip.play(indefinitely)
        else:
            soundClip.play(indefinitely)

    def stopSound(self):
        self.__currentSound.stop()

    def getClock(self):
        return self.__clock

    def getScreen(self):
        return self.__screen

    def fillBackGround(self):
        self.__screen.blit(self.__background, (0, 0))
