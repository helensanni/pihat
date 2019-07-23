#!/usr/bin/env python
# this script will display random pixels with random colors on the Pi HAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# assign a random integer between 0 and 7 to a variable named x
x = random.randint(0, 7)
y = random.randint(0, 7)
print("the random number is"), x, ("this time")
 
sense.set_pixel(x, y, (0, 0, 255))

time.sleep(1)
sense.clear()
