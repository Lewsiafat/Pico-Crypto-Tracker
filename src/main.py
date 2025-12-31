import time
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
import wifi_utils
import secrets
import crypto_api
from buttons import button_a, button_b

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
DARK_GREY = display.create_pen(30, 30, 30)

# 設定選項
COINS = ["bitcoin", "ethereum"]
INTERVALS = [10, 15, 30, 60]

def draw_status_bar(is_connected):
    """繪製頂部狀態列"""
    display.set_pen(BLACK)
    display.rectangle(0, 0, WIDTH, 40)
    
    color = GREEN if is_connected else RED
    display.set_pen(color)
    display.circle(WIDTH - 20, 20, 6)
    
    display.set_pen(GREY)
    display.text("PICO CRYPTO", 20, 12, WIDTH, 2)

def draw_info_bar(current_interval, target_coin):
    """繪製底部系統資訊欄"""
    display.set_pen(DARK_GREY)
    display.rectangle(0, HEIGHT - 30, WIDTH, 30)
    
    display.set_pen(GREY)
    display.text(f"FREQ: {current_interval}s", 10, HEIGHT - 22, WIDTH, 2)
    
    coin_text = f"COIN: {target_coin.upper()}"
    tw = display.measure_text(coin_text, 2)
    display.text(coin_text, WIDTH - tw - 10, HEIGHT - 22, WIDTH, 2)

def draw_price_page(coin_name, price, change_24h, interval):
    """繪製價格資訊頁面"""
    display.set_pen(BLACK)
    display.clear()
    
    draw_status_bar(wifi_utils.get_status())
    
    display.set_pen(GOLD)
    display.text(coin_name.upper(), 20, 60, WIDTH, 4)
    
    display.set_pen(WHITE)
    price_str = f"${price:,.2f}"
    scale = 5 if len(price_str) < 10 else 4
    display.text(price_str, 20, 110, WIDTH, scale)
    
    display.set_pen(GREY)
    display.text("24h Change:", 20, 180, WIDTH, 2)
    
    change_color = GREEN if change_24h >= 0 else RED
    display.set_pen(change_color)
    prefix = "+" if change_24h >= 0 else ""
    display.text(f"{prefix}{change_24h:.2f}%", 160, 180, WIDTH, 2)
    
    draw_info_bar(interval, coin_name)
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
    coin_idx = 0
    interval_idx = 1 # 預設 15s
    
    draw_splash("Switch Logic Demo...")
    time.sleep(1)
    
    # 初始化模擬資料
    current_price = 43125.50
    current_change = 2.45
    
    while True:
        # 偵測按鈕 A (切換幣種)
        if button_a.is_pressed():
            coin_idx = (coin_idx + 1) % len(COINS)
            print(f"Switched to coin: {COINS[coin_idx]}")
        
        # 偵測按鈕 B (切換頻率)
        if button_b.is_pressed():
            interval_idx = (interval_idx + 1) % len(INTERVALS)
            print(f"Switched to interval: {INTERVALS[interval_idx]}s")
        
        # 更新顯示 (模擬)
        draw_price_page(COINS[coin_idx], current_price, current_change, INTERVALS[interval_idx])
        
        time.sleep(0.01)
