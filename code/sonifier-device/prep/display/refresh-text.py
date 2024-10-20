import sys, time
from pirate_display import initPirateDisplay
from iotutils import getCurrentTimeStamp
from PIL import Image, ImageDraw, ImageFont

display = initPirateDisplay()
display.begin()

# font = ImageFont.load_default()
font = ImageFont.truetype("JetBrainsMono-Regular.ttf", 32)

# Black background image
img = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

counter = 0

while True:
    try:
        print(counter)
        text = str(counter)
        width, height = draw.textsize(text, font=font)
        textImage = Image.new("RGB", (width, height), (0, 0, 0))
        textDraw = ImageDraw.Draw(textImage)
        textDraw.text((0, 0), text, font=font, fill=(255, 255, 255))
        img.paste(textImage, (0, 0))
        display.display(img)
        time.sleep(1)
        img = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
        display.display(img)
        counter += 1
    except KeyboardInterrupt:
        break

img = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
display.display(img)
