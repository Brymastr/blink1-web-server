from blink1.blink1 import blink1
import time

from blink1.blink1 import Blink1
b2 = Blink1()


def busy():
    activate('purple')


def success():
    activate('cyan')


def failure():
    activate('red')


def unstable():
    activate('orange')


def activate(color):
    print("activate: " + color)
    try:
        # b2.fade_to_rgb(1000, 255, 255, 255)
        with blink1() as b1:
            for i in range(5):
                b1.fade_to_color(100, color)
                time.sleep(.8)
                b1.fade_to_color(100, 'black')
                time.sleep(.8)
    except Exception as err:
        print(type(err))
        raise
