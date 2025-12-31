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
GREY = display.create_pen(100, 100, 100)

def draw_status_bar(is_connected):
    """繪製頂部狀態列"""
    display.set_pen(BLACK)
    display.rectangle(0, 0, WIDTH, 40)
    
    # Wi-Fi 圖示
    color = GREEN if is_connected else RED
    display.set_pen(color)
    display.circle(WIDTH - 20, 20, 6)
    
    # 時間或標題
    display.set_pen(GREY)
    display.text("PICO CRYPTO", 20, 12, WIDTH, 2)

def draw_price_page(coin_name, price, change_24h):
    """繪製價格資訊頁面"""
    display.set_pen(BLACK)
    display.clear()
    
    draw_status_bar(wifi_utils.get_status())
    
    # 幣種名稱
    display.set_pen(GOLD)
    display.text(coin_name.upper(), 20, 60, WIDTH, 4)
    
    # 價格顯示
    display.set_pen(WHITE)
    price_str = f"${price:,.2f}"
    # 根據字度調整縮放
    scale = 5 if len(price_str) < 10 else 4
    display.text(price_str, 20, 110, WIDTH, scale)
    
    # 24h 漲跌幅
    display.set_pen(GREY)
    display.text("24h Change:", 20, 180, WIDTH, 2)
    
    change_color = GREEN if change_24h >= 0 else RED
    display.set_pen(change_color)
    prefix = "+" if change_24h >= 0 else ""
    display.text(f"{prefix}{change_24h:.2f}%", 160, 180, WIDTH, 2)
    
    display.update()

def draw_splash(message):
    """顯示訊息畫面"""
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(GOLD)
    title = "Pico Crypto Tracker"
    display.text(title, (WIDTH - display.measure_text(title, 3)) // 2, HEIGHT // 2 - 20, WIDTH, 3)
    display.set_pen(WHITE)
    display.text(message, (WIDTH - display.measure_text(message, 2)) // 2, HEIGHT // 2 + 40, WIDTH, 2)
    display.update()

if __name__ == "__main__":
    draw_splash("Connecting...")
    success, ip = wifi_utils.connect_wifi(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    
    if success:
        while True:
            api_success, price, change = crypto_api.get_crypto_price("bitcoin", "usd")
            if api_success:
                draw_price_page("Bitcoin", price, change)
            else:
                # 發生錯誤時顯示提示
                display.set_pen(RED)
                display.text("API Error, retrying...", 20, HEIGHT - 30, WIDTH, 2)
                display.update()
            
            # 每 60 秒更新一次
            time.sleep(15)
    else:
        draw_splash("Wi-Fi Failed!")
        time.sleep(5)