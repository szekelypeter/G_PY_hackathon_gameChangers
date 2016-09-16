from Scenes import Scene


class OptionScene(Scene):

    def __init__(self, gameController):
        self.volume = None
        super(OptionScene, self).__init__(gameController)
