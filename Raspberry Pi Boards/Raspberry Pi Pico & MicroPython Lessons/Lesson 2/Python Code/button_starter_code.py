from machine import Pin
from time import sleep

button_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button_pin.value())
    sleep(0.1)

        

