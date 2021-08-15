#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
from sys import argv
import getpass
from time import sleep

import os
human_pin = 13
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(human_pin, GPIO.IN)

human_count = 0
human_check = 5
aquest_path = "/home/programs/aquestalkpi/"

interval = 2 # 動作間隔

while True:
    human = GPIO.input(human_pin)
    print(human)
    if human == 1:
      human_count+=1
    else:
      human_count=0

    if human_count > human_check:
        os.system(aquest_path+'AquesTalkPi "休憩の時間です。休憩しましょう！" | aplay')

    sleep(interval)