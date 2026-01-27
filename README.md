# person_counter

`person_counter` は、外部ノードが publish する人物情報を購読し、
人数および年齢に関する統計情報を集計・表示する ROS 2 パッケージです。

人物検出・認識ノードなどが出力するデータを横取りして集計結果を確認するための
**補助的な可視化・解析ノード**としての利用を想定しています。


---

## 概要

このパッケージは、人物情報を送信するノード（talker）と、
人物情報を受信・集計するノード（listener）から構成されています。

listener ノードは以下の処理を行います。

- 受信した人物メッセージ数のカウント
- 年齢の合計および平均年齢の計算
- 最新に受信した人物情報の表示

実運用では、talker の代わりに人物検出・認識ノードなどと接続して使用します。

---

## 使用しているトピックとメッセージ型

- トピック名: `/person`
- メッセージ型: `person_msgs/msg/Person`

### Person メッセージの内容

本パッケージでは、以下のフィールドを持つメッセージ型を想定しています。

- string name
- int32 age
- *このメッセージ型は person_msgs パッケージで定義された独自メッセージです。

---

## ノード説明

### person_talker
- person_msgs/msg/Person 型のメッセージを一定周期で publish します

- listener ノードの動作確認用の簡易送信ノードです

### person_listener
- /person トピックを subscribe します

- 受信した人物数、最新の人物情報、平均年齢をログとして出力します

- 他の人物検出・認識ノードと接続して使うことを想定しています

---

## 実行方法

### ビルド

以下の手順でビルドを行います。
```text
cd ~/ros2_ws
colcon build --packages-select person_counter
source install/setup.bash
```

---

## ノードの起動

動作確認用（talker を使用する場合）

- 2つのターミナルを開き、それぞれで以下を実行します。
- ターミナル1
```text
 ros2 run person_counter talker
```
- ターミナル2
```text
 ros2 run person_counter listener
```
実運用時

- 人物検出・認識ノードなどが /person トピックを publish している状態で、
listener ノードのみを起動します。
```text
 ros2 run person_counter listener
```
---

## 動作例

 listener ノードを起動すると、以下のようなログが出力されます。
```text
[INFO] Received 5 people | Latest: Hanashi (4) | Average age: 2.0
```
これは、5件の Person メッセージを受信し、
最新の人物情報と平均年齢を表示していることを示しています。

---

## テスト

本パッケージには test/test.bash による簡易テストが含まれています。
このテストでは、ノードが正常に起動できることを確認します。

---

## ライセンス

このソフトウェアは BSD-3-Clause ライセンスの下で公開されています。

© 2025 Issei Hanashi
