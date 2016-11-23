# -*- coding: UTF-8 -*-
import fibo #test for module import
import random
import hero

user = hero.hero("용사")

class bcolors:
    """testing color formatting"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def intro():
    """print title text-thingy stuff on start. + Initializing process"""
    print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    print "#      WTF RPG WORLD         #"
    print "# somewhat like retro game.. #"
    print "# 한글도 나올 수 있나요?     #"
    print "##############################"
    print ""
    print bcolors.OKGREEN + "[안내원] 환영합니다, 낯선 여행자님. 당신은 누구신가요?" + bcolors.ENDC
    userInputName = raw_input("이름을 입력하세요: ")
    user.setUserName(userInputName) #create player profile
    print "[안내원] 만나서 반갑습니다,",user.getUserName() + "."

intro()

def mainMenu():
    """Main menu. All game play starts from here and comes back to here."""
    while True:
        userInput = raw_input("(M)이동 (S)상태 (I)인벤토리 (V)지도 (Z)기타: ") #main menu mockup

        if userInput in ('M', 'm'):
            print "Let's get move!"
            pass #place move feature call here
            break
        elif userInput in ('I', 'i'):
            print "Take a look at your inventory..."
            pass #place inventory feature call here
            break
        elif userInput in ('S', 's'):
            user.stat()
        elif userInput in ('V', 'v'):
            print "Here's your map."
            pass #place mapview feature call here
            break
        elif userInput in ('Z', 'z'):
            print "other menus."
            pass #place other menu call here
            break
        else:
            print "try again"

mainMenu()
