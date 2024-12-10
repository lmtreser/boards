from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 400000)
oled = SSD1306_I2C(WIDTH,HEIGHT, i2c)

oled.fill(0)
oled.text("welcome to the Pico", 0,0)
oled.text("", 0, 40)
oled.show()