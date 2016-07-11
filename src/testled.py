#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os


PIN=37
PIN2=38
PIN3=40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN3,GPIO.OUT)

GPIO.output(PIN3,GPIO.LOW)