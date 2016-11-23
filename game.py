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

intro()
print "환영합니다, 낯선 여행자님. 당신은 누구신가요?"
var = raw_input("이름을 입력하세요: ")
print "Ah, nice to meet you,",var + "."

fibo.fib(2000) #just for test
print fibo.fib.__doc__
print "Random number(0-100):", random.randrange(100)
