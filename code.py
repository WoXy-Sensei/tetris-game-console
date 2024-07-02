import board
import busio
import displayio
import time
from adafruit_st7735r import ST7735R
from keyInput import KeyInput
from tetrisApp import Tetris
from galleryApp import Gallery
from bitmap import Bitmap

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16	

displayio.release_displays()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr = True,rotation=180)

bitmap = Bitmap()

root = displayio.Group()
root.append(bitmap.get_bitmap("images/main.bmp"))
display.show(root)

keyInput = KeyInput()

runApp = None

while True:
    if keyInput.isPressedKey("A"):
        runApp = Tetris()
    if keyInput.isPressedKey("B"):
        runApp = Gallery()
    
    if runApp != None:
        root.pop()
        root.append(runApp.screen)
        runApp.start()
        if runApp.closed:
            root.remove(runApp.screen)
            root.append(bitmap.get_bitmap("images/main.bmp"))
            runApp = None
    
    time.sleep(0.1)
    