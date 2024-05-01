import time, math
from lis3mdl import LIS3MDL

# offset = [-0.17, 0.12, 0.29]

mag = LIS3MDL()

while True:
    try:
        magX, magY, magZ = mag.readG()
        print("Gauss:", magX, magY, magZ)
        print("Magnetic field strength (nT): ", mag.magneticFieldStrengthT())
        print("")
        time.sleep(1)
    except KeyboardInterrupt:
        break
