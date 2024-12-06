from getch import getch
from time import time
import os

os.system('clear')
i = 0

while True:
    move = getch().lower()
    print("\033[K", end="\r")
    if move == "w":
        print("up", end="\r")
    elif move == "a":
        print("left", end="\r")
    elif move == "s":
        print("down", end="\r")
    elif move == "d":
        print("right", end="\r")
    else:
        pass
    i += 1
    
    if i%4 == 0:
        start = time()
        print("Press space to parry", end="\r")
        parry = getch()
        print("\033[K", end="\r")
        end = time()

        if end - start < 1 and parry == ' ':
            print("You parried the attack", end="\r")
        else:
            print("You took the hit", end="\r") 

    
    