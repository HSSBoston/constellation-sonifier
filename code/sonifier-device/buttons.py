from gpiozero import Button
import time, subprocess
from tiny_code_reader import readQR
import display

buttonA = Button(5)
buttonB = Button(6)
buttonX = Button(16)
buttonY = Button(24)


while True:
    try:
        if buttonA.is_pressed:
            print("Button A pressed")
            display.displayLatLonBearingPitch()
            display.clearDisplay()
            
        if buttonB.is_pressed:
            print("Button B pressed")
            display.demo()
            display.clearDisplay()
            
        if buttonX.is_pressed:
            print("Button X pressed")
        if buttonY.is_pressed:
            print("Button Y pressed")
            qrCode = readQR()
            print("QR code scanned:", qrCode)
            display.displayQrCodeConstellation(qrCode)
            if qrCode == "Orion":
                command = "vlc -I dummy orion.aac --play-and-exit"
                subprocess.run(command, shell=True)
            display.clearDisplay()

        time.sleep(0.2)
    except KeyboardInterrupt:
        break
    