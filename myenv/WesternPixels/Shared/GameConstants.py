import os

class GameConstants:

    SCREEN_SIZE = (1280, 700)
    WINDOW_CENTER = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BEIGE = (194, 87, 72)

    MENU_PLAY = ("Play", 250)
    MENU_HIGHSCORE = ("HighScore", 400)
    MENU_EXIT = ("Exit", 550)

    GAME_MODE_SINGLE = ("Single", 200)
    GAME_MODE_MULTI = ("Multi", 400)
    HIGHSCORE = ("Highscore", 100)

    FPS = 60

    SCENE_START = 0
    SCENE_MENU = 1
    SCENE_OPTION_PLAYER_MODE = 2
    SCENE_HIGHSCORE = 3
    SCENE_PLAY_SINGLE = 4
    SCENE_PLAY_MULTI = 5
    SCENE_GAMEOVER = 6

    LOADING_TIME = 10

    GAME_MODE_SINGLE_PLAYER = 0
    GAME_MODE_MULTI_PLAYER = 1

    DIFFICULTY_EASY = 0
    DIFFICULTY_NORMAL = 1
    DIFFICULTY_HARD = 2

    IMAGE_SCENE_START_LOADING_ONE = os.path.join("Assets", "Images", "Scenes", "Start", "horse.png")
    IMAGE_SCENE_START_LOADING_TWO = os.path.join("Assets", "Images", "Scenes", "Start", "horse1.png")

    IMAGE_SCENE_MENU = os.path.join("Assets", "Images", "Scenes", "Menu", "menu.png")

    IMAGE_SCENE_PLAY_BACKGROUND_ONE = os.path.join("Assets", "Images", "Scenes", "Play", "Background", "background01.png")
    IMAGE_SCENE_PLAY_BACKGROUND_THREE = os.path.join("Assets", "Images", "Scenes", "Play","Background",  "background03.png")
    IMAGE_SCENE_PLAY_BACKGROUND_FOUR = os.path.join("Assets", "Images", "Scenes", "Play","Background",  "background02.png")
    IMAGE_SCENE_PLAY_BACKGROUND_TWO = os.path.join("Assets", "Images", "Scenes", "Play","Background",  "background04.png")

    IMAGE_SCENE_PLAY_CROSSHAIRS = os.path.join("Assets", "Images", "Scenes", "Play", "Crosshairs", "crosshairs.png")
    IMAGE_SCENE_PLAY_CROSSHAIRS_CENTER = os.path.join("Assets", "Images", "Scenes", "Play", "Crosshairs", "crosshairscenter.png")
    IMAGE_SCENE_PLAY_RADAR = os.path.join("Assets", "Images", "Scenes", "Play", "radar.png")

    IMAGE_SCENE_PLAY_ENEMY_CHICKEN_FRONT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken", "chicken_front.png")
    IMAGE_SCENE_PLAY_ENEMY_CHICKEN_HEAD = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken", "chicken_head.png")
    IMAGE_SCENE_PLAY_ENEMY_CHICKEN_LEFT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken", "chicken_left.png")
    IMAGE_SCENE_PLAY_ENEMY_CHICKEN_RIGHT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken", "chicken_right.png")

    IMAGE_SCENE_PLAY_ENEMY_CLOWN_FRONT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown", "clown_front.png")
    IMAGE_SCENE_PLAY_ENEMY_CLOWN_HEAD = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown", "clown_head.png")
    IMAGE_SCENE_PLAY_ENEMY_CLOWN_LEFT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown", "clown_left.png")
    IMAGE_SCENE_PLAY_ENEMY_CLOWN_RIGHT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown", "clown_right.png")

    IMAGE_SCENE_PLAY_ENEMY_NUN_FRONT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_front.png")
    IMAGE_SCENE_PLAY_ENEMY_NUN_HEAD = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_head.png")
    IMAGE_SCENE_PLAY_ENEMY_NUN_LEFT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_left.png")
    IMAGE_SCENE_PLAY_ENEMY_NUN_RIGHT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_right.png")

    SOUND_FILE_SCENE_START_LOADING_HORSE = os.path.join("Assets", "Sounds", "Scenes", "Start", "horse_gallop.ogg")
    SOUND_FILE_SCENE_MENU = os.path.join("Assets", "Sounds", "Scenes", "Menu", "menu.ogg")

    SOUND_SCENE_START_LOADING_HORSE = 0
    SOUND_SCENE_MENU = 1

