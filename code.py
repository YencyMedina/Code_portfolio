import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT
led.value = True

def lightUp():
    for i in range(100):
        on = i
        off = 100 - on
        for j in range(1):
            led.value = True
            time.sleep(on / 10000.0)
            led.value = False
            time.sleep(off / 10000.0)
        print(on)

def dim():
    for i in range(100):
        on = 100-i-1
        off = 100 - on
        for j in range(1):
            led.value = True
            time.sleep(on / 10000.0)
            led.value = False
            time.sleep(off / 10000.0)
        print(on)

on = 0
off = 100 - on
while True:
    lightUp()
    dim()