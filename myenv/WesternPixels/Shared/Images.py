import os

import pygame


class FileLocations:
    SCENE_START_LOADING_ONE = os.path.join("Assets", "Images", "Scenes", "Start", "horse.png")
    SCENE_START_LOADING_TWO = os.path.join("Assets", "Images", "Scenes", "Start", "horse1.png")

    SCENE_MENU = os.path.join("Assets", "Images", "Scenes", "Menu", "menu.png")

    SCENE_PLAY_BACKGROUND_ONE = os.path.join("Assets", "Images", "Scenes", "Play", "Background", "background01.png")
    SCENE_PLAY_BACKGROUND_THREE = os.path.join("Assets", "Images", "Scenes", "Play", "Background", "background03.png")
    SCENE_PLAY_BACKGROUND_FOUR = os.path.join("Assets", "Images", "Scenes", "Play", "Background", "background02.png")
    SCENE_PLAY_BACKGROUND_TWO = os.path.join("Assets", "Images", "Scenes", "Play", "Background", "background04.png")

    SCENE_PLAY_CROSSHAIRS = os.path.join("Assets", "Images", "Scenes", "Play", "Crosshairs", "crosshairs.png")
    SCENE_PLAY_CROSSHAIRS_CENTER = os.path.join("Assets", "Images", "Scenes", "Play", "Crosshairs",
                                                "crosshairscenter.png")
    SCENE_PLAY_RADAR = os.path.join("Assets", "Images", "Scenes", "Play", "radar.png")

    SCENE_PLAY_ENEMY_CHICKEN_FRONT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken",
                                                  "chicken_front.png")
    SCENE_PLAY_ENEMY_CHICKEN_HEAD = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken",
                                                 "chicken_head.png")
    SCENE_PLAY_ENEMY_CHICKEN_LEFT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken",
                                                 "chicken_left.png")
    SCENE_PLAY_ENEMY_CHICKEN_RIGHT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Chicken",
                                                  "chicken_right.png")

    SCENE_PLAY_ENEMY_CLOWN_FRONT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown",
                                                "clown_front.png")
    SCENE_PLAY_ENEMY_CLOWN_HEAD = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown", "clown_head.png")
    SCENE_PLAY_ENEMY_CLOWN_LEFT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown", "clown_left.png")
    SCENE_PLAY_ENEMY_CLOWN_RIGHT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Clown",
                                                "clown_right.png")

    SCENE_PLAY_ENEMY_NUN_FRONT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_front.png")
    SCENE_PLAY_ENEMY_NUN_HEAD = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_head.png")
    SCENE_PLAY_ENEMY_NUN_LEFT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_left.png")
    SCENE_PLAY_ENEMY_NUN_RIGHT = os.path.join("Assets", "Images", "Scenes", "Play", "Enemy", "Nun", "nun_right.png")


images = {"loading horse 1": pygame.image.load(FileLocations.SCENE_START_LOADING_ONE),
          "loading horse 2": pygame.image.load(FileLocations.SCENE_START_LOADING_TWO),

          "menu": pygame.image.load(FileLocations.SCENE_MENU),

          "scene 1": pygame.image.load(FileLocations.SCENE_PLAY_BACKGROUND_ONE),
          "scene 2": pygame.image.load(FileLocations.SCENE_PLAY_BACKGROUND_TWO),
          "scene 3": pygame.image.load(FileLocations.SCENE_PLAY_BACKGROUND_THREE),
          "scene 4": pygame.image.load(FileLocations.SCENE_PLAY_BACKGROUND_FOUR),

          "chicken Front": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CHICKEN_FRONT),
          "chicken Head": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CHICKEN_HEAD),
          "chicken Left": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CHICKEN_LEFT),
          "chicken Right": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CHICKEN_RIGHT),

          "clown Front": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CLOWN_FRONT),
          "clown Head": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CLOWN_HEAD),
          "clown Left": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CLOWN_LEFT),
          "clown Right": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_CLOWN_RIGHT),

          "nun Front": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_NUN_FRONT),
          "nun Head": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_NUN_HEAD),
          "nun Left": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_NUN_LEFT),
          "nun Right": pygame.image.load(FileLocations.SCENE_PLAY_ENEMY_NUN_RIGHT),

          "crosshairs": pygame.image.load(FileLocations.SCENE_PLAY_CROSSHAIRS),
          "crosshairs Center": pygame.image.load(FileLocations.SCENE_PLAY_CROSSHAIRS_CENTER),
          "radar": pygame.image.load(FileLocations.SCENE_PLAY_RADAR)}
