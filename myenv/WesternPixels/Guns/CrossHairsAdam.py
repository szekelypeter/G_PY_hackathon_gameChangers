from Guns.CrossHairs import CrossHair


class CrossHairsAdam(CrossHair):

    def __init__(self, image, position):
        super(CrossHairsAdam, self).__int__(image, position)
        self.__targetZone = self.calculateTargetZone()

    def calculateTargetZone(self):
        pass

    def getTargetZone(self):
        return self.__targetZone
