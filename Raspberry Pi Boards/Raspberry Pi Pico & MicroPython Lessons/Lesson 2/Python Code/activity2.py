from machine import Pin
from time import sleep, ticks_ms

# Declare variables
led_onboard = Pin("LED", Pin.OUT)
button_left = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_right = Pin(17, Pin.IN, Pin.PULL_DOWN)

print("Ready")
print("Get set")
print("GO!!!!!!!")

# Initialise scores and timing
score_left = 0
score_right = 0
timeout_ms = 30000  # 30 seconds in milliseconds
start_time = ticks_ms()

while ticks_ms() - start_time < timeout_ms:
    if button_right.value() == 1:
        sleep(0.1)
        score_right += 1
        
    if button_left.value() == 1:
        sleep(0.1)
        score_left += 1

# Print the final scores
print(f"Score left: {score_left}, Score right: {score_right}")



