import time, math
from lis2mdl import LIS2MDL
from lsm303 import LSM303

offset = [-0.17, 0.12, 0.29]

accel = LSM303()
sensor = LIS2MDL(offset=offset)
# sensor = LIS2MDL()

while True:
    try:
        magX, magY, magZ = sensor.readG()
        print("Gauss:", magX, magY, magZ)
        print("Bearing: ", sensor.bearing(magX, magY))
        
        gX, gY, gZ = accel.readG()
        pitch, roll = accel.pitchRoll(-gX, -gY, gZ)
        print(math.degrees(pitch), math.degrees(roll))
        print("Bearing: ", sensor.tiltCompensentedBearing(magX, magY, -magZ,
                                                          pitch, roll))
        
#         print("Bearing: ", sensor.bearingWithDeclination(magX, magY,
#                                                          sensor.declinationDegMinToDecimalDeg(-14, -6)))
        
#         print("nT:", sensor.readT() )
#         print("Magnetic field strength (Gauss): ", sensor.magneticFieldStrengthG())
#         print("Magnetic field strength (nT): ", sensor.magneticFieldStrengthT())
    #     print( sensor.getBearing( sensor.declinationDegMinToDecimalDeg(-14, -6),
    #                               magX, magY, axis="x"))
        print("")
        time.sleep(1)
    except KeyboardInterrupt:
        break
