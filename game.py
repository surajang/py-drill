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
var = raw_input("What's your name, hero? : ")
print "Ah, nice to meet you,",var,"."

fibo.fib(2000) #just for test
print fibo.fib.__doc__
print "Random number(0-100):", random.randrange(100)
