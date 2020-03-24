# main.py -- put your code here!
import pyb

accel = pyb.Accel()
light = pyb.LED(4)
light.on()
intensity = 0

SENSITIVITY = 3

while True:
    x = accel.x()
    if abs(x) > SENSITIVITY:
        intensity = round(x * 8.5) % 255
        light.intensity(intensity)

    pyb.delay(100)

