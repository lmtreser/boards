from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep

#set up OLED on pins and 
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)

x_adc = ADC(0)
y_adc = ADC(1)

last_x_cursor = 0
last_y_cursor = 0


# add btn to clear screen
button_left = Pin(14, Pin.IN, Pin.PULL_DOWN)

def convert (x, in_min, in_max, out_min, out_max):
    return (x -in_min) * (out_max - out_min) // (in_max - in_min) + out_min
oled.text("Etch a Sketch",0,0)

while True:
#     set cursor values and direction
    x_cursor = convert(x_adc.read_u16(),0, 65535, 125, 3)
    y_cursor = convert(y_adc.read_u16(),0, 65535, 62, 2)
    
    print(y_cursor,x_cursor)
    
# remove cursor shake adjust as needed to smooth lines  
   
    if abs(x_cursor - last_x_cursor) <2:
        x_cursor = last_x_cursor
    if abs(y_cursor - last_y_cursor) <2:
        y_cursor = last_y_cursor
        
# create a dot at each point placement of the cursor
    oled.text(".", x_cursor, y_cursor)
    
    # oled.ellipse( x_cursor, y_cursor, 1, 1, 1)
    oled.show()
#     small sleep allows for screen refresh adjust this tosuit your screen
    sleep(0.001)
#     keep track of the cursor last position 
    last_x_cursor = x_cursor
    last_y_cursor = y_cursor
#     clear button to clear the screen
    if button_left.value() == 1: #If button 1 is pressed
        oled.fill(0)
        oled.show()
