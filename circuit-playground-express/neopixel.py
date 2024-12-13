# Circuit Playground digitalio example
# Circuit Playground NeoPixel
import time
import board
import neopixel
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
# buttonA.switch_to_input(pull=digitalio.Pull.DOWN)
# buttonB = digitalio.DigitalInOut(board.BUTTON_B)
# buttonB.switch_to_input(pull=digitalio.Pull.DOWN)
slider = digitalio.DigitalInOut(board.SLIDE_SWITCH)
slider.direction = digitalio.Direction.INPUT
slider.pull = digitalio.Pull.UP
# slider.switch_to_input(pull=digitalio.Pull.UP)

# while True:
#     if slider.value:  # button is pushed
#         led.value = True
#     else:
#         led.value = False

#     time.sleep(0.01)



pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01, auto_write=False)

# choose which demos to play
# 1 means play, 0 means don't!
color_dot_chase_demo = 0
zapp_demo = 1
color_chase_demo = 0
flash_demo = 0
rainbow_demo = 0
rainbow_cycle_demo = 0


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_dot_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        pixels.show()
        pixels[i] = OFF
        time.sleep(wait)
        pixels.show()


def zapp(color, wait):
    for i in range(10):
        pixels[i] = color
        pixels.show()
        # pixels[i] = OFF
        time.sleep(wait)
        # pixels.show()


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 10) + j * 5
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)


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
SLEEPTIME = 1
RAINBOWCYCLEDELAY = 0.05
RAINBOWDEMODELAY = 0.05

while True:
    if color_dot_chase_demo & slider.value:
        color_dot_chase(RED, CHASEDELAY)  # Increase the number to slow down the color chase
        color_dot_chase(YELLOW, CHASEDELAY)
        color_dot_chase(GREEN, CHASEDELAY)
        color_dot_chase(CYAN, CHASEDELAY)
        color_dot_chase(BLUE, CHASEDELAY)
        color_dot_chase(PURPLE, CHASEDELAY)
        # color_dot_chase(OFF, CHASEDELAY)

    if zapp_demo & buttonA.value:
        zapp(RED, ZAPPDELAY)  # Increase the number to slow down the color chase
        # zapp(YELLOW, ZAPPDELAY)
        # zapp(GREEN, ZAPPDELAY)
        # zapp(CYAN, ZAPPDELAY)
        # zapp(BLUE, ZAPPDELAY)
        # zapp(PURPLE, ZAPPDELAY)
        zapp(OFF, ZAPPDELAY)

    if color_chase_demo & slider.value:
        color_chase(RED, CHASEDELAY)  # Increase the number to slow down the color chase
        color_chase(YELLOW, CHASEDELAY)
        color_chase(GREEN, CHASEDELAY)
        color_chase(CYAN, CHASEDELAY)
        color_chase(BLUE, CHASEDELAY)
        color_chase(PURPLE, CHASEDELAY)
        color_chase(OFF, CHASEDELAY)

    if flash_demo & slider.value:
        pixels.fill(RED)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(SLEEPTIME)
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(SLEEPTIME)
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(SLEEPTIME)
        pixels.fill(WHITE)
        pixels.show()
        time.sleep(SLEEPTIME)

    if rainbow_cycle_demo & slider.value:
        rainbow_cycle(RAINBOWCYCLEDELAY)  # Increase the number to slow down the rainbow.

    if rainbow_demo & slider.value:
        rainbow(RAINBOWDEMODELAY)  # Increase the number to slow down the rainbow.

