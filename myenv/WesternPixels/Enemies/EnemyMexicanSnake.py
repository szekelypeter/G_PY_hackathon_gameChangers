from Enemies import Enemy


class EnemymexicanSnake(Enemy):

    def __init__(self, gameController, gun, image, position, shootingTime):
        super(EnemymexicanSnake, self).__init__(gameController, gun, image, position, shootingTime)

    def reload(self):
        pass
