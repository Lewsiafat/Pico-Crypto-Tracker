# Pico-Crypto-Tracker 🚀

A real-time cryptocurrency price monitor for **Raspberry Pi Pico 2 W** and **Pimoroni Pico Display Pack 2.8"**.

This project provides a sleek, hardware-accelerated dashboard to track live crypto prices directly on your desktop. Built with MicroPython, it handles Wi-Fi connectivity, secure API fetching, and non-blocking user interactions.

## ✨ Features

- **Live Price Tracking:** Real-time data fetched via the CoinGecko API.
- **Multi-Coin Support:** Cycle between **BTC** and **ETH** using physical **Button A**.
- **Dynamic Intervals:** Cycle through update frequencies (**10s, 15s, 30s, 60s**) using **Button B**.
- **Modern UI:** Optimized 320x240 "Modern Dark" interface with color-coded price changes (Green for up, Red for down).
- **System Status Bar:** Real-time feedback for Wi-Fi signal, update countdown, and target coin.
- **Robustness:** Built-in protection against API Rate Limiting (Error 429).

## 🛠 Hardware Requirements

- **Microcontroller:** Raspberry Pi Pico 2 W.
- **Display:** [Pimoroni Pico Display Pack 2.8"](https://shop.pimoroni.com/products/pico-display-pack-2-8) (320x240 IPS LCD).
- **Firmware:** MicroPython with `picographics` support (Pimoroni's custom build recommended).

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Pico-Crypto-Tracker.git
```

### 2. Configure Wi-Fi
Navigate to the `src/` directory. Copy `secrets.py.example` to `secrets.py` and enter your credentials:
```python
WIFI_SSID = "Your_WiFi_Name"
WIFI_PASSWORD = "Your_WiFi_Password"
```

### 3. Upload Code
Upload the contents of the `src/` directory to your Pico:
- `main.py` (Entry point)
- `wifi_utils.py` (Network management)
- `crypto_api.py` (API module)
- `buttons.py` (Button handler)
- `secrets.py` (Private credentials)

### 4. Run
Restart your Pico. It will automatically connect to Wi-Fi and start displaying live prices.

## 🖱 Controls

- **Button A:** Cycle through Coins (BTC -> ETH -> BTC).
- **Button B:** Cycle through Update Intervals (10s -> 15s -> 30s -> 60s).

## 📝 Development Notes

- Developed using the **Conductor** spec-driven framework.
- Uses `time.ticks_ms()` for non-blocking execution, ensuring responsive button sensing.
- The `secrets.py` file is ignored by Git to keep your credentials safe.

---
Created at the turn of 2025 🎆