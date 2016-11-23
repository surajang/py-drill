# -*- coding: UTF-8 -*-
import fibo #test for module import
import random

def intro():
    """print title text-thingy stuff on start."""
    print "##############################"
    print "#      WTF RPG WORLD         #"
    print "# somewhat like retro game.. #"
    print "# 한글도 나올 수 있나요?     #"
    print "##############################"
    print ""

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
        print "현재위치 "+ self.locationV + "-" + self.locationH + " | HP " + str(self.currentHP) + "/" + str(self.hpMax) + " | " + str(self.currentMP) + "/" + str(self.mpMax)

    def getUserName(self):
        """Returns player's name"""
        return self.userName

intro()

print "[안내원] 환영합니다, 낯선 여행자님. 당신은 누구신가요?"
var = raw_input("이름을 입력하세요: ")
user = hero(var) #create player profile
print "[안내원] Ah, nice to meet you,",user.getUserName() + "."

user.stat() # display user status
userInput = raw_input("(M)이동 (I)인벤토리 (V)지도 (Z)기타: ") #main menu mockup
print "##Debug## userInput =", userInput
