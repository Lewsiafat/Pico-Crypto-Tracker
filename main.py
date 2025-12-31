import time
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

# 初始化螢幕
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(0.8)

WIDTH, HEIGHT = display.get_bounds()

# 定義顏色
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
GOLD = display.create_pen(255, 215, 0)

def draw_splash():
    """繪製啟動畫面"""
    display.set_pen(BLACK)
    display.clear()
    
    # 繪製標題 (金色)
    display.set_pen(GOLD)
    title = "Pico Crypto Tracker"
    scale = 3
    tw = display.measure_text(title, scale)
    display.text(title, (WIDTH - tw) // 2, HEIGHT // 2 - 20, WIDTH, scale)
    
    # 繪製副標題 (白色)
    display.set_pen(WHITE)
    subtitle = "Initializing..."
    scale = 2
    sw = display.measure_text(subtitle, scale)
    display.text(subtitle, (WIDTH - sw) // 2, HEIGHT // 2 + 40, WIDTH, scale)
    
    display.update()

if __name__ == "__main__":
    draw_splash()
    # 暫停三秒以便觀察啟動畫
    time.sleep(3)
    
    # 之後會跳轉到主循環
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.text("Hardware Ready.", 20, 20, WIDTH, 2)
    display.update()
