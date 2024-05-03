import subprocess
from datetime import datetime
from pirate_display import initPirateDisplay
from iotutils import getCurrentTimeStamp
from PIL import Image, ImageDraw, ImageFont
import gpsserial as gps
from compass import bearingPitch
from pprint import pprint
from hoshimiru import getConstellationData, findConstellations

display = initPirateDisplay()
display.begin()
blackBackground = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
display.display(blackBackground)

# font = ImageFont.load_default()
font = ImageFont.truetype("JetBrainsMono-Regular.ttf", 36)
fontBig = ImageFont.truetype("JetBrainsMono-Regular.ttf", 56)

daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
dt = datetime.now()
day = daysOfWeek[dt.weekday()]

serialPort = "/dev/serial0"
gpsSerialPort = gps.init(serialPort)

def clearDisplay():
    img = Image.new('RGB', (display.width, display.height), color=(0, 0, 0))
    display.display(img)

def pasteImage(img, text, width, height, x, y, font, color):
    textImage = Image.new("RGB", (width, height), (0, 0, 0))
    textDraw = ImageDraw.Draw(textImage)
    textDraw.text((0, 0), text, align="center", font=font, fill=color)
    rotatedTextImage = textImage.rotate(270, expand=True)
    img.paste(rotatedTextImage, (x, y))

def displayQrCodeConstellation(qrcode):
    # Black background image
    img = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    date = getCurrentTimeStamp()
    dateList = date.split("-")
    mdy = dateList[1] + "/" + dateList[2] + "/" + dateList[0]
    if int(dateList[3]) > 12:
        h = int(dateList[3]) - 12
        hm = str(h) + ":" + dateList[4] + "PM"
    else:
        h = int(dateList[3])
        hm = str(h) + ":" + dateList[4] + "AM"
    
    width, height = draw.textsize(mdy, font=font)
    pasteImage(img, mdy, width, height,
               display.width-height, int(display.height/2 - width/2),
               font, (255, 255, 255))

    width, height = draw.textsize(day, font=font)
    pasteImage(img, day, width, height,
               display.width-(height *2), int(display.height/2 - width/2),
               font, (255, 255, 255))
    
    width, height = draw.textsize(hm, font=font)
    pasteImage(img, hm, width, height,
               display.width-(height *3), int(display.height/2 - width/2),
               font, (255, 255, 255))

    width, height = draw.textsize(qrcode, font=fontBig)
    pasteImage(img, qrcode, width, height,
               int(display.width-(height * 3.5)), int(display.height/2 - width/2),
               fontBig, (255, 165, 0))
    display.display(img)
    
def displayLatLonBearingPitch():
    gpsData = gps.getData(gpsSerialPort)
    lat = round(gps.getDecimalLatitude(gpsData), 1)
    lon = round(gps.getDecimalLongitude(gpsData), 1)
    print(lat, lon)
    
    bearing, pitch = bearingPitch()

    img = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    latStr = f"Lat: {lat:6}"
    width, height = draw.textsize(latStr, font=font)
    pasteImage(img, latStr, width, height,
               display.width-height, 0,
               font, (255, 255, 255))
    
    lonStr = f"Lon: {lon:6}"
    width, height = draw.textsize(lonStr, font=font)
    pasteImage(img, lonStr, width, height,
               display.width-(height *2), 0,
               font, (255, 255, 255))

    dirStr = f"Dir: {round(bearing, 1):6}"
    width, height = draw.textsize(dirStr, font=font)
    pasteImage(img, dirStr, width, height,
               display.width-(height *3), 0,
               font, (255, 255, 255))

    pitchStr = f"Pitch: {round(pitch, 1):4}"
    width, height = draw.textsize(pitchStr, font=font)
    pasteImage(img, pitchStr, width, height,
               display.width-(height *4), 0,
               font, (255, 255, 255))
    
    apiToken="ef1d7180-2180-439f-a3d0-a837cd7ab37d"

    dateTime = getCurrentTimeStamp().split("-")

    constellationsList = getConstellationData(lat, lon,
                                              dateTime[0] + "-" + dateTime[1] + "-" + dateTime[2],
                                              dateTime[3], dateTime[4],
                                              apiToken)
    print(len(constellationsList), "constellations viewable")
    #pprint(constellationsList)

    foundConstellations = findConstellations(constellationsList, bearingDecimal=bearing, pitchDecimal=pitch)
    print(len(foundConstellations), "constellations viewable at bearing=", bearing, "pitch=", pitch)
    pprint(foundConstellations)

    if len(foundConstellations) >= 1:
        constellationName = foundConstellations[0]["enName"]
    else:
        constellationName = "None"

    width, height = draw.textsize(constellationName, font=font)
    pasteImage(img, constellationName, width, height,
               int(display.width-(height * 5)), 0,
               font, (255, 165, 0))

    display.display(img)

def demo():
    gpsData = gps.getData(gpsSerialPort)
    lat = round(gps.getDecimalLatitude(gpsData), 1)
    lon = round(gps.getDecimalLongitude(gpsData), 1)
    print(lat, lon)
    
    bearing, pitch = bearingPitch()

    img = Image.new("RGB", (display.width, display.height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    latStr = f"Lat: {lat:6}"
    width, height = draw.textsize(latStr, font=font)
    pasteImage(img, latStr, width, height,
               display.width-height, 0,
               font, (255, 255, 255))
    
    lonStr = f"Lon: {lon:6}"
    width, height = draw.textsize(lonStr, font=font)
    pasteImage(img, lonStr, width, height,
               display.width-(height *2), 0,
               font, (255, 255, 255))

    dirStr = f"Dir: {round(bearing, 1):6}"
    width, height = draw.textsize(dirStr, font=font)
    pasteImage(img, dirStr, width, height,
               display.width-(height *3), 0,
               font, (255, 255, 255))

    pitchStr = f"Pitch: {round(pitch, 1):4}"
    width, height = draw.textsize(pitchStr, font=font)
    pasteImage(img, pitchStr, width, height,
               display.width-(height *4), 0,
               font, (255, 255, 255))

    constellationName = "Ursa major"
    width, height = draw.textsize(constellationName, font=font)
    pasteImage(img, constellationName, width, height,
               int(display.width-(height * 4.5)), 0,
               font, (255, 165, 0))

    constellationName = "Big dipper"
    width, height = draw.textsize(constellationName, font=font)
    pasteImage(img, constellationName, width, height,
               int(display.width-(height * 5.5)), 0,
               font, (255, 165, 0))
    display.display(img)
    
    command = "vlc -I dummy bigdipper.aac --play-and-exit"
    subprocess.run(command, shell=True)
    
    
if __name__ == "__main__":
#     displayQrCodeConstellation("Orion")
    displayLatLonBearingPitch()

