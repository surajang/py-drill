# -*- coding: UTF-8 -*-
class hero:
    """Manage player's status info."""
    userName = ""       #Record player name
    playStartTime = 0   #Record for player's game start time
    playClearTime = 0   #Record for player's game clear time
    moveCounter = 0     #Record for player's movement count
    currentStage = 1    #Record for player's stage clear info.

    def getStatus(self):
        """Display player's status"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" " + self.userName + "@Room #"+ str(self.currentStage) + " | " + "Play time: 00m 20s" + " | " + "Moves: 0")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("")

    def getUserName(self):
        """Returns player's name (string)"""
        return self.userName

    def setUserName(self, inputName):
        """Set player name"""
        self.userName = inputName

    def getCurrentStage(self):
        """Returns player's current stage number (number)"""
        return self.currentStage

    def setCurrentStage(self, stageNumber):
        """Update player's current stage number"""
        self.currentStage = stageNumber
