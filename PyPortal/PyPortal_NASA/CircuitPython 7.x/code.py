import time
import board
from adafruit_pyportal import PyPortal
# This version requires an SD card
# Set up where we'll be fetching data from
# NASA_KEY = 'sFvcDSUE7LBwXtiipPY821omNEh5sVlPvhpe68aa'
DATA_SOURCE = "https://api.nasa.gov/planetary/apod?api_key=sFvcDSUE7LBwXtiipPY821omNEh5sVlPvhpe68aa"
# There's a few different places we look for data in the photo of the day
IMAGE_LOCATION = ["url"]
TITLE_LOCATION = ["title"]
DATE_LOCATION = ["date"]

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=(TITLE_LOCATION, DATE_LOCATION),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/nasa_background.bmp",
                    text_font=cwd+"/fonts/Arial-12.bdf",
                    text_position=((5, 220), (5, 200)),
                    text_color=(0xFFFFFF, 0xFFFFFF),
                    text_maxlen=(50, 50), # cut off characters
                    image_json_path=IMAGE_LOCATION,
                    image_resize=(320, 240),
                    image_position=(0, 0))

while True:
    response = None
    try:
        response = pyportal.fetch()
        print("Response is", response)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)

    time.sleep(30*60)  # 30 minutes till next check
