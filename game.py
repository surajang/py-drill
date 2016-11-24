# -*- coding: UTF-8 -*-
import fibo #test for module import
import random
import hero
import sys
from colorama import Fore, Back, Style, init

init()
user = hero.hero("용사")

class bcolors:
    """testing color formatting"""
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.PURPLE + "PURPLE" + bcolors.ENDC
print bcolors.BLUE + "BLUE" + bcolors.ENDC
print bcolors.GREEN + "GREEN" + bcolors.ENDC
print bcolors.YELLOW + "WARNING" + bcolors.ENDC
print bcolors.RED + "FAIL" + bcolors.ENDC
print bcolors.BOLD + "BOLD" + bcolors.ENDC
print bcolors.UNDERLINE + "UNDERLINE" + bcolors.ENDC

def intro():
    """print title text-thingy stuff on start. + Initializing process"""
    print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    print "#      WTF RPG WORLD         #"
    print "# somewhat like retro game.. #"
    print "# 한글도 나올 수 있나요?     #"
    print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    print ""
    print bcolors.PURPLE + "[안내원] 환영합니다, 낯선 여행자님. 당신은 누구신가요?" + bcolors.ENDC
    userInputName = raw_input("이름을 입력하세요: ")
    user.setUserName(userInputName) #create player profile
    print "[안내원] 만나서 반갑습니다,",user.getUserName() + "."

intro()

def mainMenu():
    """Main menu. All game play starts from here and comes back to here."""
    while True:
        userInput = raw_input("[MAIN] (M)이동 (S)상태 (I)인벤토리 (V)지도 (Z)기타: ") #main menu mockup

        if userInput in ('M', 'm'):
            print "Let's get move!"
            pass #place move feature call here
            break
        elif userInput in ('I', 'i'):
            print "Take a look at your inventory..."
            pass #place inventory feature call here
            break
        elif userInput in ('S', 's'):
            user.stat() #display player's status and come back to main menu
        elif userInput in ('V', 'v'):
            print "Here's your map."
            pass #place mapview feature call here
            break
        elif userInput in ('Z', 'z'):
            print "other menus."
            optionMenu()
            pass #place other menu call here
            break
        else:
            print "try again"

def optionMenu():
    """Option menu. Provides misc. features."""
    while True:
        userInput = raw_input("[OPTION] (B)메인메뉴 (L)불러오기 (S)저장 (H)도움말 (Q)종료: ") #main menu mockup

        if userInput in ('B', 'b'):
            mainMenu() #Back to main
            break
        elif userInput in ('L', 'l'):
            print "Load previous play..."
            pass #place loading feature call here
            break
        elif userInput in ('S', 's'):
            pass #Save game
            mainMenu()
            break
        elif userInput in ('H', 'h'):
            print "Help!!!"
            pass #place mapview feature call here
            mainMenu()
            break
        elif userInput in ('Q', 'q'):
            print "Good bye."
            sys.exit(0)
            break
        else:
            print "try again"

mainMenu()
