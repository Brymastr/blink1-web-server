from blink1.blink1 import blink1
import time


def busy():
    activate(232, 66, 244)


def success():
    activate(22, 226, 172)


def failure():
    activate(232, 34, 0)


def unstable():
    activate(232, 146, 0)


def activate(r, g, b):
    print("activate")
    with blink1() as b1:
        for i in range(5):
            b1.fade_to_color(100, (r, g, b))
            time.sleep(.8)
            b1.fade_to_color(100, (0, 0, 0))
            time.sleep(.8)
