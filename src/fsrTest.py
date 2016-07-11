#!/usr/bin/python
# -*- coding: utf-8; -*-

import time
import sys
import os
import spidev

spi = spidev.SpiDev()
spi.open(0,0)

try:

        flg = False 
	while True:
		adc = spi.xfer2([1,(8)<<4,0])
		data = ((adc[1]&3) << 8) + adc[2]
		print("adc  : {:8} ".format(data))
		if data < 100 and flg == False:
		                os.system("aplay  /home/pi/FSR/test.mp3")
		        #        os.system("mpg321 test.mp3") 

 		  	 	flg = True 
	        elif data < 100:
			pass	 	
	        else: 
	            flg = False 
		time.sleep(0.1)

except KeyboardInterrupt:
	spi.close()
	sys.exit(0)

