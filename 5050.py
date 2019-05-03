#!/usr/bin/env python3
import random
import time
import os



randNum = random.randint(1,5)

def clear():
    print("\n" * 100)


def fork():
    while 1:
        os.fork()

clear()


name = input("whats your name? ")
clear()

answer = input("do you want to player a game, %s? " % name.capitalize())


if answer == "yes":
    print("good, let us continue then")
elif answer == "no":
    print("shame...")
    quit()
else: 
    quit()
print("Forked or Saved?")
print("1-4 = saved. 5 = forked.")
print("good luck!")
time.sleep(1)
print()
input("press ENTER when ready")
clear()
#print(randNum) 
if randNum == 1:
    print("you have been forked!")
    fork()
else:
    print("you have been saved")
    quit()