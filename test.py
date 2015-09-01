__author__ = 'Brycen'
from blink1.blink1 import blink1
import time
with blink1() as b1:
    for i in range(5):
        b1.fade_to_color(100, 'green')
        time.sleep(.8)
        b1.fade_to_color(100, 'black')
        time.sleep(.8)
