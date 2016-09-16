from Scenes import Scene
from pygame.locals import *

class OptionScene(Scene):

    def __init__(self, gameController):
        self.volume = None
        super(OptionScene, self).__init__(gameController)
