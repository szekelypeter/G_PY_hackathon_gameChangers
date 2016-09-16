from Shared import GameObject


class CrossHairs(GameObject):

    def __int__(self, image, position):
        super(CrossHairs, self).__int__(image, position)

    def calculateTargetZone(self):
        pass