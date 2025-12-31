import network
import time

def connect_wifi(ssid, password, timeout=10):
    """
    連接至指定的 Wi-Fi 網路。
    回傳: (success, ip_address)
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # 等待連線
    start_time = time.time()
    while not wlan.isconnected() and (time.time() - start_time) < timeout:
        time.sleep(1)
        print("Connecting to Wi-Fi...")

    if wlan.isconnected():
        status = wlan.ifconfig()
        print(f"Connected! IP: {status[0]}")
        return True, status[0]
    else:
        print("Wi-Fi connection failed.")
        return False, None

def get_status():
    """獲取目前連線狀態"""
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()
