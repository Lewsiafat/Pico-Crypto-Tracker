# Track Plan: Wi-Fi 動態配網與 QR Code 設定

## Phase 1: 基礎存儲與 QR Code 顯示
- [ ] Task: 實作憑證存儲模組 (處理 `wifi.json` 的讀寫與校驗)
- [ ] Task: 整合 QR Code 生成庫，並在 2.8" 螢幕上實作「設定模式」指引畫面
- [ ] Task: Conductor - User Manual Verification '基礎存儲與 QR Code 顯示' (Protocol in workflow.md)

## Phase 2: AP 模式與配網服務器
- [ ] Task: 實作 AP 模式啟用邏輯與周邊 Wi-Fi 掃描功能
- [ ] Task: 開發輕量級 Web Server 與 HTML 設定頁面 (SSID 選擇與密碼輸入)
- [ ] Task: 實作配網結果處理與自動重啟邏輯
- [ ] Task: Conductor - User Manual Verification 'AP 模式與配網服務器' (Protocol in workflow.md)

## Phase 3: 流程整合與觸發機制
- [ ] Task: 重構 `main.py` 與 `wifi_utils.py` 以整合動態配網流程
- [ ] Task: 實作手動觸發機制 (啟動時長按 X 鍵進入設定模式)
- [ ] Task: 移除專案中剩餘的硬編碼密碼邏輯並進行最終清理
- [ ] Task: Conductor - User Manual Verification '流程整合與觸發機制' (Protocol in workflow.md)
