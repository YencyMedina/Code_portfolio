import time
import board
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = .5)

defcolor = [216, 231, 0]
red = [255, 0, 0]
black = [0,0,0]
white = [255,255,255]
blue = [0,0,255]
green = [0,255,0]
purple = [255,0,255]

color1 = [defcolor[0],defcolor[1],defcolor[2]]
np.fill(color1)
def fade_out(defcolor, delay = 0.005):
    fadeR = defcolor[0]/256.0
    fadeG = defcolor[1]/256.0
    fadeB = defcolor[2]/256.0
    for i in range(256):
        color1[0] = int (defcolor[0] - (fadeR*i))
        color1[1] = int (defcolor[1] - (fadeG*i))
        color1[2] = int (defcolor[2] - (fadeB*i))
        np.fill(color1)
        print(i, defcolor,fadeR*i,fadeG*i,fadeB*i)
        time.sleep(delay)
        np.show()

def fade_in(defcolor, delay = 0.005):
    fadeR = defcolor[0]/256.0
    fadeG = defcolor[1]/256.0
    fadeB = defcolor[2]/256.0
    for i in range(256):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        print(i, defcolor,fadeR*i,fadeG*i,fadeB*i)
        time.sleep(delay)
        np.show()
        
def sparkle(fgcolor = white, bgcolor = black, delay = 0.005, num_sparks = 10):
    for i in range(50):
        np.fill(bgcolor)
        np.show()
        for j in range(num_sparks):
            rand_int = random.randrange(0, 30)
            np[rand_int] = fgcolor
            np.show()
        time.sleep(delay)
        np[rand_int] = bgcolor
        np.show()
        
        
def chase(fgcolor = green, bgcolor = purple, speed = 0.001):
    for j in range(100):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = fgcolor
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = bgcolor
                print("fColor",i,np[i])
            time.sleep(speed)


while True:
    fade_out(purple)
    fade_in(green)
    fade_out(green)
    fade_in(purple)
    fade_out(purple)
    fade_in(green)
    sparkle(purple, green, 0.01, 5)
    fade_out(green)
    fade_in(purple)
    chase()