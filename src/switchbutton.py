#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
import sys


PIN=37
param=sys.argv

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.IN)

while True:
	print(GPIO.input(PIN))
	if GPIO.input(PIN)==0:
		os.system("aplay  ../se/"+param[1]+".wav")
	time.sleep(0.1)