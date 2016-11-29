# -*- coding: UTF-8 -*-
import hero
import sys
from colorama import Fore, Back, Style, init
# some imports...

def clearScreen():
    sys.stderr.write("\x1b[2J\x1b[H") #Clear Terminal screen. May not work in Windows client?

def introTitle():
    """Draw main title with ascii graphic... Just for fancy looking :) """
    clearScreen()
    print "12345678901234567890123456789012345678901234567890123456789012345678901234567890" #Ruler for 80-char terminal width
    print Back.RED + ""
    print "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                             ┃"
    print "┃    ██▓███ ▓██   ██▓ ██▀███   ▒█████   ▒█████   ███▄ ▄███▓   ┃"
    print "┃   ▓██░  ██▒▒██  ██▒▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒   ┃"
    print "┃   ▓██░ ██▓▒ ▒██ ██░▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▓██    ▓██░   ┃"
    print "┃   ▒██▄█▓▒ ▒ ░ ▐██▓░▒██▀▀█▄  ▒██   ██░▒██   ██░▒██    ▒██    ┃"
    print "┃   ▒██▒ ░  ░ ░ ██▒▓░░██▓ ▒██▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒   ┃"
    print "┃   ▒▓▒░ ░  ░  ██▒▒▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░   ┃"
    print "┃   ░▒ ░     ▓██ ░▒░   ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░   ┃"
    print "┃   ░░       ▒ ▒ ░░    ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░      ┃"
    print "┃            ░ ░        ░         ░ ░      ░ ░         ░      ┃"
    print "┃            ░ ░                                              ┃"
    print "┃                 GET THE HELL OUT OF THERE!                  ┃"
    print "┃               PyROOM project by surajang 2016               ┃"
    print "┃                                                             ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"
    print Style.RESET_ALL + ""

def welcomeProcess():
    """Welcoming user process"""
    print "Select menu to start."
    print "(N)New game (R)Ranking : "

    userInputName = raw_input("이름을 입력하세요: ")
    user.setUserName(userInputName) #create player profile
    print "[안내원] 만나서 반갑습니다,",user.getUserName() + "."

def showMap():
    """Display the map of current room. May contains graphical data..?"""
    print "   1 2 3 4 5 6 7 8 9 0 "
    print "1 #####################"
    print "2 # | | | | | | | | | #"
    print "3 # | |$| | | | | | | #"
    print "4 # | | | |X| | | | | #"
    print "5 @ | | | | | | | | | @"
    print "6 @ | | | | | | | | | @"
    print "7 # | | | | | | | | | #"
    print "8 # | | | | | | |O| | #"
    print "9 # | | | | | | | | | #"
    print "0 # | | | | | | | | | #"
    print "  #####################"

def mainMenu():
    """Main menu. All game play starts from here and comes back to here."""
    while True:
        userInput = raw_input("(M)이동 (S)상태 (I)인벤토리 (V)지도 (Z)기타: ") #main menu mockup

        if userInput in ('M', 'm'):
            print "Let's get move!"
            pass #place move feature call here
        elif userInput in ('I', 'i'):
            print "Take a look at your inventory..."
            pass #place inventory feature call here
        elif userInput in ('S', 's'):
            user.stat() #display player's status and come back to main menu
        elif userInput in ('V', 'v'):
            showMap()
        elif userInput in ('Z', 'z'):
            optionMenu()
            pass #place other menu call here
            break
        else:
            print "try again"

def optionMenu():
    """Option menu. Provides misc. features."""
    while True:
        userInput = raw_input(Back.GREEN + "[OPTION]"+ Back.RESET + " (B)메인메뉴 (S)저장 (R)Ranking (H)도움말 (Q)종료: ") #main menu mockup

        if userInput in ('B', 'b'):
            mainMenu() #Back to main
            break
        elif userInput in ('R', 'r'):
            clearScreen()
            print "Ranking chart..."
            print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            print "| # |    NAME    | Playtime | Moves | Message        "
            print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            print "| 1 | userName   | 12:22:30 | 325   | WTF!!!        |"
            print "| 2 | userName2  | 12:22:30 | 807   | LOL           |"
            print "| 3 | userName3  | 12:22:30 | 423   | Nah...        |"
            print "| 4 | userName4  | 12:22:30 | 112   | So be it.     |"
            print "| 5 | userName5  | 02:02:30 |  25   | :D            |"
            print "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            print "(1/3 pages) (B)y Time (C)ontinue (E)xit: "
            pass #place Ranking table call here
            mainMenu()
            break
        elif userInput in ('S', 's'):
            pass #Save game
            print "saving..."
            mainMenu()
            break
        elif userInput in ('H', 'h'):
            print "Help!!!"
            pass #place mapview feature call here
            mainMenu()
            break
        elif userInput in ('Q', 'q'):
            print "Good bye."
            pass #Place quit sequence (confirm --> quit)
            sys.exit(0)
            break
        else:
            print "try again"

init()  #Initialize Colorama
user = hero.hero()
introTitle()
welcomeProcess()
mainMenu()
