# Project Workflow

## Guiding Principles

1. **The Plan is the Source of Truth:** All work must be tracked in `plan.md`
2. **The Tech Stack is Deliberate:** Changes to the tech stack must be documented in `tech-stack.md` *before* implementation
3. **User Experience First:** Every decision should prioritize user experience
4. **Keep it Simple:** Avoid over-engineering. Focus on functionality and reliability.

## Task Workflow

All tasks follow a strict lifecycle:

### Standard Task Workflow

1. **Select Task:** Choose the next available task from `plan.md` in sequential order.

2. **Create Task Branch:** 為每個任務建立一個專屬的 Git 分支。
   ```bash
   git checkout -b task/description-of-task
   ```

3. **Mark In Progress:** Before beginning work, edit `plan.md` and change the task from `[ ]` to `[~]`.

4. **Implementation:** 
   - 根據技術棧與產品指南實作功能。
   - 確保代碼符合 `conductor/code_styleguides/` 中的規範。

5. **Manual Verification:** 
   - 由於 MicroPython 環境限制，必須在硬體或模擬器上進行手動測試。
   - 驗證功能是否符合預期，並檢查 UI 是否正確顯示。

6. **Commit Code Changes:** 
   - Stage all code changes related to the task.
   - 使用清楚、簡潔的 Commit Message，例如：`feat(ui): Add BTC price display`。
   - Perform the commit.

7. **Merge to Main:** 將完成的分支合併回 `main` 分支並刪除任務分支。
   ```bash
   git checkout main
   git merge task/description-of-task
   git branch -d task/description-of-task
   ```

8. **Record Task Commit SHA:**
   - **Step 8.1: Update Plan:** Read `plan.md`, find the line for the completed task, update its status from `[~]` to `[x]`, and append the first 7 characters of the merge commit hash.
   - **Step 8.2: Write Plan:** Write the updated content back to `plan.md`.

9. **Commit Plan Update:**
   - **Action:** Stage the modified `plan.md` file.
   - **Action:** Commit this change with a descriptive message (e.g., `conductor(plan): Mark task 'Add BTC display' as complete`).

### Phase Completion Verification Protocol

**Trigger:** This protocol is executed immediately after a task is completed that also concludes a phase in `plan.md`.

1.  **Announce Protocol Start:** Inform the user that the phase is complete.
2.  **Manual Verification Plan:** 提供詳細的步驟讓使用者在硬體上驗證整個階段的功能。
3.  **Await Explicit User Feedback:** 暫停並等待使用者確認（輸入 "yes"）。
4.  **Create Checkpoint Commit:** 執行一個 Checkpoint 提交。
5.  **Record Phase Checkpoint SHA:** 在 `plan.md` 的階段標題後方註記 SHA 碼。

## Definition of Done

A task is complete when:

1. All code implemented to specification.
2. Manually verified on Raspberry Pi Pico 2 W hardware.
3. Code follows project's code style guidelines.
4. Changes merged into `main` branch.
5. Implementation notes and SHA added to `plan.md`.
6. Changes committed with proper message.