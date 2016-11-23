# -*- coding: UTF-8 -*-
import fibo #test for module import
import random
import hero

def intro():
    """print title text-thingy stuff on start."""
    print "##############################"
    print "#      WTF RPG WORLD         #"
    print "# somewhat like retro game.. #"
    print "# 한글도 나올 수 있나요?     #"
    print "##############################"
    print ""

intro()

print "[안내원] 환영합니다, 낯선 여행자님. 당신은 누구신가요?"
userInputName = raw_input("이름을 입력하세요: ")
user = hero.hero(userInputName) #create player profile
print "[안내원] Ah, nice to meet you,",user.getUserName() + "."

user.stat() # display user status
userInput = raw_input("(M)이동 (I)인벤토리 (V)지도 (Z)기타: ") #main menu mockup
print "##Debug## userInput =", userInput
