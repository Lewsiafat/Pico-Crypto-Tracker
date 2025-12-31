from machine import Pin
import time

class ButtonHandler:
    def __init__(self, pin_num):
        # 嘗試使用 PULL_UP，若硬體已有外部上拉電阻亦不影響
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.last_state = 1  # 1 代表未按下
        self.debounce_time = 0

    def is_pressed(self):
        """
        偵測按鈕是否被「按下」。
        使用簡單的邊緣偵測與冷卻時間。
        """
        current_state = self.pin.value()
        now = time.ticks_ms()
        
        # 偵測按下動作 (從 1 變為 0)
        if self.last_state == 1 and current_state == 0:
            if time.ticks_diff(now, self.debounce_time) > 200: # 增加冷卻時間至 200ms
                self.debounce_time = now
                self.last_state = 0
                return True
        
        self.last_state = current_state
        return False

# 定義按鈕實例
button_a = ButtonHandler(12)
button_b = ButtonHandler(13)
button_x = ButtonHandler(14)
button_y = ButtonHandler(15)