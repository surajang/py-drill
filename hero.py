# -*- coding: UTF-8 -*-
class Hero:
    """Manage player's status info."""
    userName = ""       #Record player name
    playStartTime = 0   #Record for player's game start time
    totalPlayTime = 0   #Record for player's game play time
    moveCounter = 0     #Record for player's movement count
    currentStage = 1    #Record for player's stage clear info.

    def get_status(self):
        """Display player's status"""
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" " + self.userName + "@Room #"+ str(self.currentStage) + " | " + "Play time: 00m 20s" + " | " + "Moves: 0")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("")

    def get_user_name(self):
        """Returns player's name (string)"""
        return self.userName

    def set_user_name(self, inputName):
        """Set player name"""
        self.userName = inputName

    def get_current_stage(self):
        """Returns player's current stage number (number)"""
        return self.currentStage

    def set_current_stage(self, stageNumber):
        """Update player's current stage number"""
        self.currentStage = stageNumber

    def set_play_start_time(self, timeStamp):
        """Save the initialized time = very first play time"""
        self.playStartTime = timeStamp

    def get_play_start_time(self):
        """Returns player's first game play time (number)"""
        return self.playStartTime

    def get_total_play_time(self):
        """Returns player's total game play time (number)"""
        return self.totalPlayTime

    def set_total_play_time(self, timeDelta):
        """Update player's total game play time with given time delta.
        timeDelta >=0, so totalPlayTime never decreases!!
        """
        self.totalPlayTime = self.totalPlayTime + timeDelta
        
