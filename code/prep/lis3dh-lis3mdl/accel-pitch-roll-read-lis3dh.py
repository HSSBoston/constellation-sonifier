import time, math
from lis3dh import LIS3DH

accel = LIS3DH()

while True:
    try:
        x, y, z = accel.readG()
        print("g:", x, y, z)
        pitch, roll = accel.pitchRoll(-x, y, z)
        print("Pitch:", math.degrees(pitch), "Roll:", math.degrees(roll))
        print("")
        time.sleep(1)
    except KeyboardInterrupt:
        break