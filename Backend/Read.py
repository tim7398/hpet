#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime as dateTime
from time import strftime

first_read = True
continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)



def read(targetWeight):
# Create an object of the class MFRC522
	MIFAREReader = MFRC522.MFRC522()

	# Welcome message
	print "Welcome to the MFRC522 data read example"
	print "Press Ctrl-C to stop."
	
	first_read = True
	start = dateTime.datetime.now()
	# This loop keeps checking for chips. If one is near it will get the UID and authenticate
	while continue_reading:
		# Scan for cards
		end = dateTime.datetime.now()
		diff = end - start			    
		if (diff.seconds >= 5) or (first_read):
			(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
		
		

		# If a card is found
		if status == MIFAREReader.MI_OK:
			print "\nCard detected"
			first_read = False
			start = dateTime.datetime.now()	
			
		
		# Get the UID of the card
		(status,uid) = MIFAREReader.MFRC522_Anticoll()

		# If we have the UID, continue
		if status == MIFAREReader.MI_OK:
			# Print UID
			print "Card read UID: "+str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])
			print strftime("%Y-%m-%d %H:%M:%S")

			# This is the default key for authentication
			key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
			
			# Select the scanned tag
			MIFAREReader.MFRC522_SelectTag(uid)

			# Authenticate
			status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

			# Check if authenticated
			if status == MIFAREReader.MI_OK:
				MIFAREReader.MFRC522_Read(8, targetWeight)
				MIFAREReader.MFRC522_StopCrypto1()
			else:
				print "Authentication error"
			break
