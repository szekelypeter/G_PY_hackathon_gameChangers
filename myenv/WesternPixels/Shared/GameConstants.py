import os

class GameConstants:

    SCREEN_SIZE = (800, 600)
    WINDOW_CENTER = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)

    FPS = 60

    SCENE_START = 0
    SCENE_MENU = 1
    SCENE_OPTION = 2
    SCENE_HIGHSCORE = 3
    SCENE_PLAY = 4
    SCENE_GAMEOVER = 5

    LOADING_TIME = 5

    GAME_MODE_SINGLE_PLAYER = 0
    GAME_MODE_MULTI_PLAYER = 1

    DIFFICULTY_EASY = 0
    DIFFICULTY_NORMAL = 1
    DIFFICULTY_HARD = 2

    IMAGE_SCENE_START_LOADING_ONE = os.path.join("Assets", "Images", "Scenes", "Start", "horse.png")
    IMAGE_SCENE_START_LOADING_TWO = os.path.join("Assets", "Images", "Scenes", "Start", "horse1.png")
