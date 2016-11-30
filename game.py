# -*- coding: UTF-8 -*-
import hero
import sys
import time
from colorama import Fore, Back, Style, init
# some imports...

def clear_screen():
    #sys.stderr.write("\x1b[2J\x1b[H") #Clear Terminal screen. May not work in Windows client?
    print(chr(27) + "[2J") #Don't know why this one makes extra linebreak???!

def intro_title():
    """Draw main title with ascii graphic... Just for fancy looking :) """
    #clear_screen()
    print(Back.RED)
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                             ┃")
    print("┃    ██▓███ ▓██   ██▓ ██▀███   ▒█████   ▒█████   ███▄ ▄███▓   ┃")
    print("┃   ▓██░  ██▒▒██  ██▒▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒   ┃")
    print("┃   ▓██░ ██▓▒ ▒██ ██░▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▓██    ▓██░   ┃")
    print("┃   ▒██▄█▓▒ ▒ ░ ▐██▓░▒██▀▀█▄  ▒██   ██░▒██   ██░▒██    ▒██    ┃")
    print("┃   ▒██▒ ░  ░ ░ ██▒▓░░██▓ ▒██▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒   ┃")
    print("┃   ▒▓▒░ ░  ░  ██▒▒▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░   ┃")
    print("┃   ░▒ ░     ▓██ ░▒░   ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░   ┃")
    print("┃   ░░       ▒ ▒ ░░    ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░      ┃")
    print("┃            ░ ░        ░         ░ ░      ░ ░         ░      ┃")
    print("┃            ░ ░                                              ┃")
    print("┃                 GET THE HELL OUT OF THERE!                  ┃")
    print("┃             PyROOM project by (c)surajang 2016              ┃")
    print("┃                 Published under MIT License                 ┃")
    print("┃                                                             ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(Style.RESET_ALL)

def welcome_menu():
    """Welcoming-user menu.
    Provide sign-up, login, ranking view features.
    Sign-up and login feature: user DB required, but not yet implemented :(
    """

    while True:
        welcomeMenuInput = input("(N)ew (L)ogin (R)anking :")
        if welcomeMenuInput in ('N', 'n'):
            print("new game!!!")
            create_new_user()
            break
        elif welcomeMenuInput in ('L', 'l'):
            print("Login process")
        elif welcomeMenuInput in ('R', 'r'):
            view_ranking()
        else:
            print("Wrong input. try again")

def create_new_user():
    """Do new user sign-up process.
    Get User name, PW(TBD) from user and save them to DB
    Advance user to corresponding stage (which is #1)
    """
    userInputName = input("Enter player name: ")
    user.set_user_name(userInputName) #create player profile
    print("Welcome," + user.get_user_name() + ".")
    print(time.time())
    user.set_play_start_time(time.time())
    pass #Now, pass the user to the stage #1 room.
    stage_dispatcher(user.get_current_stage())

def stage_dispatcher(roomNumber):
    """Send user to requested stage room
    roomNumber arg. is required.
    """
    print(user.get_user_name() + " is now entering room #" + str(roomNumber))
    pass #call stage1 story

def show_map():
    """Display the map of current room. May contains graphical data..?"""
    print("   1 2 3 4 5 6 7 8 9 0 ")
    print("1 #####################")
    print("2 # | | | | | | | | | #")
    print("3 # | |$| | | | | | | #")
    print("4 # | | | |X| | | | | #")
    print("5 @ | | | | | | | | | @")
    print("6 @ | | | | | | | | | @")
    print("7 # | | | | | | | | | #")
    print("8 # | | | | | | |O| | #")
    print("9 # | | | | | | | | | #")
    print("0 # | | | | | | | | | #")
    print("  #####################")

def main_menu():
    """Main menu. All game play starts from here and comes back to here."""
    while True:
        userInput = input("(M)ove (S)tat (I)nventory (V)iew Map (Z)Etc. :") #main menu mockup

        if userInput in ('M', 'm'):
            print("Let's get move!")
            pass #place move feature call here
        elif userInput in ('I', 'i'):
            print("Take a look at your inventory...")
            pass #place inventory feature call here
        elif userInput in ('S', 's'):
            user.get_status() #display player's status and come back to main menu
        elif userInput in ('V', 'v'):
            show_map()
        elif userInput in ('Z', 'z'):
            option_menu()
            break
        else:
            print("try again")

def option_menu():
    """Option menu. Provides misc. features."""
    while True:
        userInput = input(Back.GREEN + "[OPTION]"+ Back.RESET + " (B)ack (S)ave (R)anking (H)elp (Q)uit: ") #main menu mockup

        if userInput in ('B', 'b'):
            main_menu() #Back to main
            break
        elif userInput in ('R', 'r'):    #View ranking
            view_ranking()
        elif userInput in ('S', 's'):    #Save current game status
            pass #Save game
            print("saving...")
        elif userInput in ('H', 'h'):    #View Help
            print("Help!!!")
            pass #place mapview feature call here
        elif userInput in ('Q', 'q'):    #Quit game
            exit_game()
        else:
            print("try again")

def exit_game():
    """Do game-exiting process"""
    while True:
        exitConfirm = input("Are you sure to quit game(Y/N)?: ")
        if exitConfirm in ('Y', 'y'):
            pass #Check play time of current session and add to total play time
            pass #Check moveCount of current session and add to total moveCount
            pass #Check current stage and update to player's profile
            print("Good bye.")
            sys.exit(0)
        else:
            print("Nope... get back...")
            break

def view_ranking():
    """Display Rank table"""
    #clear_screen()
    print("Ranking chart...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("| # |    NAME    | Playtime | Moves | Message        ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("| 1 | userName   | 12:22:30 | 325   | WTF!!!        |")
    print("| 2 | userName2  | 12:22:30 | 807   | LOL           |")
    print("| 3 | userName3  | 12:22:30 | 423   | Nah...        |")
    print("| 4 | userName4  | 12:22:30 | 112   | So be it.     |")
    print("| 5 | userName5  | 02:02:30 |  25   | :D            |")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("(1/3 pages) (B)y Time (C)ontinue (E)xit: ")
    pass #place Ranking table call here

init()  #Initialize Colorama
user = hero.Hero() #create/Initialize user profile
intro_title() #Draw intro title
welcome_menu()
main_menu()
