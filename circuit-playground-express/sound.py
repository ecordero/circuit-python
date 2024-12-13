import time
from adafruit_circuitplayground.express import cpx

def zap(color, wait):
    for i in range(10):
        cpx.pixels[i] = color
        cpx.pixels.show()
        time.sleep(wait)
        cpx.pixels[i] = OFF
        cpx.pixels.show()

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
CHASEDELAY = 0.1
ZAPPDELAY = 0.025

while True:
    if cpx.button_a:
        zap(RED, ZAPPDELAY)
        cpx.play_tone(220, 0.5)
    elif cpx.button_b:
        zap(BLUE, ZAPPDELAY)
        cpx.play_tone(440, 0.5)
    else
        cpx.stop_tone()

