class Team:

    def __init__(self, twoPlayerMode, playerOne, playerTwo, health, highScore):
        self.__twoPlayerMode = twoPlayerMode
        self.__playerOne = playerOne
        self.__playerTwo = playerTwo
        self.__health = health
        self.__highScore = highScore

    def isTwoPlayerMode(self):
        return self.__twoPlayerMode

    def getPlayerOne(self):
        return self.__playerOne

    def getPlayerTwo(self):
        return self.__playerTwo

    def getHealth(self):
        return self.__health

    def setHealth(self, health):
        self.__health = health

    def getHighScore(self):
        return self.__highScore
