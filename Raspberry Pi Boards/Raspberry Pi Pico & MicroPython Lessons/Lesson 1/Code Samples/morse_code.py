from machine import Pin
from time import sleep
# not that is you are using PICO W the pin 25 should be replaced with "LED"
led_onboard = Pin("LED", Pin.OUT)


while True:
    for i in range(6):
        led_onboard.toggle()
        sleep(1)
    for i in range(6):
        led_onboard.toggle()
        sleep(0.5)
    for i in range(6):
        led_onboard.toggle()
        sleep(1)

