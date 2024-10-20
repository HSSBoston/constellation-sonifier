from gpiozero import Button
import time

buttonA = Button(5)
buttonB = Button(6)
buttonX = Button(16)
buttonY = Button(24)


while True:
    try:
        if buttonA.is_pressed:
            print("A")
        if buttonB.is_pressed:
            print("B")
        if buttonX.is_pressed:
            print("X")
        if buttonY.is_pressed:
            print("Y")
        time.sleep(0.2)
    except KeyboardInterrupt:
        break
    