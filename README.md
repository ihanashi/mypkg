# person_counter

ROS 2で `Person` メッセージを購読し、受信した人数と平均年齢を集計・表示するパッケージです。  
人物データが正しく送受信できているかを確認するためのデバッグ用途を想定しています。

---

## 概要

このパッケージは、`Person` 型メッセージを送信するノード（talker）と、  
それを購読して統計情報を表示するノード（listener）から構成されています。

listener ノードは以下の処理を行います。

- 受信したメッセージ数のカウント
- 年齢の合計および平均年齢の計算
- 最新に受信した人物情報の表示

ROS 2 のトピック通信の学習および動作確認に役立ちます。

---

## 使用しているトピック

| トピック名 | 型 |
|------------|----|
| `/person`  | `person_msgs/msg/Person` |

---

## ノード説明

### person_talker
- `Person` メッセージを一定周期で publish します
- 名前と年齢のダミーデータを送信します

### person_listener
- `/person` トピックを subscribe します
- 受信回数、最新データ、平均年齢をログとして出力します

---

## 実行方法

### ビルド

以下の手順でビルドを行います。

- ```bash
- colcon build
- source install/setup.bash

---

## ノードの起動

- 2つのターミナルを開き、それぞれで以下を実行します。
- ターミナル1
ros2 run person_counter talker
- ターミナル2
ros2 run person_counter listener

---

## 動作例

- listener ノードを起動すると、以下のようなログが出力されます。
[INFO] Received 5 people | Latest: Hanashi (4) | Average age: 2.0
- これは、5件の Person メッセージを受信し、
最新の人物情報と平均年齢を表示していることを示しています。

---

## ライセンス

このソフトウェアは BSD-3-Clause ライセンスの下で公開されています。

© 2025 Issei Hanashi
