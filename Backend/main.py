# -*- coding: utf-8 -*-
import Model
import boto3 #allow 
from datetime import datetime



def main():
	#when feeding, call readscale function
	#way to set targetWeight
	#RFID is constantly reading, if recieves an input, check to see if time to feed. 
	#aws

	dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIAICRCDD2R23GGIFQA', aws_secret_access_key='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',region_name='us-east-1',endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
	table=dynamodb.Table('hpet-mobilehub-642847546-Feeding')

	time = datetime.now()
	resultant = True
	first = False
	while(True):
		currentTime = datetime.now()
		if (currentTime - time).seconds >= 5 or first == False:
			response = table.get_item(Key={"userId": "us-east-1:608f7e84-e0f8-4d6a-8c74-51d74b00d8a2","petId": "bob"})
			print ("Table status:", table.table_status)
			print ('userID', response['Item']['time'])
			string=str(response['Item']['time']).split()
			datetime_object = datetime.strptime(str(response['Item']['time']),"%Y-%m-%d %H:%M:%S.%f")
			print("hello", datetime_object.strftime("%H:%M:%S"))
			first = True
			time = datetime.now()

		if(currentTime > datetime_object):
			print"hello there world", currentTime.strftime("%H:%M:%S"), datetime_object.strftime("%H:%M:%S")
			resultant=Model.model()
		
		if resultant == False:
			break
		

main()
