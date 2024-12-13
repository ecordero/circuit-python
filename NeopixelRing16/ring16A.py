# program for joe's blinken lights using:
# * circuit playground express
# * neopixel ring (16)
# * sticks (8 x 4 sticks) [future work]
import board, neopixel, random, digitalio, time, touchio
led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
slider = digitalio.DigitalInOut(board.SLIDE_SWITCH)
slider.direction = digitalio.Direction.INPUT
slider.pull = digitalio.Pull.UP
touchPad2 = board.A2
touchPad3 = board.A3
touchPad4 = board.A4
touchPad5 = board.A5


buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.switch_to_input(pull=digitalio.Pull.DOWN)
buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)
touch2 = touchio.TouchIn(touchPad2)
touch3 = touchio.TouchIn(touchPad3)
touch4 = touchio.TouchIn(touchPad4)
touch5 = touchio.TouchIn(touchPad5)

# ring
numpix = 16  # Number of NeoPixels
pixpin = board.A1  # Pin where NeoPixels are connected
strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.005)

# cpx
basePixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01, auto_write=False)


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

def color_dot_chase(color):
    for i in range(10):
        basePixels[i] = color
        basePixels.show()
        basePixels[i] = OFF
        time.sleep(0.05)
        basePixels.show()


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

while True:  # Loop forever...
# while count < len(ALL_COLORS):  # Loop forever...

	# if slider.value:
	# 		for i in range(10)
	# 				color_dot_chase(RED)

  if buttonA.value:  # button is pushed
      setQuadColor(QUAD1, WHITE)
  else:
      setQuadColor(QUAD1, OFF)

  if buttonB.value:
      setQuadColor(QUAD3, CYAN)
  else:
      setQuadColor(QUAD3, OFF)

  if touch2.value:
      color_dot_chase(RED)
      setQuadColor(QUAD1, GREEN)
  else:
      setQuadColor(QUAD1, OFF)

  if touch3.value:
      color_dot_chase(BLUE)
      setQuadColor(QUAD2, GREEN)
  else:
      setQuadColor(QUAD2, OFF)

  if touch4.value:
      color_dot_chase(CYAN)
      setQuadColor(QUAD3, GREEN)
  else:
      setQuadColor(QUAD3, OFF)

  if touch5.value:
      color_dot_chase(PURPLE)
      setQuadColor(QUAD4, GREEN)
  else:
      setQuadColor(QUAD4, OFF)

  # animate()



