# Library for a display in Pimoroni Pirate Audio with a square display,
# a speaker and 4 buttons. The display is 1.3" IPS colour LCD (240x240px) that
# requires ST7789 driver. 

import ST7789

display_type = "square"

def initPirateDisplay():
    disp = ST7789.ST7789(
        height=135 if display_type == "rect" else 240,
        rotation=0 if display_type == "rect" else 90,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    #         cs=ST7789.BG_SPI_CS_BACK,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=13,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000,
        offset_left=0 if display_type == "square" else 40,
        offset_top=53 if display_type == "rect" else 0
    )
    return disp


# Alternatively load a TTF font.
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 16)
