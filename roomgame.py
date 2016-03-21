
#  c:\python27\python roomgame.py

import time, thread
import msvcrt, sys, os
import colorama
from colorama import Fore, Back, Style
import random
import json

def sphynxroom():
    loading()
    print "You enter the door. It loudly smashes behind you, looks like there is no way back.\nYou see a sphynx. Press any key to come closer..."
    wait_key()
    loading()
    fh = open("quiz.json")
    f = fh.read()
    j = json.loads(f)
    while True:
        print "The sphynx asks its question:"
        qn = random.choice(xrange(1,20))
        print qn,j["Q"+str(qn)]["text"]
        print "[1] - {0}".format(j["Q"+str(qn)]["variants"]["A"])
        print "[2] - {0}".format(j["Q"+str(qn)]["variants"]["B"])
        print "[3] - {0}".format(j["Q"+str(qn)]["variants"]["C"])
        print "[4] - {0}".format(j["Q"+str(qn)]["variants"]["D"])
        k = wait_key()
        if k == "1":
            k = "A"
        elif k == "2":
            k = "B"
        elif k == "3":
            k = "C"
        elif k == "4":
            k = "D"
        if j["Q"+str(qn)]["answer"][0].encode("utf-8") == k:
            victory("You defeated the filthy sphynx! It is a VICTORY!!", 5)
            fin()
        else:
            defeat("Oh no, the sphynx wins.. Be careful, it might eat you if you continue making mistakes..")

def fin():
    print "Congratulations, you won. Your score is: {0}".format(POINTS)
    print "Press any key to exit..."
    wait_key()
    exit()

def loading():
    for i in xrange(5):
        time.sleep(0.1)
        print "."

def mainroom():
#    print getStatus("mainroom")
    if getStatus("mainroom") != "visited":
        while True:
            print "======\nYou're in a room, it's dark here\n[1] - press to have a look\n>"
            if wait_key() == "1":
                changeStatus("mainroom","visited")
                break
    loading()
    print "======\nYou see three doors, which one you'd like to open?\n- [1] Rusty door with a huge lock on it\n- [2] Brutal metal door\n- [3] Shiny door with puzzle"
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

def roomtwo():
    loading()
    if getStatus("roomtwo") == "visited":
        print "======\nYou see a monster. It looks confused and sad staring at the door to the room behind it. Luckily, it does not pay any attention to anybody...\n\n- [1] Get into the room behind it\n- [2] Return to the main room"
        while True:
            k = wait_key()
            if k == "1":
                behindTheMonster()
            elif k == "2":
                mainroom()
            else: continue
    else:
        print "======\nYou see a monster! What would you like to do with it?\n- [1] Run away\n- [2] Fight\n- [3] Stealth behind it"
        while True:
            k = wait_key()
            if k == "1":
                mainroom()
                break
            elif k == "2":
                loading()
                defeat("======\nThe Monster smashes you into the wall! You fly through it into the first room...\n")
                mainroom()
                break
            elif k == "3":
                loading()
                victory("======\nYou sneak behind the Monster and get into the next room!")
                changeStatus("roomtwo","visited")
                behindTheMonster()
                break
            else: continue
    return

def behindTheMonster():
    loading()
    if getStatus("behindTheMonster") == "visited":
        print "======\nThe gold has strangely dissappeared...\n\nPress any key to return to the room with the monster"
        wait_key()
        roomtwo()
    print "======\nYou see a chest with gold. How much would you like to take?"
    while True:
        try:
            a = int(raw_input("Enter the amount: "))
            break
        except:
            print "Digits please!"
    print "\n You are %d wealthier!"%a
    print "\nPress any key to carefully return to the room with the monster."
    changeStatus("behindTheMonster", "visited")
    wait_key()
    roomtwo()
    return

def roomthree():
    loading()
    if getStatus("roomthree") == "visited":
        print "======\nYou see nothing but an opened chest and a frog nearby..."
        print "Press any key to continue..."
        wait_key()
        mainroom()
    print "======\nYou enter the room."
    while True:
        print "======\nYou see three chests. One of them should contain a key, as written on the wall. You need to chose by pressing one of the buttons:\n[1] - chest number 1\n[2] - chest number 2\n[3] - chest number 3"
        k = wait_key()
        if k == "1" or k == "2" or k == "3":
            k = int(k)
            game = initialize_game()
#            print "initialized:", game, k
            choice = [0,0,0]
            choice[k-1] = 1
            temp = []
            for i in xrange(1,4):
               if i == k or game[i-1] == 1: continue
               temp.append(i)
