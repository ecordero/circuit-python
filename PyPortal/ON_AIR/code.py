# import time
# import board
# from adafruit_pyportal import PyPortal
# import terminalio
# from adafruit_display_text import label

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example shows the use color and background_color
"""
import time
import board
import displayio

from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label


#  Setup the SPI display
if "DISPLAY" in dir(board):
    # use built in display (PyPortal, PyGamer, PyBadge, CLUE, etc.)
    # see guide for setting up external displays (TFT / OLED breakouts, RGB matrices, etc.)
    # https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
    display = board.DISPLAY

else:
    print("Starting external display")  # goes to serial only
    # Setup the LCD display with driver
    # You may need to change this to match the display driver for the chipset
    # used on your display
    from adafruit_ili9341 import ILI9341

    # from adafruit_st7789 import ST7789

    displayio.release_displays()

    # setup the SPI bus
    spi = board.SPI()
    tft_cs = board.D9  # arbitrary, pin not used
    tft_dc = board.D10
    tft_backlight = board.D12
    tft_reset = board.D11

    while not spi.try_lock():
        spi.configure(baudrate=32000000)
    spi.unlock()

    display_bus = displayio.FourWire(
        spi,
        command=tft_dc,
        chip_select=tft_cs,
        reset=tft_reset,
        baudrate=32000000,
        polarity=1,
        phase=1,
    )

    # Number of pixels in the display
    DISPLAY_WIDTH = 320
    DISPLAY_HEIGHT = 240

    # display = ST7789(display_bus, width=240, height=240, rotation=0, rowstart=80, colstart=0)

    # create the display
    display = ILI9341(
        display_bus,
        width=DISPLAY_WIDTH,
        height=DISPLAY_HEIGHT,
        rotation=180,  # The rotation can be adjusted to match your configuration.
        auto_refresh=True,
        native_frames_per_second=90,
    )

display.show(None)

# font=terminalio.FONT # this is the Builtin fixed dimension font

font = bitmap_font.load_font("fonts/LeagueSpartan-Bold-16.bdf")

CUSTOMTEXT="ON AIR\nON AIR\nON AIR\nON AIR\nON AIR\nON AIR"
CUSTOMTEXT2="ON AIR ON AIR ON AIR\nON AIR ON AIR ON AIR"
text = []
text.append(CUSTOMTEXT)  # no ascenders or descenders
text.append(CUSTOMTEXT2)  # only descenders
# text.append("ON AIR !")  # only ascenders
# text.append("")  # both ascenders and descenders
# text.append("")  # with newline

display.auto_refresh = True
myGroup = displayio.Group()
display.show(myGroup)

myPadding = 250
MESSAGE=label.Label(
    font,
    text=CUSTOMTEXT,
    color=0xFFFFFF,
    # x=10,
    # y=10,
    anchor_point=(0, 0),
    anchored_position=(120, 10),
    background_color=0xFF0000,
    background_tight=False,
    padding_top=myPadding,
    padding_bottom=myPadding,
    padding_left=myPadding,
    padding_right=myPadding,
)
MESSAGE2=label.Label(
    font,
    text=CUSTOMTEXT2,
    color=0xFFFFFF,
    # x=10,
    # y=10,
    anchor_point=(0, 0),
    anchored_position=(47, 90),
    background_color=0xFF0000,
    background_tight=False,
    padding_top=myPadding,
    padding_bottom=myPadding,
    padding_left=myPadding,
    padding_right=myPadding,
)
messages = [MESSAGE, MESSAGE2]
text_area = []
text_area.append(MESSAGE)
text_area.append(MESSAGE2)



for i, thisText in enumerate(text):
    text_area.append(messages[i])
    myGroup.append(text_area[i])
        # label.Label(
        #     font,
        #     text=thisText,
        #     color=0xFFFFFF,
        #     background_tight=False,
        #     padding_top=myPadding,
        #     padding_bottom=myPadding,
        #     padding_left=myPadding,
        #     padding_right=myPadding,
        # )
    # )

#     this_x = 10
#     this_y = 10 + i * 40
#     text_area[i].x = 10
#     text_area[i].y = 3 + i * 50
#     text_area[i].anchor_point = (0, 0)
#     text_area[i].anchored_position = (this_x, this_y)
#     myGroup.append(text_area[i])

# myGroup.append(MESSAGE)
# print("background color is {}".format(text_area[0].background_color))


while True:
    time.sleep(2)
    text_area[0].text = ""  # change some text in an existing text box
    # Note: changed text must fit within existing number of characters
    # when the Label was created

    # text_area[0].background_color = 0xFF0000
    for area in text_area:
        area.color = 0xFFFFFF
        area.background_color = 0xFF0000
    # print("background color is {:06x}".format(text_area[0].background_color))
    time.sleep(2)
    for area in text_area:
        area.color = 0xFF0000
        area.background_color = 0xFFFFFF
    # print("background color is {:06x}".format(text_area[0].background_color))
    time.sleep(2)
    # for area in text_area:
    #     area.background_color = 0x00FF00
    # print("background color is {:06x}".format(text_area[0].background_color))
    # time.sleep(2)
    # for area in text_area:
    #     area.background_color = 0xFF0000
    # print("background color is {:06x}".format(text_area[0].background_color))
    # time.sleep(2)
    # for area in text_area:
    #     area.background_color = None
    # print("background color is {}".format(text_area[0].background_color))