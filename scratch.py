# -*- coding: UTF-8 -*-
# Just for test & memo... Nothing related to actual project.

def fib(n):
    """print a Fibonacci series"""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b

# class bcolors:
#     """testing color formatting"""
#     PURPLE = '\033[95m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
# print bcolors.PURPLE + "PURPLE" + bcolors.ENDC
# print bcolors.BLUE + "BLUE" + bcolors.ENDC
# print bcolors.GREEN + "GREEN" + bcolors.ENDC
# print bcolors.YELLOW + "WARNING" + bcolors.ENDC
# print bcolors.RED + "FAIL" + bcolors.ENDC
# print bcolors.BOLD + "BOLD" + bcolors.ENDC
# print bcolors.UNDERLINE + "UNDERLINE" + bcolors.ENDC
