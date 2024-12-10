from machine import Pin, ADC
from time import sleep


led_onboard = Pin(25, Pin.OUT)
adc = ADC(0)
led = PWM(led_onboard)
led.freq(1000)

while True:
    led.duty_u16(adc.read_u16())
          
    sleep(0.5)
