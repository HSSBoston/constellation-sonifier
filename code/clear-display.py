import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7789

display_type = "square"

disp = ST7789.ST7789(
    height=135 if display_type == "rect" else 240,
    rotation=0 if display_type == "rect" else 90,
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=13,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=0 if display_type == "square" else 40,
    offset_top=53 if display_type == "rect" else 0
)

disp.begin()
WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
disp.display(img)
