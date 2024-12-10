from machine import Pin
from time import sleep

led_red = Pin(15, Pin.OUT)

while True:
    led_red.value(1)