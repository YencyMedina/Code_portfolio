import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.D2)
led.direction = dio.Direction.OUTPUT

led2 = dio.DigitalInOut(board.D3)
led2.direction = dio.Direction.OUTPUT


led3 = dio.DigitalInOut(board.D4)
led3.direction = dio.Direction.OUTPUT

led4 = dio.DigitalInOut(board.D5)
led4.direction = dio.Direction.OUTPUT

button = dio.DigitalInOut(board.D6)
button.direction = dio.Direction.INPUT

button2 = dio.DigitalInOut(board.D7)
button2.direction = dio.Direction.INPUT

button3 = dio.DigitalInOut(board.D8)
button3.direction = dio.Direction.INPUT

button4 = dio.DigitalInOut(board.D9)
button4.direction = dio.Direction.INPUT


MAX_ON = 100
CHANGE = 20
on = 0
off = 100

#Turns the LEDs off by setting on to 0
def off_btn():
    global on, off
    on = 0

#Turns LEDs on by setting on to 100
def on_btn():
    global on, off
    on = MAX_ON
    print(on)

#Dims the LEDs by taking on down by 20
def dim():
    global on, off
    if on > 0:
        if on <= 100:
            on -= CHANGE
            off = on
    print(off)

#brightens the LEDs by adding 20 to on
def brighten():
    global on, off
    if on < 100:
        on += CHANGE
        print(on)

while True:
    if on > 0:
        led.value = True
        led2.value = True
        led3.value = True
        led4.value = True
        time.sleep(on/10000.0)
    if off > 0:
        led.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        time.sleep(off/10000.0)
    
    if not button.value:
        print("off button pressed")
        off_btn()
        time.sleep(0.5)
    
    elif not button2.value:
        print("on button pressed")
        on_btn()
        time.sleep(0.5)
    
    
    elif not button3.value and off > 0:
        print("brighten button pressed")
        brighten()
        time.sleep(0.5)
    
    elif not button4.value off < 100:
        print("dim button pressed")
        dim()
        time.sleep(0.5)