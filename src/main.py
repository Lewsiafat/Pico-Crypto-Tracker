import time
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
import wifi_utils
import secrets
import crypto_api

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
    color = GREEN if is_connected else RED
    display.set_pen(color)
    display.circle(WIDTH - 20, 20, 8)
    
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
    
    draw_status_bar(wifi_utils.get_status())
    display.update()

if __name__ == "__main__":
    draw_splash("Connecting to Wi-Fi...")
    
    success, ip = wifi_utils.connect_wifi(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    
    if success:
        draw_splash("Fetching BTC Price...")
        # 測試 API
        api_success, price, change = crypto_api.get_crypto_price("bitcoin", "usd")
        if api_success:
            draw_splash(f"BTC: ${price:,.2f}")
        else:
            draw_splash("API Fetch Failed")
    else:
        draw_splash("Wi-Fi Failed")
    
    time.sleep(3)
    
    # 預留給下一個任務：完整的 UI 頁面
    display.set_pen(BLACK)
    display.clear()
    draw_status_bar(wifi_utils.get_status())
    display.set_pen(WHITE)
    display.text("Next: Detailed UI...", 20, 60, WIDTH, 2)
    display.update()
