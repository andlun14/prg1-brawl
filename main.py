import random
import sys
import time
from pynput import keyboard

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
currentdir = 0
playerx = 10

def render(x, ex):
    clear()
    for a in range(4):
        for b in range(x):
            sys.stdout.write(" ")
       
        sys.stdout.write(char[a])

        for b in range(ex + 20 - x):
            sys.stdout.write(" ")

        sys.stdout.write(en[a])

        sys.stdout.write("\n")
    sys.stdout.flush()


def on_press(key):
    global currentdir
    if key == keyboard.Key.left:
        currentdir = -1
    if key == keyboard.Key.right:
        currentdir = 1

def on_release(key):
    global currentdir
    if key in (keyboard.Key.left, keyboard.Key.right):
        currentdir = 0

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()


while True:
    print(currentdir)
    if currentdir == 1 and playerx < 30:
        playerx += 1
    elif currentdir == -1 and playerx > 0:
        playerx -= 1
    render(playerx, 0)
    print(playerx)
    time.sleep(0.05)