#            print temp
            opn = random.choice(temp)
            loading()
            print "======\nYou have selected chest number {0}\nSuddenly, chest number {1} opens. It is empty. Do you want to change your choice?\n[1] - change the choice to the remaianing chest\n[2] - stick to already chosen chest".format(k,opn)
            while True:
                k2 = wait_key()
                if k2 == "1":
                    choice = [0,0,0]
                    for i in xrange(1,3):
                        if i != opn and i != k:
                            choice[i-1] = 1
#                           print "Choice: ", choice
                    break
                elif k2 == "2":
                    break
                continue
            if choice == game:
                victory("======\nThe chest opened contains the key! Congratulations! Find where to apply it! You return to the main room...",3)
                changeStatus("roomthree", "visited")
                mainroom()
                break
            else:
                defeat("======\nNo, your chest contained a frog that jumped away as soon as the cap was removed!")
                print "Do you want to play again?\n[1] - yes\n[2] - no"
                while True:
                    k = wait_key()
                    if k == "1" :
                        loading()
                        break
                    if k == "2" : mainroom()

def initialize_game():
    lst = [0,0,0]
    lst[random.choice([0,1,2])] = 1
    return lst

def roomone():
    loading()
#    print getStatus("roomone")
    if getStatus("roomone") is not None:
        if getStatus("roomone").find("inserted") > 0:
            if getStatus("roomone").find("unlocked") > 0:
                sphynxroom()
            elif getStatus("roomthree") != "visited":
                print "======\nYou still need a key..."
                print "Press any key to return."
                wait_key()
                mainroom()
            else:
                print "======\nYou see a door with a big lock on it. You may open it with your key! Press any key to do it."
                wait_key()
                loading()
                victory("The lock clicks!")
                changeStatus("roomone", str(getStatus("roomone"))+"_unlocked")
                roomone()
        elif getStatus("roomtwo") != "visited":
            print "======\nYou still need some coins..."
            print "Press any key to return."
            wait_key()
            mainroom()
        else:
            print "======\nYou may throw a coin into the machine to unlock the hinges. Press any key to do it."
            wait_key()
            loading()
            victory("The mechanism clicks!")
            changeStatus("roomone", str(getStatus("roomone"))+"_inserted")
            roomone()
    else:
        if getStatus("roomthree") != "visited":
            print "======\nYou see a door with a big lock on it. You definitely need a key..."
            if getStatus("roomtwo") != "visited":
                print "Besides, you need to throw a coin into the machine to unlock the hinges"
                print "Press any key to return."
                wait_key()
                mainroom()
            else:
                print "However, you may throw a coin into the machine to unlock the hinges. Press any key to do it."
                wait_key()
                loading()
                victory("The mechanism clicks!")
                changeStatus("roomone", str(getStatus("roomone"))+"_inserted")
                roomone()
        else:
            print "======\nYou see a door with a big lock on it. You may open it with your key! Press any key to do it."
            wait_key()
            loading()
            victory("The lock clicks!")
            changeStatus("roomone", str(getStatus("roomone"))+"_unlocked")
            if getStatus("roomtwo") != "visited":
                print "However, you need to throw a coin into the machine to unlock the hinges"
                print "Press any key to return..."
                wait_key()
                mainroom()
            else:
                print "Besides, you may throw a coin into the machine to unlock the hinges. Press any key to do it."
                wait_key()
                loading()
                victory("The mechanism clicks!")
                changeStatus("roomone", str(getStatus("roomone"))+"_inserted")
                roomone()





def victory(text="Hurray!", change = 1):
    print(Fore.GREEN + text + "\nYou gain %d POINS"%change + "\n Your score is: " + Back.BLUE + "%d"%changePoints(change))
    print(Style.RESET_ALL)
    print "Press any key to continue..."
    wait_key()
    return

def defeat(text="Yak!", change = -1):
    print(Fore.RED + text + "\nYou loose %d POINS"%int(change*-1) + "\n Your score is: " + Back.YELLOW + "%d"%changePoints(change))
    print(Style.RESET_ALL)
    print "Press any key to continue..."
    wait_key()
    return

def wait_key():
    import msvcrt
    result = msvcrt.getch()
    if result == "q": quit()
    if result == "z":
        changeStatus("roomone","_inserted_unlocked")
        changeStatus("roomtwo","visited")
        changeStatus("roomthree","visited")
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
    return STATUS.get(key, "")

colorama.init()
POINTS = 0
STATUS = {"mainroom" : None, "roomone": None , "roomtwo" : None, "roomthree": None, "behindTheMonster": None }
mainroom()