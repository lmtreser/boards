from machine import Pin
from time import sleep
# not that is you are using PICO W the pin 25 should be replaced with "LED"
led_onboard = Pin(25, Pin.OUT)


while True:
   
    led_onboard.value(1)
    sleep(1)
    led_onboard.value(0)
    sleep(1)


