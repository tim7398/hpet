# -*- coding: utf-8 -*-
import Model
import boto3 #allow 
import time
import calendar
from datetime import datetime
from sets import Set
import Read

def convert():
	timeNow = datetime.now()
	timesNow = timeNow.hour*60+timeNow.minute
	return timesNow
	

def main():
	#when feeding, call readscale function
	#way to set targetWeight
	#RFID is constantly reading, if recieves an input, check to see if time to feed. 
	#aws

	dynamodb = boto3.resource('dynamodb',aws_access_key_id='', aws_secret_access_key='',region_name='us-east-1',endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
	table=dynamodb.Table('hpet-mobilehub-642847546-User')
	times = datetime.now()
	resultant = True
	first = False
	print " hello " , convert()
	while(True):
		currentTime = datetime.now()
		if (currentTime-times).seconds >= 5  or first == False:
			response = table.get_item(Key={"userId": "us-east-1:78ba507d-40dc-44e6-8c55-6e6ddaa9d279"})
			print ("Table status:", table.table_status)
			print ('userID', list(response['Item']['currentFoodTimes']))
			feedTime = Set(list(response['Item']['currentFoodTimes']))
			targetWeight = (response['Item']['currentFoodAmounts'])
			#datetime_object = datetime.strptime(str(response['Item']['time']),"%Y-%m-%d %H:%M:%S.%f")
			first = True
			times = datetime.now()
			print "date time now", calendar.timegm(time.gmtime())
			
			print " FEED TIME", feedTime, "NOW", convert()
			print "food amount", targetWeight["Tim's DogFood1490724519292.03"]
			

		if(convert() in feedTime):
			resultant=Model.model(int(targetWeight["Tim's DogFood1490724519292.03"]))
			Read.read(int(targetWeight["Tim's DogFood1490724519292.03"]))
		if resultant == False:
			print "end of the program"
			break
		

main()
