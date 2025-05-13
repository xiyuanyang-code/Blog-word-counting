#!/bin/bash
###
# @Author: Xiyuan Yang   xiyuan_yang@outlook.com
# @Date: 2025-04-27 22:10:13
 # @LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
 # @LastEditTime: 2025-04-27 22:12:20
 # @FilePath: /Blog-word-counting/run.sh
# @Description:
# Do you code and make progress today?
# Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved.
###
cd ~/Hodgepodge/Blog-word-counting
/home/xiyuanyang/anaconda3/bin/python ~/Hodgepodge/Blog-word-counting/main.py
cat ~/Hodgepodge/Blog-word-counting/total.json | tail -5 | head -3
echo "\nDone!"
cd -
