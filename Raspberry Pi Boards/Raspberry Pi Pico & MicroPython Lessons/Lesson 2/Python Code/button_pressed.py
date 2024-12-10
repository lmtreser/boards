from machine import Pin
from time import sleep

button_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button_pin.value() == 1:
        sleep(0.2)
        print("the button has been pressed")

        

