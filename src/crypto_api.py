import urequests
import ujson

def get_crypto_price(coin_id="bitcoin", currency="usd"):
    """
    從 CoinGecko 獲取虛擬貨幣價格。
    回傳: (success, price, price_change_24h)
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}&include_24hr_change=true"
    
    try:
        print(f"Fetching price for {coin_id}...")
        response = urequests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            price = data[coin_id][currency]
            change = data[coin_id].get(f"{currency}_24h_change", 0)
            response.close()
            return True, price, change
        else:
            print(f"API Error: {response.status_code}")
            response.close()
            return False, 0, 0
    except Exception as e:
        print(f"Connection Error: {e}")
        return False, 0, 0
