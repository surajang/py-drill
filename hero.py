# -*- coding: UTF-8 -*-
from time import time
import datetime

class Hero:
    """Manage player's status info."""
    userName = ""       #Record player name
    playStartTime = 0   #Record for player's game start time
    totalPlayTime = 0   #Record for player's game play time
    moveCounter = 0     #Record for player's movement count
    currentStage = 1    #Record for player's stage clear info.

    def get_status(self):
        """Display player's status"""
        self.update_total_play_time()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" " + self.userName + "@Room #"+ str(self.currentStage) + " | " + "Play time: " + str(self.get_total_play_time()) + "s" + " | " + "Moves: " + str(self.moveCounter))
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
        """Returns player's total game play time"""
        return datetime.timedelta(seconds=self.totalPlayTime)
        # Requires to return "MM:SS" formatted result

    def update_total_play_time(self):
        """Update player's total game play time
        totalPlayTime never decreases!!
        """
        self.totalPlayTime = time() - self.playStartTime
        #self.totalPlayTime = self.totalPlayTime + timeDelta

    def get_move_counter(self):
        """Returns player's total move count number"""
        return self.moveCounter

    def set_move_counter(self, moveDelta):
        """Update player's total move counter. never decreses!!!"""
        self.moveCounter = self.moveCounter + moveDelta
