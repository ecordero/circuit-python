# program for joe's blinken lights using:
# * circuit playground express
# * neopixel ring (16)
# * sticks (8 x 4 sticks) [future work]
import board, neopixel, random, digitalio, time, touchio
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.025

# ring
numpix = 16  # Number of NeoPixels
pixpin = board.A1  # Pin where NeoPixels are connected
strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.005)

# cpx
# basePixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01, auto_write=False)


TEAL = (75, 250, 100) # RGB color - teal
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

ALL_COLORS = [TEAL, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]
QUAD1 = [0,1,2,3]
QUAD2 = [4,5,6,7]
QUAD3 = [8,9,10,11]
QUAD4 = [12,13,14,15]

count = 0

# def color_dot_chase(color):
#     for i in range(10):
#         basePixels[i] = color
#         basePixels.show()
#         basePixels[i] = OFF
#         time.sleep(0.05)
#         basePixels.show()


def animate():
  for i in range(numpix):
    # Set 'head' pixel to color:
    colorIndex = random.randrange(0, len(ALL_COLORS) - 1)
    # strip[i] = ALL_COLORS[colorIndex]
    setPixelColor(i, ALL_COLORS[colorIndex])
    strip.write()  # Refresh LED states
    time.sleep(0.125)  # 16 millisecond delay
    strip[i] = OFF
    # strip[sine[(i + len(sine) - 8) % len(sine)]] = [0, 0, 0]
    strip.write()  # Refresh LED states
    time.sleep(0.125)  # 16 millisecond delay
    count = i

def setPixelColor(pixelIndex, colorValue):
  strip[pixelIndex] = colorValue
  # strip.write()
  # time.sleep(0.025)

def setQuadColor(pixelIndexes, quadColor):
  for i in pixelIndexes:
    setPixelColor(i, quadColor)

setQuadColor(QUAD1, OFF)
setQuadColor(QUAD2, OFF)
setQuadColor(QUAD3, OFF)
setQuadColor(QUAD4, OFF)

while True:  # Loop forever...
# while count < len(ALL_COLORS):  # Loop forever...

  # if cpx.switch:
  #     cpx.pixels.fill(GREEN)

  if cpx.button_a:  # button is pushed
      setQuadColor(QUAD1, OFF)
      setQuadColor(QUAD2, OFF)
      setQuadColor(QUAD3, OFF)
      setQuadColor(QUAD4, OFF)

  if cpx.button_a:  # button is pushed
      animate()

  if cpx.touch_A2:
    cpx.pixels.fill(RED)
    setQuadColor(QUAD1, GREEN)
    time.sleep(1)
    cpx.pixels.fill(OFF)
  # else:
    # setQuadColor(QUAD1, OFF)

  if cpx.touch_A3:
    cpx.pixels.fill(BLUE)
    setQuadColor(QUAD2, GREEN)
    time.sleep(1)
    cpx.pixels.fill(OFF)
  # else:
    # setQuadColor(QUAD2, OFF)

  if cpx.touch_A4:
    cpx.pixels.fill(CYAN)
    setQuadColor(QUAD3, GREEN)
    time.sleep(1)
    cpx.pixels.fill(OFF)
  # else:
    # setQuadColor(QUAD3, OFF)

  if cpx.touch_A5:
    cpx.pixels.fill(PURPLE)
    setQuadColor(QUAD4, GREEN)
    time.sleep(1)
    cpx.pixels.fill(OFF)
  # else:
    # setQuadColor(QUAD4, OFF)

  # animate()



