# -*- coding: UTF-8 -*-
class hero:
    """Manage player's status info."""
    userName = ""
    playStartTime = 0
    playClearTime = 0
    currentStage = 1

    def stat(self):
        """Display player's status"""
        print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        print "현재위치: "+ str(self.currentStage) + "번 방 | " + "플레이 시간: 00분 20초"
        print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        print ""

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
