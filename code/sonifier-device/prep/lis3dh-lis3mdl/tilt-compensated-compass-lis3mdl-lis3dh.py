import time, math
from lis3mdl import LIS3MDL
from lis3dh import LIS3DH

offset = [-0.8004238526746565 , 0.1680064308681672 , 1.54983922829582]
#         -0.10494007600116925 , -0.027769657994738378 , 0.04311604793919904]
mag = LIS3MDL(offset=offset)
accel = LIS3DH()

while True:
    try:
        magX, magY, magZ = mag.readG()
        print("Gauss:", magX, magY, magZ)
        print("Magnetic field strength (nT): ", mag.magneticFieldStrengthT())
        print("2D Bearing: ", mag.bearing(magX, -magY))
        
        gX, gY, gZ = accel.readG()
        pitch, roll = accel.pitchRoll(-gX, gY, gZ)
        print("Pitch:", math.degrees(pitch), "Roll:", math.degrees(roll))
        print("3D Bearing: ", mag.tiltCompensentedBearing(magX, -magY, -magZ,
                                                             pitch, roll))
        print("")
        time.sleep(1)
    except KeyboardInterrupt:
        break
