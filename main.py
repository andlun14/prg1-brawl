import random
import sys
import time

# Startvärdena väljer du själv.
spelare_hp = 100
fiende_hp = 80

# Ditt första kort börjar här.

def slowPrint(string, speed=0.075):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    time.sleep(0.2)

def clear():
    print("\033[H\033[J", end="")

char = [
    r"  `o^     ",
    r"^\/0\_+---",
    r"  /O\     ",
    r" _| /_    "
]
en = [
    r"     ^o´  ",
    r"---+_/0\/^",
    r"     /0\  ",
    r"    _\ |_ "
]

def render(x, ex, y):
    global spelare_hp, fiende_hp
    clear()
    sys.stdout.write(f"hp: {spelare_hp}")
    for i in range(0, 20 - (4 + len(str(spelare_hp)))):
        sys.stdout.write(" ")
    sys.stdout.write(f"fiende hp: {fiende_hp}")
    sys.stdout.write("\n")
    for a in range(4):
        for b in range(x):
            sys.stdout.write(" ")

        if y == 1 and a == 1:
            sys.stdout.write(" ")
        sys.stdout.write(char[a])

        if y == 1 and a == 1:
            for b in range(ex + 19 - x):
                sys.stdout.write(" ")
        else:
            for b in range(ex + 20 - x):
                sys.stdout.write(" ")
        if y != 3:
            sys.stdout.write(en[a])

        sys.stdout.write("\n")
    sys.stdout.flush()

def anim(x):
    if x == 0:
        for i in range(0, 10):
            render(10 + i, 0, 0)
            time.sleep((1.2 ** i)/10)
        for i in range(1, 3):
            render(19, 0, 1)
            time.sleep(0.2)
            render(19, 0, 0)
            time.sleep(0.2)
        for i in range(1, 3):
            render(19, 0, 3)
            time.sleep(0.4)
            render(19, 0, 0)
            time.sleep(0.4)
anim(0)