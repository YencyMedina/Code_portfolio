import time
import board
import neopixel
import random

np = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write = False, brightness = 1)

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
defaultcolor = [216, 231, 0]
defcolor = [orange, yellow, orangeT]
randcolor = random.choice(defcolor)
defcolor2 = [lightBlue, lightBlue, white]
randcolor2 = random.choice(defcolor2)

color1 = [defaultcolor[0],defaultcolor[1],defaultcolor[2]]
np.fill(color1)
'''
Function: fade_out

Description: This function begins with a color and fades to black

Parameters: defcolor(list), delay(float)

Return value: Prints the color values as they update
'''
def fade_out(defaultcolor, delay = 0.005):
    fadeR = defaultcolor[0]/256.0
    fadeG = defaultcolor[1]/256.0
    fadeB = defaultcolor[2]/256.0
    for i in range(256):
        color1[0] = int (defaultcolor[0] - (fadeR*i))
        color1[1] = int (defaultcolor[1] - (fadeG*i))
        color1[2] = int (defaultcolor[2] - (fadeB*i))
        np.fill(color1)
        print(i, defaultcolor,fadeR*i,fadeG*i,fadeB*i)
        time.sleep(delay)
        np.show()

'''
Function: fade_in

Description: This function begins with a black and fades in to a color

Parameters: defcolor(list), delay(float)

Return value: Prints the color values as they update
'''
def fade_in(defaultcolor, delay = 0.005):
    fadeR = defaultcolor[0]/256.0
    fadeG = defaultcolor[1]/256.0
    fadeB = defaultcolor[2]/256.0
    for i in range(256):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        print(i, defaultcolor,fadeR*i,fadeG*i,fadeB*i)
        time.sleep(delay)
        np.show()
        
'''
Function: sparkle

Description: This function causes a foreground color to pop up in random pixel intervals on top of the background color.

Parameters: fgcolor(list), bgcolor(list), delay(float), num_sparks(int)

Return value: nothing
'''
def sparkle(fgcolor = white, bgcolor = black, delay = 0.005, num_sparks = 10):
    for i in range(50):
        np.fill(bgcolor)
        np.show()
        for j in range(num_sparks):
            rand_int = random.randrange(0, 10)
            np[rand_int] = fgcolor
            np.show()
        time.sleep(delay)
        np[rand_int] = bgcolor
        np.show()
        
'''
Function: chase

Description: This function causes a foreground color to follow after the background in sets of two

Parameters: fgcolor(list), bgcolor(list), speed(float)

Return value: Prints the background and foreground color values as they update
'''
def chase(fgcolor = green, bgcolor = purple, speed = 0.005):
    for j in range(100):
        np.show()
        for i in range(10):
            if i % 3 != 0:
                led = (i+j) % 10 
                np[led] = fgcolor
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 10
                np[led] = bgcolor
                print("fColor",i,np[i])
            time.sleep(speed)

'''
Function: Lightning

Description: This function creates a random amount of lightning flashes over random periods of time

Parameters: bgcolor(list), flash(list), and numpix(int)

Return value: prints the amount of time the function will sleep before the next flash
'''
def lightning(bgcolor = darkpurple, flash = randcolor2, numpix = np.n):
        for h in range(5):
            randomsleep = random.random()*10
            randompix = random.randrange(3,8)
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

'''
Function: Fire

Description: This function creates a fire effect in which random flashes of red appear on an orange background

Parameters: fgcolor(list), bgcolor(list), numsparks(int)

Return value: nothing
'''
def fire(fgcolor = white, bgcolor = black, num_sparks = 15):
    for i in range(50):
        np.fill(bgcolor)
        np.show()
        for j in range(num_sparks):
            randcolor = random.choice(defcolor)
            rand_int = random.randrange(0, 10)
            rand_intT = random.randrange(0, 10)
            randomsleep = random.random()/100
            np[rand_int] = fgcolor
            np[rand_intT] = black
            np.show()
            time.sleep(randomsleep)
        np[rand_int] = bgcolor
        np.show()

while True:
    fade_out(purple)
    fade_in(green)
    fade_out(green)
    fade_in(purple)
    fade_out(purple)
    fade_in(green)
    sparkle(purple, green, 0.05, 5)
    fade_out(green)
    fade_in(purple)
    fade_out(purple)
    fade_in(green)
    chase()
    fade_out(green)
    fade_in(orange)
    chase(orange, purple)
    fade_out(purple)
    fade_in(purple)
    fire(randcolor, red)
    lightning()
