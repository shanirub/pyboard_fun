# main.py -- put your code here!
import pyb
led = pyb.LED(2)
while true:
    led.toggle()
    pyb.delay(1000)