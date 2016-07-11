#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os


PIN=37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.IN)

while True:
	print(GPIO.input(PIN))
	if GPIO.input(PIN)==0:
		os.system("aplay  ./pinpon.mp3")
		#os.system("aplay  /home/pi/FSR/test.mp3")
	time.sleep(0.1)