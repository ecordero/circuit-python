# # SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# # SPDX-License-Identifier: MIT

# # CircuitPython NeoPixel Color Picker Example

# import board
# import neopixel

# from adafruit_bluefruit_connect.packet import Packet
# from adafruit_bluefruit_connect.color_packet import ColorPacket

# from adafruit_ble import BLERadio
# from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
# from adafruit_ble.services.nordic import UARTService
# # from adafruit_led_animation.animation import Pulse, Solid
# # import adafruit_led_animation.color as color

# ble = BLERadio()
# uart_service = UARTService()
# advertisement = ProvideServicesAdvertisement(uart_service)

# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

# # pulse = Pulse(pixels,
# #               speed=0.01,
# #               color=color.PURPLE,  # Use CYAN for Male Key
# #               period=3,
# #               min_intensity=0.0,
# #               max_intensity=0.5)



# while True:
#     # Advertise when not connected.
#     ble.start_advertising(advertisement)
#     while not ble.connected:
#         pass
#     ble.stop_advertising()

#     while ble.connected:
#       if uart_service.in_waiting:
#             packet = Packet.from_stream(uart_service)
#             if isinstance(packet, ColorPacket):
#                 print(packet.color)
#                 pixels.fill(packet.color)
#                 # pulse.animate()

import board
import neopixel


from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)#, brightness=0.1)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.UP:
                        # The 1 button was pressed.
                        print("UP button pressed!")
                        pixels.fill((255,0,0))

                    if packet.button == ButtonPacket.BUTTON_1:
                        # The 1 button was pressed.
                        print("1 button pressed!")
                        pixels.fill((255,255,255))

                    elif packet.button == ButtonPacket.DOWN:
                        # The UP button was pressed.
                        print("DOWN button pressed!")
                        pixels.fill((0,0,0))

    # If we got here, we lost the connection. Go up to the top and start
    # advertising again and waiting for a connection.

