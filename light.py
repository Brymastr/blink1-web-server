__author__ = 'Brycen'

from blink1.blink1 import blink1
import time

# b1 = Blink1()


def blink():
    with blink1() as b1:
        print("blink!")
        for i in range(5):
            b1.fade_to_rgb(10, 255, 255, 255)
            time.sleep(.1)
            b1.fade_to_rgb(10, 0, 0, 0)
            time.sleep(.1)


