# Driver for the LSM303 accelerometer
# April 24, 2024 v0.01
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/

import smbus, sys, time, math
from typing import ClassVar, Tuple, Final

# Default I2C address
_ADDRESS: Final[int] = 0x19
# Default sensitivity level: ±2g (Choices: ±2g, ±4g, ±8g and ±16g)
_SCALE: Final[int] = 2
# Default data rate: 200Hz (Choices: 1, 10, 25, 50, 100, 200 and 400 Hz)
_DATA_RATE: Final[int] = 200

# Register addresses
_REG_WHO_AM_I: Final[int] = 0x0F
_CTRL_REG1: Final[int] = 0x20
_CTRL_REG2: Final[int] = 0x21
_CTRL_REG3: Final[int] = 0x22
_CTRL_REG4: Final[int] = 0x23
_CTRL_REG5: Final[int] = 0x24

_OUT_X_L: Final[int] = 0x28
_OUT_X_H: Final[int] = 0x29
_OUT_Y_L: Final[int] = 0x2A
_OUT_Y_H: Final[int] = 0x2B
_OUT_Z_L: Final[int] = 0x2C
_OUT_Z_H: Final[int] = 0x2D

# Defaults to the high resolution mode (12-bit data output)
#
class LSM303:
    # address (hex): I2C address in hex
    # scale: Accelerometer's sensing range: 2, 4, 8 or 16 (±2g, ±4g, ±8g or ±16g)
    # dataRate: Sensing frequency: 1, 10, 25, 50, 100, 200 or 400 Hz
    #
    def __init__(self, *, address: int =_ADDRESS, scale: int =_SCALE, dataRate: int =_DATA_RATE) -> None:
        assert scale in [2, 4, 8, 16], "Wrong LSM303 sensing scale: " +\
               str(scale) + "." + " It must be 2, 4, 8 or 16."
        assert dataRate in [1, 10, 25, 50, 100, 200, 400], "Wrong LSM303 sensing frequency "+\
               "(data rate): " + str(dataRate) + "." + " It must be 1, 10, 25, 50, 100, 200 or 400."

        self._scale: int = scale
        self._dataRate: int = dataRate
        self._addr: int = address
        self._i2c: smbus.SMBus = smbus.SMBus(1)
        
        reg1Data: int
        if self._dataRate == 1:
            reg1Data = 0x17
        elif self._dataRate == 10:
            reg1Data = 0x27
        elif self._dataRate == 25:
            reg1Data = 0x37
        elif self._dataRate == 50:
            reg1Data = 0x47
        elif self._dataRate == 100:
            reg1Data = 0x57
        elif self._dataRate == 200:
            reg1Data = 0x67
        elif self._dataRate == 400:
            reg1Data = 0x77

        reg4Data: int
        if self._scale == 2:
            reg4Data = 0x08
        elif self._scale == 4:
            reg4Data = 0x18
        elif self._scale == 8:
            reg4Data = 0x28
        elif self._scale == 16:
            reg4Data = 0x38

        try:
            # Ping the sensor
            sensorId = self._i2c.read_byte_data(self._addr, _REG_WHO_AM_I)
            if sensorId != 0x33:
                raise RuntimeError("Failed to find LSM303.")
            # Clear/reset the sensor's memory
            self._i2c.write_byte_data(self._addr, _CTRL_REG5, 0x80)
            # Set high-resolution mode, data rate (sensing freq) and sensing scale
            self._i2c.write_byte_data(self._addr, _CTRL_REG1, reg1Data)
            self._i2c.write_byte_data(self._addr, _CTRL_REG4, reg4Data)
            print("LSM303 configured with " + "addr=" + hex(self._addr) +\
                  ", sensing scale=±" + str(self._scale) + "g" +\
                  ", data rate=" + str(self._dataRate) + "Hz.")
        except OSError:
            print("Wrong I2C address: " + hex(self._addr))
            raise

    # Returns an I2C address in hex (string).
    @property
    def addr(self) -> str:
        return hex(self._addr)

    @property
    def scale(self) -> int:
        return self._scale
    
    @property
    def rate(self) -> int:
        return self._dataRate

    @property
    def i2c(self) -> smbus.SMBus:
        return self._i2c

    # Read X, Y, and Z acceleration values in G and return them as a tuple.
    # When one of the axes points straight to Earth, its G value is 1 or -1. 
    #
    def readG(self) -> Tuple[float, float, float]:
        # xh: Most significant part of acceleration data
        # xl: Least significant part of acceleration data
        # Concat xh and xl to get the complete accel data.
        xl = self._i2c.read_byte_data(self._addr, _OUT_X_L)
        xh = self._i2c.read_byte_data(self._addr, _OUT_X_H)
        yl = self._i2c.read_byte_data(self._addr, _OUT_Y_L)
        yh = self._i2c.read_byte_data(self._addr, _OUT_Y_H)
        zl = self._i2c.read_byte_data(self._addr, _OUT_Z_L)
        zh = self._i2c.read_byte_data(self._addr, _OUT_Z_H)
        
        # Concat xh (8-bits) and xl (8 bits) to derive the complete 16-bit data. 
        # Its left-justified 12 bits encode an accel value in the default high-res
        # data mode.
        x = (xh << 8 | xl) >> 4
        y = (yh << 8 | yl) >> 4
        z = (zh << 8 | zl) >> 4
        
        # Each accel value is expressed as two's complement. Convert it
        # to a signed value [-2048, 2047]. Note: 2^12 = 4096
        if x >= 2048:
            x -= 4096
        if y >= 2048:
            y -= 4096
        if z >= 2048:
            z -= 4096
        
        # Convert accel values to G values based on the sensitivity level.
        divider = 4096/(2 * self._scale)
        return (x/divider, y/divider, z/divider)

    # Read X, Y, and Z acceleration values in m/s^2 and return them as a tuple.
    # When one of the axes points straight to Earth, its G value is 9.806 or -9.806. 
    #
    def read(self) -> Tuple[float, float, float]:
        x, y, z = self.readG()
        return (x * 9.806, y * 9.806, z * 9.806)
    
    def pitchRoll(self, x, y, z):
        accelStrength = math.sqrt(x**2 + y**2 + z**2)
        xNormalized = x/accelStrength
        yNormalized = y/accelStrength
#         zNormalized = z/accelStrength
        pitch = math.asin(-xNormalized)
        roll = math.asin(yNormalized/math.cos(pitch))

#         roll = math.atan2(yNormalized, zNormalized)
#         pitch = math.atan( -xNormalized/(yNormalized * math.sin(roll) * math.cos(roll)) )
        
#         roll = math.atan2(y, z)
#         pitch = math.atan( -x/(y * math.sin(roll) + z * math.cos(roll)) )
        
        return (pitch, roll)
        
if __name__ == "__main__":
    sensor = LSM303()
    print("G:", sensor.readG() )
    print("m/s^2:", sensor.read() )
#     x, y, z = sensor.readG()
#     pitch, roll = sensor.pitchRoll(x, y, z)
#     print(math.degrees(pitch), math.degrees(roll))

#     sensor = LIS3DH(sensitivity=4)
#     print( sensor.readG() )
#     print( sensor.read() )
