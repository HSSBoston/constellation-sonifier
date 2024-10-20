import time, math
from lis3mdl import LIS3MDL

sensor = LIS3MDL()
magX, magY, magZ = sensor.readG()
minX = maxX = magX
minY = maxY = magY
minZ = maxZ = magZ

while True:
    try:
        magX, magY, magZ = sensor.readG()
        
        minX = min(minX, magX)
        minY = min(minY, magY)
        minZ = min(minZ, magZ)
        
        maxX = max(maxX, magX)
        maxY = max(maxY, magY)
        maxZ = max(maxZ, magZ)
        
        offsetX = (maxX + minX) / 2
        offsetY = (maxY + minY) / 2
        offsetZ = (maxZ + minZ) / 2
        
        fieldX = (maxX - minX) / 2
        fieldY = (maxY - minY) / 2
        fieldZ = (maxZ - minZ) / 2

        print("Gauss:", magX, magY, magZ)
        print("Magnetic field strength (nT): ", sensor.magneticFieldStrengthT())
        print("Field:        X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(
            fieldX, fieldY, fieldZ))
        print("Hard Offset:  X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(
            offsetX, offsetY, offsetZ))
        print("")

    #     print( sensor.getBearing( sensor.declinationDegMinToDecimalDeg(-14, -6),
    #                               magX, magY, axis="x"))
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
print("----------")
print("Your hard iron offset:", offsetX, ",", offsetY, ",", offsetZ)