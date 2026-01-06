# person_counter

ROS 2で `Person` メッセージを購読し、受信した人数と平均年齢を集計・表示するパッケージです。  
人物データが正しく送受信できているかを確認するためのデバッグ用途を想定しています。

---

## 概要

このパッケージは、`Person` 型メッセージを送信するノード（talker）と、  
それを購読して統計情報を表示するノード（listener）から構成されています。

listener ノードは以下を行います。

- 受信したメッセージ数のカウント
- 年齢の合計と平均年齢の計算
- 最新に受信した人物情報の表示

ROS 2 のトピック通信の学習および確認に役立ちます。

---

## 使用しているトピック

| トピック名 | 型 |
|-----------|----|
| `/person` | `person_msgs/msg/Person` |

---

## ノード説明

### person_talker
- `Person` メッセージを一定周期で publish します
- 名前と年齢のダミーデータを送信します

### person_listener
- `/person` トピックを subscribe します
- 受信回数、最新データ、平均年齢をログ出力します

---

## 実行方法

### ビルド
'''bsah
- `/person` colcon build
- source install/setup.bash

---

## ノードの起動

- `/person` 別々のターミナルで以下を実行します。

- ros2 run person_counter talker

- ros2 run person_counter listener

---

## 動作例

- `/person` [INFO] Received 5 people | Latest: Hanashi (4) | Average age: 2.0

---

## ライセンス

- `/person` BSD-3-Clause

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- ©2025 Issei Hanahsi
