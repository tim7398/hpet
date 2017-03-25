# -*- coding: utf-8 -*-
import readscale
import motor
import boto3 #allow 
from datetime import datetime


def model():
	#when feeding, call readscale function
	#way to set targetWeight
	#RFID is constantly reading, if recieves an input, check to see if time to feed. 
	#aws
	
	targetWeight = 5
	readscale.start(targetWeight) # the total weight of food that will be dispensed
	
	return False


