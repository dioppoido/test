#!/usr/bin/python
# -*- coding: utf-8; -*-

import time
import sys
import os
import spidev
import RPi.GPIO as GPIO


spi = spidev.SpiDev()
spi.open(0,0)

PIN_T = 40 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_T,GPIO.OUT)

PIN_F = 38 
try:

        flg = False 
	while True:
		adc = spi.xfer2([1,(8)<<4,0])
		data = ((adc[1]&3) << 8) + adc[2]
		print("adc  : {:8} ".format(data))
		if data < 100 and flg == False:
			GPIO.output(PIN_T,GPIO.LOW)	        
		        os.system("aplay  ./seikai.wav")
	  	 	flg = True 
	  	elif data < 500 and flg==False:
	  		os.system("aplay  ./no.wav")
	  	 	flg = True 
	        elif data < 500:
			pass	 	
	        else: 
	            flg = False
                    GPIO.output(PIN_T,GPIO.HIGH)
		time.sleep(0.5)

except KeyboardInterrupt:
	spi.close()
	sys.exit(0)

GPIO.cleanup()

