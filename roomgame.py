
#  c:\python27\python roomgame.py

import time, thread
import msvcrt, sys, os
import colorama
from colorama import Fore, Back, Style

def loading():
    for i in xrange(5):
        time.sleep(0.05)
        print "."

def mainroom():
#    print getStatus("mainroom")
    if getStatus("mainroom") != "visited":
        while True:
            print "======\nYou're in a room, it's dark here\nPress [q] to have a look\n>"
            if wait_key() == "q":
                changeStatus("mainroom","visited")
                break
    loading()
    print "======\nYou see three doors, which one you'd like to open?\n- [1] Brutal metal door \n- [2] Shiny door with puzzle\n- [3] Bronze door with a huge lock on it"
    while True:
        k = wait_key()
        if k == "1":
            roomone()
            break
        elif k == "2":
            roomtwo()
            break
        elif k == "3":
            roomthree()
            break
        else: continue
    return

def roomone():
    loading()
    if getStatus("roomone") == "confused":
        print "======\nYou see a monster. It looks confused and sad staring at the door to the room behind it. Luckily, it does not pay any attention to anybody...\n\n- [n] Get into the room behind it\n- [q] Return to the main room"
        while True:
            k = wait_key()
            if k == "n":
                behindTheMonster()
            elif k == "q":
                mainroom()
            else: continue
    else:
        print "======\nYou see a monster! What would you like to do with it?\n- [r] Run away\n- [f] Fight\n- [s] Stealth behind it"
        while True:
            k = wait_key()
            if k == "r":
                mainroom()
                break
            elif k == "f":
                loading()
                defeat("======\nThe Monster smashes you into the wall! You fly through it into the first room...\n")
                mainroom()
                break
            elif k == "s":
                loading()
                victory("======\nYou sneak behind the Monster and get into the next room!")
                changeStatus("roomone","confused")
                time.sleep(6)
                behindTheMonster()
                break
            else: continue
    return

def roomtwo():
    print "two"

def roomthree():
    print "three"


def behindTheMonster():
    loading()
    if getStatus("behindTheMonster") == "visited":
        print "======\nThe gold has strangely dissappeared...\n\nYou return to the room with the monster"
        roomone()
    print "======\nYou see a chest with gold. How much would you like to take?"
    while True:
        try:
            a = int(raw_input("Enter the amount: "))
            break
        except:
            print "Digits please!"
    print "\n You are %d wealthier!"%a
    print "\nYou carefully return to the room the monster."
    time.sleep(6)
    changeStatus("behindTheMonster", "visited")
    roomone()
    return

def victory(text="Hurray!", change = 1):
    print(Fore.GREEN + text + "\n\nYour score is:%d"%changePoints(change))
    print(Style.RESET_ALL)
    return

def defeat(text="Yak!", change = -1):
    print(Fore.RED + text + "Your score is: " + Back.YELLOW + "%d"%changePoints(change))
    print(Style.RESET_ALL)
    print "Press any key to continue..."
    wait_key()
    return

def wait_key():
    import msvcrt
    result = msvcrt.getch()
    if result == "z": quit()
    return result

def changePoints(i = 0):
    global POINTS
    POINTS = POINTS + i
    return POINTS

def changeStatus(key, value):
    global STATUS
    STATUS[key] = value

def getStatus(key):
    global STATUS
    return STATUS.get(key, None)

colorama.init()
POINTS = 0
STATUS = {"mainroom" : None, "roomone": None , "roomtwo" : None, "roomthree": None, "behindTheMonster": None }
mainroom()