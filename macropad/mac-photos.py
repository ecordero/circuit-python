# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Mac Photos', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x000020, 'U', [Keycode.UP_ARROW]),
        (0x000000, '', []),
        # # 2nd row ----------
        (0x000020, '< L', [Keycode.LEFT_ARROW]),
        (0x006000, 'Enhance', [Keycode.COMMAND, 'e']),
        (0x000020, 'R >', [Keycode.RIGHT_ARROW]),
        # # 3rd row ----------
        (0x000000, '', []),
        (0x000020, 'D', [Keycode.DOWN_ARROW]),
        (0x000000, '', []),
        # # 4th row ----------
        # (0x800080, 'Ada', [Keycode.COMMAND, 't', -Keycode.COMMAND,
        #                    'www.adafruit.com\n']),   # Adafruit in new window
        # (0x004000, 'Grafton', [Keycode.COMMAND, 't', -Keycode.COMMAND,
        #                     'https://www.grafton-ma.gov\n']),   # Digi-Key in new window
        # (0x101010, 'Hacks', [Keycode.COMMAND, 't', -Keycode.COMMAND,
        #                      'www.hackaday.com\n']), # Hack-a-Day in new win
        # # Encoder button ---
        # (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
