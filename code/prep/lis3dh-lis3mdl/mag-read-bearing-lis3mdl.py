import time, math
from lis3mdl import LIS3MDL

offset = [-0.10494007600116925 , -0.027769657994738378 , 0.04311604793919904]
mag = LIS3MDL(offset=offset)

while True:
    try:
        magX, magY, magZ = mag.readG()
        print("Gauss:", magX, magY, magZ)
        print("Magnetic field strength (nT): ", mag.magneticFieldStrengthT())
        print("Bearing: ", mag.bearing(magX, -magY))
        print("")
        time.sleep(1)
    except KeyboardInterrupt:
        break
