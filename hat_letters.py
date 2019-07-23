#!/usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

sense.show_letter("H", red)
time.sleep(1)
sense.show_letter("i", white)
time.sleep(1)
sense.show_letter("!", blue)
sense.show_letter("T", red)
time.sleep(1)
sense.show_letter("e", red)
time.sleep(1)
sense.show_letter("x", red)
time.sleep(1)
sense.show_letter("a", red)
time.sleep(1)
sense.show_letter("s", red)
time.sleep(1)
sense.show_letter("H", red)
time.sleep(1)
sense.show_letter("H", red)
time.sleep(1)
sense.show_letter("H", red)
time.sleep(1)
time.sleep(1)
sense.clear()
