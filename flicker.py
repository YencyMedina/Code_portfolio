import time
import board
import neopixel
import random

NUM_PIXELS = 30
np = neopixel.NeoPixel(board.D2, NUM_PIXELS, auto_write = False, brightness = .2)

red = (255, 0, 0)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
purple = (255,0,255)
yellow = (255, 100, 0)
orangeT = (255, 80, 0)
orange = (255, 64, 0)
lightBlue = (87, 232, 255)
lightpurple = (227, 98, 255)
darkpurple = (18,0,18)
defcolor = [orange, yellow, orangeT]
randcolor = random.choice(defcolor)
defcolor2 = [lightBlue, lightBlue, white]
randcolor2 = random.choice(defcolor2)

def fire(fgcolor = white, bgcolor = black, num_sparks = 15):
    for i in range(50):
        np.fill(bgcolor)
        np.show()
        for j in range(num_sparks):
            randcolor = random.choice(defcolor)
            rand_int = random.randrange(0, 30)
            rand_intT = random.randrange(0, 30)
            randomsleep = random.random()/100
            np[rand_int] = fgcolor
            np[rand_intT] = black
            np.show()
            time.sleep(randomsleep)
        np[rand_int] = bgcolor
        np.show()
        
def lightning(bgcolor = darkpurple, flash = randcolor2, numpix = np.n):
    for i in range(50):
        randomsleep = random.random()*10
        randompix = random.randrange(1,5)
        print("sleep", randomsleep)
        np.fill(bgcolor)
        np.show()
        time.sleep(randomsleep)
        for j in range(randompix):
            np.fill(flash)
            np.show()
            time.sleep(0.05)
            np.fill(bgcolor)
            np.show()
            time.sleep(0.01)

while True:
    #fire(randcolor, red)
    lightning()