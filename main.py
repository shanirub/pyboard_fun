# main.py -- put your code here!
import pyb

green = pyb.LED(2)
blue = pyb.LED(4)

while True:
    green.toggle()
    pyb.delay(1000)
    blue.toggle()
    pyb.delay(500)

    
