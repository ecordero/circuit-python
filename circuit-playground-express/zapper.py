from adafruit_circuitplayground import cp
import time

NUMPIX = 10

RED = (255, 0, 0)
YELLOW = (255, 125, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

MODE = 'off'

cp.pixels.brightness = 0.1
cp.pixels.fill(OFF)  # Turn off the NeoPixels if they're on!
def zaptone():
    i = 0
    f = 15
    for i in range(NUMPIX):
        cp.start_tone(i + f)
        cp.pixels.fill(RED)
        # cp.pixels.fill(OFF)
        cp.pixels[i] = YELLOW
        cp.pixels.fill(OFF)
        cp.pixels.brightness = 0.5
        # cp.pixels.show()
        time.sleep(0.012)
        # cp.pixels[i] = OFF
        # cp.pixels.show()

def stunSequence():
    i = 0
    f = 15
    for i in range(NUMPIX):
        cp.start_tone(i + f)
        cp.pixels.fill(BLUE)
        # cp.pixels.fill(OFF)
        cp.pixels[i] = PURPLE
        # cp.pixels.fill(OFF)
        cp.pixels.brightness = 0.5
        cp.stop_tone()

def loadingtone():
    i = 0
    f = 100
    cp.pixels.brightness = 0.5
    for i in range(NUMPIX):
        cp.start_tone(i + f, 0.125)
        # cp.pixels(GREEN)
        cp.pixels[i] = GREEN
        time.sleep(0.125)
    cp.stop_tone()
    cp.pixels.fill(OFF)
def runSound(tone):
    if tone == 'poweredup':
        FREQ = 1000
        SLEEPTIME = 0.01
        cp.start_tone(FREQ)
        time.sleep(SLEEPTIME)
        cp.stop_tone()
        cp.start_tone(FREQ)
        time.sleep(SLEEPTIME)
        cp.stop_tone()
    if tone == 'stunmode':
        FREQ = 200
        SLEEPTIME = 0.01
        cp.start_tone(FREQ)
        time.sleep(SLEEPTIME)
        cp.stop_tone()
        cp.start_tone(FREQ)
        time.sleep(SLEEPTIME)
        cp.stop_tone()
    else:
        cp.stop_tone()

def confirmZapMode():
    DELAY = 0.325
    cp.pixels.fill(OFF)
    time.sleep(DELAY)
    runSound('poweredup')
    cp.pixels.brightness = 0.0625
    cp.pixels.fill(GREEN)

def startupSequence():
    DELAY = 0.1
    i = 0
    for i in range(10):
        cp.pixels.brightness = 0.5
        cp.pixels[i] = GREEN
        time.sleep(DELAY)
    confirmZapMode()

def setMode(mode):
    MODE = mode
    if MODE == 'zap':
        confirmZapMode()
    if MODE == 'stun':
        runSound('stunmode')
        cp.pixels.fill(BLUE)

startupSequence()

while True:
    if cp.button_a:
        i = 0
        f = 15
        for i in range(10):
            cp.start_tone(i + f)
            cp.pixels.fill(RED)
            # cp.pixels.fill(OFF)
            cp.pixels[i] = YELLOW
            cp.pixels.fill(OFF)
            cp.pixels.brightness = 0.5
            # cp.pixels.show()
            time.sleep(0.012)
            # cp.pixels[i] = OFF
            # cp.pixels.show()
    elif cp.button_b:
        cp.start_tone(294)
        cp.pixels[7] = (0, 0, 255)
    elif cp.touch_A1 and cp.touch_A2:
        cp.pixels.fill(GREEN)
    elif cp.touch_A1:
        cp.pixels.fill(YELLOW)
    elif cp.touch_A2:
        setMode('stun')
    elif cp.touch_A3:
        zaptone()
    elif cp.touch_A4:
        loadingtone()
    elif cp.touch_A6:
        stunSequence()
    else:
        cp.stop_tone()
        # if mode == 'zap':
        #     cp.pixels.fill(GREEN)
        # elif mode == 'stun':
        #     cp.pixels.fill(BLUE)
        # else:
        #     cp.pixels.fill(OFF)
