import time
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
import wifi_utils
import secrets

# 初始化螢幕
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(0.8)

WIDTH, HEIGHT = display.get_bounds()

# 定義顏色
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
GOLD = display.create_pen(255, 215, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)

def draw_status_bar(is_connected):
    """繪製頂部狀態列與 Wi-Fi 圖示"""
    # 繪製 Wi-Fi 圖示 (圓點)
    color = GREEN if is_connected else RED
    display.set_pen(color)
    display.circle(WIDTH - 20, 20, 8)
    
    # 繪製連線文字
    display.set_pen(WHITE)
    status_text = "Wi-Fi: Connected" if is_connected else "Wi-Fi: Disconnected"
    display.text(status_text, WIDTH - 180, 12, WIDTH, 1)

def draw_splash(message="Initializing..."):
    """繪製啟動畫面"""
    display.set_pen(BLACK)
    display.clear()
    
    display.set_pen(GOLD)
    title = "Pico Crypto Tracker"
    scale = 3
    tw = display.measure_text(title, scale)
    display.text(title, (WIDTH - tw) // 2, HEIGHT // 2 - 20, WIDTH, scale)
    
    display.set_pen(WHITE)
    sw = display.measure_text(message, 2)
    display.text(message, (WIDTH - sw) // 2, HEIGHT // 2 + 40, WIDTH, 2)
    
    # 繪製狀態列
    draw_status_bar(wifi_utils.get_status())
    
    display.update()

if __name__ == "__main__":
    # 1. 顯示初始啟動畫面
    draw_splash("Connecting to Wi-Fi...")
    
    # 2. 嘗試連線 Wi-Fi
    success, ip = wifi_utils.connect_wifi(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    
    if success:
        draw_splash(f"Connected! IP: {ip}")
    else:
        draw_splash("Wi-Fi Connection Failed")
    
    time.sleep(3)
    
    # 3. 主循環預留位置
    display.set_pen(BLACK)
    display.clear()
    draw_status_bar(wifi_utils.get_status())
    display.set_pen(WHITE)
    display.text("Waiting for API...", 20, 60, WIDTH, 2)
    display.update()