import os

class GameConstants:

    SCREEN_SIZE = (1280, 1024)
    WINDOW_CENTER = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    MENU_PLAY = ("Play", -300)
    MENU_HIGHSCORE = ("HighScore", -150)
    MENU_EXIT = ("Exit", 50)

    GAME_MODE_SINGLE = ("Single", -200)
    GAME_MODE_MULTI = ("Multi", 100)
    HIGHSCORE = ("Highscore", 100)

    FPS = 60

    SCENE_START = 0
    SCENE_MENU = 1
    SCENE_OPTION_PLAYER_MODE = 2
    SCENE_HIGHSCORE = 3
    SCENE_PLAY_SINGLE = 4
    SCENE_PLAY_MULTI = 5
    SCENE_GAMEOVER = 6

    LOADING_TIME = 5

    GAME_MODE_SINGLE_PLAYER = 0
    GAME_MODE_MULTI_PLAYER = 1

    DIFFICULTY_EASY = 0
    DIFFICULTY_NORMAL = 1
    DIFFICULTY_HARD = 2

    IMAGE_SCENE_START_LOADING_ONE = os.path.join("Assets", "Images", "Scenes", "Start", "horse.png")
    IMAGE_SCENE_START_LOADING_TWO = os.path.join("Assets", "Images", "Scenes", "Start", "horse1.png")

    IMAGE_SCENE_PLAY_BACKGROUND_ONE = os.path.join("Assets", "Images", "Scenes", "Play", "background01.png")
    IMAGE_SCENE_PLAY_BACKGROUND_TWO = os.path.join("Assets", "Images", "Scenes", "Play", "background02.png")
    IMAGE_SCENE_PLAY_BACKGROUND_THRREE = os.path.join("Assets", "Images", "Scenes", "Play", "background03.png")
    IMAGE_SCENE_PLAY_BACKGROUND_FOUR = os.path.join("Assets", "Images", "Scenes", "Play", "background04.png")

    SOUND_FILE_SCENE_START_LOADING_HORSE = os.path.join("Assets", "Sounds", "Scenes", "Start", "horse_gallop.ogg")
    SOUND_FILE_SCENE_MENU = os.path.join("Assets", "Sounds", "Scenes", "Menu", "menu.ogg")

    SOUND_SCENE_START_LOADING_HORSE = 0
    SOUND_SCENE_MENU = 1

