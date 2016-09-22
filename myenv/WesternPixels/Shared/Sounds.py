import os
import pygame

pygame.mixer.init()

class FileLocations:
    SCENE_START_LOADING_HORSE = os.path.join("Assets", "Sounds", "Scenes", "Start", "horse_gallop.ogg")
    SCENE_MENU = os.path.join("Assets", "Sounds", "Scenes", "Menu", "menu.ogg")

    SCENE_PLAY_ENEMIES_CHICKEN = os.path.join("Assets", "Sounds", "Scenes", "Play", "Enemies", "chicken.ogg")
    SCENE_PLAY_ENEMIES_CLOWN = os.path.join("Assets", "Sounds", "Scenes", "Play", "Enemies", "clown.ogg")
    SCENE_PLAY_ENEMIES_NUN = os.path.join("Assets", "Sounds", "Scenes", "Play", "Enemies", "nun.ogg")

    SCENE_PLAY_PUFF_1 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff1.ogg")
    SCENE_PLAY_PUFF_2 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff2.ogg")
    SCENE_PLAY_PUFF_3 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff3.ogg")
    SCENE_PLAY_PUFF_4 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff4.ogg")
    SCENE_PLAY_PUFF_5 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff5.ogg")
    SCENE_PLAY_PUFF_6 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff6.ogg")
    SCENE_PLAY_PUFF_7 = os.path.join("Assets", "Sounds", "Scenes", "Play", "Puff", "paff7.ogg")

sounds = {"loading horse": pygame.mixer.Sound(FileLocations.SCENE_START_LOADING_HORSE),
          "menu": pygame.mixer.Sound(FileLocations.SCENE_MENU),
          "puff 1": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_1),
          "puff 2": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_2),
          "puff 3": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_3),
          "puff 4": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_4),
          "puff 5": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_5),
          "puff 6": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_6),
          "puff 7": pygame.mixer.Sound(FileLocations.SCENE_PLAY_PUFF_7),
          "chicken": pygame.mixer.Sound(FileLocations.SCENE_PLAY_ENEMIES_CHICKEN),
          "clown": pygame.mixer.Sound(FileLocations.SCENE_PLAY_ENEMIES_CLOWN),
          "nun": pygame.mixer.Sound(FileLocations.SCENE_PLAY_ENEMIES_NUN)}