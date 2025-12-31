from buttons import button_a, button_b
import time

print("--- Button Test Start ---")
print("Press Button A or B to test...")

while True:
    if button_a.is_pressed():
        print("Button A Pressed!")
    
    if button_b.is_pressed():
        print("Button B Pressed!")
    
    time.sleep(0.01) # 100Hz 採樣
