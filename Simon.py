import time
import board
import digitalio as dio
import random

colors = (1, 2, 3, 4)
randcolor = [random.choice(colors)]
started = False
points = 0

button = dio.DigitalInOut(board.D2)
button.direction = dio.Direction.INPUT

led = dio.DigitalInOut(board.D3)
led.direction = dio.Direction.OUTPUT

button2 = dio.DigitalInOut(board.D4)
button2.direction = dio.Direction.INPUT

led2 = dio.DigitalInOut(board.D5)
led2.direction = dio.Direction.OUTPUT

button3 = dio.DigitalInOut(board.D6)
button3.direction = dio.Direction.INPUT

led3 = dio.DigitalInOut(board.D7)
led3.direction = dio.Direction.OUTPUT

button4 = dio.DigitalInOut(board.D8)
button4.direction = dio.Direction.INPUT

led4 = dio.DigitalInOut(board.D9)
led4.direction = dio.Direction.OUTPUT

start = dio.DigitalInOut(board.D10)
start.direction = dio.Direction.INPUT

#displays the amount of points the user has, all lights is 10 while only green is 1
def point_system():
    for i in range(int(points/10)):
        led.value = True
        led2.value = True
        led3.value = True
        led4.value = True
        time.sleep(0.2)
        led.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        time.sleep(0.2)
    for i in range(points % 10):
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)
# displays the sequence the user has to repeat in order to progress
def sequence():
    for colors in randcolor:
        if colors == 1:
            led.value = True
            time.sleep(0.5)
            led.value = False
            print("Green")
        if colors == 2:
            led2.value = True
            time.sleep(0.5)
            led2.value = False
            print("Red")
        if colors == 3:
            led3.value = True
            time.sleep(0.5)
            led3.value = False
            print("Yellow")
        if colors == 4:
            led4.value = True
            time.sleep(0.5)
            led4.value = False
            print("White")
        time.sleep(0.15)
# adds on to the sequence every time it is called            
def addsequence():
    randcolor.append(random.choice(colors))
    print("-----")
# checks for user input by going through the list and comparing it to the button check
def user_input():
    for color in randcolor:
        check = 0
        while check == 0:
            if button.value == True:
                led.value = True
                time.sleep(0.3)
                led.value = False
                check = 1
            if button2.value == True:
                led2.value = True
                time.sleep(0.3)
                led2.value = False
                check = 2
            if button3.value == True:
                led3.value = True
                time.sleep(0.3)
                led3.value = False
                check = 3
            if button4.value == True:
                led4.value = True
                time.sleep(0.3)
                led4.value = False
                check = 4
        if check != color:
            print("-----" + "\n" + "False")
            return False
    print("-----" + "\n" + "correct")
    return True
# When the start button is pressed started is set to true meaning the sequence can be displayed, once the sequence is done then the user check begins, if the check returns false the loop will exit and reset but display the amount of points first, if its true it will add a point and add on to the sequence.
while True:
    randcolor = [random.choice(colors)]
    if start.value:
        started = True
        print(started)
        print("-----")
        while started:
            sequence()
            print("seq")
            if user_input():
                points += 1
                print("-----" + "\n" + "adding")
                addsequence()
            else:
                started = False
                point_system()
            time.sleep(0.2)
