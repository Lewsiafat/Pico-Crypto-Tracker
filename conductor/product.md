# Initial Concept
建立一個能顯示目前虛擬貨幣價格的應用.有一定的互動操作

# 產品指南 - Pico Crypto Tracker

## 產品願景
利用 Raspberry Pi Pico 2 W 的 Wi-Fi 能力與 Pimoroni Pico Display Pack 2.8 的大尺寸彩色螢幕，打造一個即時、美觀且具備互動性的加密貨幣監控裝置。

## 核心功能
*   **即時價格追蹤：** 透過 Wi-Fi 串接 API 獲取最新的虛擬貨幣價格（如 BTC, ETH 等）。
*   **多幣種切換：** 利用 Display Pack 上的四個實體按鈕（A, B, X, Y） or 選單界面，快速切換觀看的幣種。
*   **數據可視化：** 在 320x240 螢幕上顯示當前價格、24小時漲跌幅，以及簡單的趨勢圖表。
*   **互動選單：** 提供直覺的 UI 界面，方便使用者進行簡單的設定或切換顯示模式。

## 目標硬體
*   **控制器：** Raspberry Pi Pico 2 W (支援 Wi-Fi)
*   **顯示器/輸入：** Pimoroni Pico Display Pack 2.8 (320x240 IPS LCD + 4 個按鈕)
