# Arkanoid 打磚塊

<img src="https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/logo.png" alt="logo" width="100"/> 

![arkanoid](https://img.shields.io/github/v/tag/PAIA-Playful-AI-Arena/arkanoid)
[![Python 3.9](https://img.shields.io/badge/python->3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![MLGame](https://img.shields.io/badge/MLGame->10.4.6a2-<COLOR>.svg)](https://github.com/PAIA-Playful-AI-Arena/MLGame)


打磚塊(Arkanoid)可是世界上最古老經典遊戲之一，設計你的 AI 移動板子，將球打向磚塊，破壞所有磚塊得到勝利，快來成為厲害的打磚塊大師！

- `遊戲目標` &nbsp;&nbsp;&nbsp;破壞所有磚塊

- `失敗條件` &nbsp;&nbsp;&nbsp;沒有接到球

<img src="https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/arkanoid.gif" height="500"/>

# 更新內容(3.0.1)
1. 更新遊戲物件尺寸，更新遊戲畫面
2. 調整資料格式，符合 `MLGame 10.4.6a2` 以後版本

---
# **啟動方式**

- 直接啟動 [main.py](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/main.py) 即可執行

# **遊戲參數設定**

```python
# main.py 
game = Arkanoid(level=3, level_file=None)
```
- `level`：指定關卡地圖。可以指定的關卡地圖皆在 `./asset/level_data/` 裡
- `level_file`：也可以使用自己設計的關卡地圖。


# 座標系統
![座標系統](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/game-web-readme/dev/arkanoid/images/side1.png)
- 使用 pygame 座標系統，`左上角為 (0,0)`，`X軸` 以 `右` 為正，`Y軸` 以 `下` 為正，單位為 px。
- 本遊戲所提供的座標，皆是物體`左上角`的座標
- 螢幕大小 200 x 500
- 板子 40 x 10
- 球 10 x 10
- 磚塊、硬磚塊 25 x 10

## **玩法**

- 發球：左邊/右邊：A / D
- 移動板子：左右方向鍵


# 遊戲物件

## 板子

- 綠色長方形。
- 每一影格的移動速度是 (±5, 0)。
- 初始位置在 (75, 400) 此數值為物件`左上角`的座標。

## 球

- 藍色正方形。
- 每一影格的移動速度是 (±7, ±7)。
- 球會從板子所在的位置發出，可以選擇往左或往右發球。
- 如果在 150 影格內沒有發球，則會自動往隨機兩個方向發球。
- 初始位置在 (93, 395) 此數值為物件`左上角`的座標。

## 磚塊

- 橘色長方形。
- 其位置由關卡地圖決定。

## 硬磚塊

- 紅色長方形。
- 硬磚塊要被打`兩次`才會被破壞。被球打到會變成一般磚塊。但是如果被`加速`後的球打到，則可以直接被破壞。


## 切球機制
![切球機制](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/game-web-readme/dev/arkanoid/images/side2.png)
- 球的 `X軸` 速度會因為接球時板子的移動方向而改變：
  1. 板子與球的移動方向`相同`，球的 `X軸` 速度會增為 `±10`，可以一次打掉硬磚塊
  2. 板子與球的移動方向`相反`，球會被打回`反方向`，速度為 `±7`
  3. 板子不動，球依照反彈原理反彈，速度為 `±7`

# 自訂關卡地圖
除了 PAIA 提供的關卡，你也可以嘗試自行設計關卡，讓磚塊出現在不同位置來營造更多遊戲樂趣，也可以使用[地圖編輯器](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/tool/arkanoid_map_editor.exe)自行編輯地圖。


# 適用賽制
- `闖關賽`
---

# **進階說明**

## 使用ＡＩ玩遊戲

```bash
# 在 arkanoid 資料夾中打開終端機 
 python -m mlgame -i ./ml/ml_play_template.py . --difficulty NORMAL --level 5 
```

## ＡＩ範例

```python

class MLPlay:
    def __init__(self,ai_name, *args, **kwargs):
        """
        Constructor
        """
        print(ai_name)

    def update(self, scene_info, *args, **kwargs):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
                scene_info["status"] == "GAME_PASS"):
            return "RESET"
        if not scene_info["ball_served"]:
            command = "SERVE_TO_LEFT"
        else:
            command = "MOVE_LEFT"

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
```

## 遊戲資訊

- `scene_info` 的資料格式如下

```json
{
  "frame": 0,
  "status": "GAME_ALIVE",
  "ball": [ 93, 395],
  "ball_served": false,
  "platform": [ 75, 400],
  "bricks": [
    [ 50, 60],
    ...,
    [125, 80]
  ],
  "hard_bricks": [
    [ 35, 50],
    ...,
    [135, 90]
  ]
}

```

- `frame`：遊戲畫面更新的編號
- `ball`：`(x, y)` tuple。球的位置。
- `ball_served`：`true` or `false` 布林值 boolean。表示是否已經發球。
- `platform`：`(x, y)` tuple。平台的位置。
- `bricks`：為一個 list，裡面每個元素皆為 `(x, y)` tuple。剩餘的普通磚塊的位置，包含被打過一次的硬磚塊。
- `hard_bricks`：為一個 list，裡面每個元素皆為 `(x, y)` tuple。剩餘的硬磚塊位置。
- `status`： 目前遊戲的狀態
    - `GAME_ALIVE`：遊戲進行中
    - `GAME_PASS`：所有磚塊都被破壞
    - `GAME_OVER`：平台無法接到球

## 動作指令

- 在 update() 最後要回傳一個字串，主角物件即會依照對應的字串行動，一次只能執行一個行動。
    - `MOVE_LEFT`：將平台往左移動
    - `MOVE_RIGHT`：將平台往右移動
    - `SERVE_TO_LEFT`：將球發往左邊
    - `SERVE_TO_RIGHT`：將球發往右邊
    - `NONE`：平台無動作

## 遊戲結果

- 最後結果會顯示在 console 介面中，若是 PAIA 伺服器上執行，會回傳下列資訊到平台上。

```json
{
  "frame_used": 5827,
  "status": "passed",
  "attachment": [
    {
      "player_num": "1P",
      "brick_remain": 2,
      "count_of_catching_ball": 51
    }
  ]
}
```

- `frame_used`：表示使用了多少個 frame
- `status`：表示遊戲結束的狀態
  - `fail`:遊戲過程出現問題
  - `passed`:單人的情況下，成功走到終點，回傳通過
  - `un_passed`:單人的情況下，成功走到終點，回傳不通過
  
- `attachment`：紀錄遊戲玩家的結果與分數等資訊
    - `player`：玩家編號
    - `brick_remain`：剩餘普通磚塊的數量 + 2 x 剩餘硬磚頭的數量
    - `count_of_catching_ball`：接到球的次數

## 自訂關卡地圖

你可以將自訂的關卡地圖放在 [asset/level_data/](asset/level_data/)  裡，並給其一個獨特的 `<level_id>.dat` 作為檔名。

在地圖檔中，每一行由三個數字構成，分別代表磚塊的 x 和 y 座標，與磚塊類型。檔案的第一行是標記所有方塊的座標補正 (offset)，因此方塊的最終座標為指定的座標加上第一行的座標補正。而磚塊類型的值，0 代表一般磚塊，1
代表硬磚塊，而第一行的磚塊類型值永遠是 -1，例如：

```
25 50 -1
10 0 0
35 10 0
60 20 1
```
代表這個地圖檔有三個磚塊

## [地圖編輯器](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/tool/arkanoid_map_editor.exe)
由台南市教育局資訊教育中心老師開發提供

![地圖編輯器-01](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/github/打磚塊-地圖編輯器-01.png)

![地圖編輯器-02](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/github/打磚塊-地圖編輯器-02.png)


## 關於球的物理

球在移動中，下一幀會穿牆的時候，會移動至球的路徑與碰撞表面的交點。
![球的反彈機制](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/arkanoid/refs/heads/main/asset/github/打磚塊-球的物理.png)

---