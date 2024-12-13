from adafruit_circuitplayground.express import cpx
import board
import touchio

# touch = touchio.TouchIn_A1
touch = touchio.TouchIn(board.A1)

while True:
    if cpx.switch:
        if cpx.button_a:
            print("Temperature : ", cpx.temperature)
        if cpx.button_b:
            print("Light : ", cpx.light)
    else:
        print(touch.raw_value)
