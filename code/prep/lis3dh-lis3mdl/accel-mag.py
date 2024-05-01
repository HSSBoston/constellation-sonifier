from lis3dh import LIS3DH
from lis3mdl import LIS3MDL

accel = LIS3DH()
# print("G:", sensor.readG() )
# print("m/s^2:", sensor.read() )
accelX, accelY, accelY = accel.readG()
pitch, roll = accel.pitchRoll(accelX, accelY, accelY)
print(pitch, roll)

mag = LIS3MDL()
magX, magY, magZ = mag.readG()
print(magX, magY, magZ)
print(mag.getBearing(mag.declinationDegMinToDecimalDeg(-14, -6),
                     magX, magY, axis="X"))

print(mag.getCompensatedBearing(mag.declinationDegMinToDecimalDeg(-14, -6),
                                magX, magY, magZ,
                                pitch, roll, axis="X"))
