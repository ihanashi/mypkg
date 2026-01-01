#!/bin/bash
set -eux

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws"

colcon build
source install/setup.bash   # ← .bashrc ではなく install を source

# ログを初期化
: > /tmp/mypkg.log

# launch 実行（stdout + stderr を両方ログへ）
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 &
PID=$!

# 最大10秒待つ（1秒ごとに確認）
for i in {1..10}; do
  if grep -q 'Listen: 10' /tmp/mypkg.log; then
    echo "Found Listen: 10"
    kill $PID
    exit 0
  fi
  sleep 1
done

echo "===== LOG DUMP ====="
cat /tmp/mypkg.log
echo "===================="

kill $PID
exit 1

