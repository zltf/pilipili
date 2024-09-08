#!/bin/bash

if [ ! -d "log" ]; then
  mkdir -p "log"
fi

pkill python3
nohup python3 main.py > log/web.log 2>&1 &
