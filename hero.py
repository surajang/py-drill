# -*- coding: UTF-8 -*-
class hero:
    """Manage player's status info."""
    userName = ""
    locationV = "N1"
    locationH = "W3"
    hpMax = 100
    mpMax = 50
    currentHP = 100
    currentMP = 50

    def __init__(self, inputName):
        """Initiate user profile with name"""
        self.userName = inputName

    def stat(self):
        """Display player's status"""
        print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        print "현재위치 "+ self.locationV + "-" + self.locationH + " | HP " + str(self.currentHP) + "/" + str(self.hpMax) + " | " + str(self.currentMP) + "/" + str(self.mpMax)
        print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        print ""

    def getUserName(self):
        """Returns player's name"""
        return self.userName

    def setUserName(self, inputName):
        """Set player name"""
        self.userName = inputName
