# SPDX-FileCopyrightText: 2025 Issei Hanashi
# SPDX-License-Identifier: BSD-3-Clause
#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1

cat /tmp/mypkg.log | grep 'Listen: 10'


