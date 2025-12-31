# Track Spec: Wi-Fi 動態配網與 QR Code 設定

## 1. 概觀 (Overview)
移除程式碼中硬編碼的 Wi-Fi 憑證，改為動態配網機制。當裝置無法連網或使用者手動觸發時，透過開啟 AP 模式與顯示 QR Code，引導使用者使用行動裝置完成網路設定。

## 2. 功能需求 (Functional Requirements)
*   **連線邏輯：**
    *   啟動時檢查是否存在 `wifi.json`。
    *   若存在，嘗試連線；若成功，進入主程式。
    *   若不存在或連線失敗，自動進入「設定模式」。
*   **設定模式 (Config Mode)：**
    *   **AP 模式：** 開啟 Access Point（例如 SSID: `Pico-Setup`）。
    *   **網頁伺服器：** 執行一個簡單的 Web Server，提供 Wi-Fi 掃描清單與密碼輸入頁面。
    *   **QR Code 顯示：** 在 2.8" 螢幕上生成並顯示 QR Code，掃描後自動連上 AP 或開啟設定網頁。
*   **手動觸發：** 支援在啟動時長按特定按鈕（如 X 鍵）強制清除舊設定並進入「設定模式」。
*   **資料持久化：** 將使用者設定的 SSID 與密碼儲存於 `src/wifi.json` 中。

## 3. 非功能需求 (Non-Functional Requirements)
*   **易用性：** 螢幕需顯示清楚的步驟指引（例如 "Scan QR to Setup"）。
*   **安全性：** 網頁伺服器僅在設定模式下運行。
*   **穩定性：** 儲存 JSON 時需處理異常情況，避免檔案損壞導致無法啟動。

## 4. 驗收標準 (Acceptance Criteria)
*   初次啟動時，裝置能正確顯示 QR Code 並開啟 AP。
*   使用手機掃描 QR Code 後，能進入設定頁面並看到周邊 Wi-Fi 清單。
*   提交設定後，裝置能自動儲存資料、重啟並成功連上目標 Wi-Fi。
*   長按指定按鈕能強制再次進入設定介面。

## 5. 範疇外 (Out of Scope)
*   不支援連線到需要 Web 認證的企業級 Wi-Fi (Captive Portal)。
*   不處理多組 Wi-Fi 憑證備份，僅儲存最後一組成功設定。
