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
    display.set_pen(BLACK)
    display.rectangle(0, 0, WIDTH, 40)
    color = GREEN if is_connected else RED
    display.set_pen(color)
    display.circle(WIDTH - 20, 20, 6)
    display.set_pen(GREY)
    display.text("PICO CRYPTO", 20, 12, WIDTH, 2)

def draw_info_bar(current_interval, target_coin, next_update_in=None):
    display.set_pen(DARK_GREY)
    display.rectangle(0, HEIGHT - 30, WIDTH, 30)
    display.set_pen(GREY)
    
    # 顯示頻率與倒數 (若有)
    freq_text = f"FREQ: {current_interval}s"
    if next_update_in is not None:
        freq_text += f" ({next_update_in}s)"
    display.text(freq_text, 10, HEIGHT - 22, WIDTH, 2)
    
    coin_text = f"COIN: {target_coin.upper()}"
    tw = display.measure_text(coin_text, 2)
    display.text(coin_text, WIDTH - tw - 10, HEIGHT - 22, WIDTH, 2)

def draw_price_page(coin_name, price, change_24h, interval, next_update_in):
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
    draw_info_bar(interval, coin_name, next_update_in)
    display.update()

def draw_splash(message):
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
    
    draw_splash("Connecting to Wi-Fi...")
    success, ip = wifi_utils.connect_wifi(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    
    if success:
        last_update_time = 0
        price = 0
        change = 0
        need_initial_fetch = True
        
        while True:
            current_time = time.time()
            current_coin = COINS[coin_idx]
            current_interval = INTERVALS[interval_idx]
            
            # 偵測按鈕 A (切換幣種)
            if button_a.is_pressed():
                coin_idx = (coin_idx + 1) % len(COINS)
                # 切換幣種後不立即更新 API，等下一次循環
            
            # 偵測按鈕 B (切換頻率)
            if button_b.is_pressed():
                interval_idx = (interval_idx + 1) % len(INTERVALS)
                # 頻率切換會即時影響下一次更新時間
            
            # 判斷是否需要更新 API
            time_since_update = current_time - last_update_time
            if need_initial_fetch or time_since_update >= current_interval:
                print(f"Updating price for {current_coin}...")
                api_success, new_price, new_change = crypto_api.get_crypto_price(current_coin, "usd")
                
                # 無論成功或失敗，都更新 last_update_time 以重設倒數計時
                last_update_time = current_time
                need_initial_fetch = False
                
                if api_success:
                    price, change = new_price, new_change
                else:
                    print("API update failed, will retry in next interval...")
            
            # 計算下次更新倒數
            next_update_in = max(0, current_interval - (current_time - last_update_time))
            
            # 渲染 UI (每一幀更新一次，以確保按鈕反應與倒數顯示靈敏)
            draw_price_page(current_coin, price, change, current_interval, int(next_update_in))
            
            # 稍微降低 CPU 負擔
            time.sleep(0.05)
    else:
        draw_splash("Wi-Fi Connection Failed")
        while True:
            time.sleep(1)