# 技術棧 - Pico Crypto Tracker

## 核心技術
*   **語言：** MicroPython (針對 Raspberry Pi Pico 2 W 優化)
*   **硬體：** 
    *   Raspberry Pi Pico 2 W (雙核 RP2350，具備 2.4GHz Wi-Fi)
    *   Pimoroni Pico Display Pack 2.8 (320x240 IPS LCD)

## 軟體庫與框架
*   **圖形顯示：** `picographics` - Pimoroni 提供的硬體加速圖形庫。
*   **網路連線：** `network` 模組 - 用於管理 Wi-Fi 連接。
*   **數據獲取：** `urequests` - 用於發送 HTTP GET 請求至加密貨幣 API。
*   **資料解析：** `ujson` - 用於解析 API 回傳的 JSON 格式數據。

## 開發工具
*   **IDE：** Visual Studio Code (配合 MicroPico 擴充套件)
*   **部署：** 透過 USB 直接將 `.py` 檔案傳輸至 Pico 2 W。
