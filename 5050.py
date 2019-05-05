#!/usr/bin/env python3
import random
import time
import os



randNum = random.randint(1,2)

def clear():
    print("\n" * 100)

def smallClear():
    print("\n" * 5)

def fork():
    while 1:
        os.fork()

clear()

print("name debug for debugging")
name = input("whats your name? ")
clear()
answer = input("do you want to player a game, %s? " % name.capitalize())


if answer == "yes":
    print("good, let us continue then")
elif answer == "no":
    print("you wouldn't have won anyways.")
    quit()
elif answer == "nah mate":
    print("NO JOKING!")
    quit()
else:
    print("FATAL ERROR. SHUTTING DOWN GAME!")
    quit()

print("Forked or Saved?")
print("1 = Saved. 2 = Forked")
print("good luck!")
time.sleep(1)
print()
input("press ENTER when ready")
clear()

if name == "debug":
    print(randNum) 

if randNum == 1:
    print("you have been forked!")
    #fork()
else:
    print("you have been saved")
    quit()