# main.py -- put your code here!
import pyb

leds = [pyb.LED(i) for i in range(1,5)]
led = pyb.LED(4)

for l in leds:
    l.off()

intensity = 0
n = 0

while True:
    n = (n + 1) % 4
    leds[n].toggle()
    intensity = (intensity + 1) % 255
    led.intensity(intensity)
    pyb.delay(20)




