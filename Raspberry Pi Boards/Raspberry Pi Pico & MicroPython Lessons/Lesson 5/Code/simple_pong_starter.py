from machine import Pin, PWM, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep 
from random import randint

i2c = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
oled = SSD1306_I2C(128,64,i2c)
# connect potentiometers to ADC0 and ADC1
adc = ADC(0)

            
        
oled.fill_rect(30,  62, PAD_WIDTH, PAD_HEIGHT, 1) # fill with 1s

def draw_ball():
    oled.fill_rect(ball_x, ball_y, 4, 4, 1) #


PAD_WIDTH = 2
PAD_HEIGHT = 2
HALF_PAD_WIDTH = int(PAD_WIDTH / 2)
HALF_PAD_HEIGHT = int(PAD_HEIGHT / 2)


score = 0

# start with the ball in the center
ball = int(HALF_WIDTH)

# set the initial directinon to down to the right
ball_dir = 1


def convert (x, in_min, in_max, out_min, out_max):
    return (x -in_min) * (out_max - out_min) // (in_max - in_min) + out_min


# The main event loop
while True:
    oled.fill(0) 

    x_cursor = convert(x_adc.read_u16(),0, 65535, 125, 3)


    draw_paddle(1, x_cursor)

    draw_ball()

    #update ball position with the current directions
    ball_x = ball_x + ball_x_dir
    ball_y = ball_y + ball_y_dir

    # update the ball direction if we are at the top or bottom edge
    if ball_y < 0:
        ball_y_dir = 1
        
    if ball_y > HEIGHT - 3:
        ball_y_dir = -1
       

    # if it hits the paddle bounce else score
    if ball_x < 1:
        top_paddle = x_cursor  - HALF_PAD_HEIGHT
        bottom_paddle = x_cursor  + HALF_PAD_HEIGHT
        if ball_y > top_paddle and ball_y < bottom_paddle:
            # we have a hit
            ball_x_dir = 1
            ball_x = 2
            print('paddle hit on left edge', x_cursor , top_paddle, bottom_paddle)
        else:
            # we have a score for the right player
            r_score += 1
            ball_x = int(HALF_WIDTH)
            ball_y = int(HALF_HEIGHT)
            ball_x_dir = randint(-1, 2)
            if ball_x_dir == 0:
                ball_x_dir = 1
            ball_y_dir = randint(-1, 2)
            print('score on left edge', x_cursor , top_paddle, bottom_paddle)
            sleep(.25)

    if ball_x > WIDTH - 3:
        ball_x = WIDTH - 4
        top_paddle = y_cursor  - HALF_PAD_HEIGHT
        bottom_paddle = y_cursor  + HALF_PAD_HEIGHT
        if ball_y > top_paddle and ball_y < bottom_paddle:
            ball_x_dir = -1
            print('bounce on right paddle', y_cursor , top_paddle, bottom_paddle)
        else:
            l_score += 1
            ball_x = int(HALF_WIDTH)
            ball_y = int(HALF_HEIGHT)
            ball_x_dir = randint(-1, 2)
            if ball_x_dir == 0:
                ball_x_dir = 1
            ball_y_dir = randint(-1, 2)
            print('score on right edge', y_cursor , top_paddle, bottom_paddle)
            sleep(.25)

    oled.text(str(l_score), HALF_WIDTH - 20, 5, 1)

    oled.text(str(r_score), HALF_WIDTH + 5, 5, 1)

    oled.show()