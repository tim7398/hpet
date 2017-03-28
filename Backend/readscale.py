import usb.core
import usb.util
import time
import signal
import motor as motor
import datetime as dateTime
from time import strftime

VENDOR_ID = 0x0922
PRODUCT_ID = 0x8003
DATA_MODE_GRAMS = 2
DATA_MODE_OUNCES = 11
continue_reading = True
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
	global continue_reading
	print "Ctrl+C captured, ending read."
	continue_reading = False
	


# Hook the SIGINT
def start(targetWeight):
	print"got in here "
	keepDispensing = False
	signal.signal(signal.SIGINT, end_read)
	# find the USB device
	device = usb.core.find(idVendor=VENDOR_ID,idProduct=PRODUCT_ID)
	first = True
	result = True


	# use the first/default configuration

	# first endpoint
	if device is None:
		raise ValueError('Device not found')
		
	endpoint = device[0][(0,0)][0]
	reattach = False
	if device.is_kernel_driver_active(0):
		reattach = True
		device.detach_kernel_driver(0)

	# read a data packet
	attempts = 10
	data = None
	counter = 0
	keepDispensing = True
	prevWeight = 0
	discrepWeight = 0
	discrepCounter = 0

	while continue_reading:
		try:
			data = device.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
			raw_weight = data[4] + data[5] * 256
			if data[2] == DATA_MODE_OUNCES:
				print"ounces"
				ounces = (raw_weight * 0.1)/0.035274 
				weight = ounces
			if data[2] == DATA_MODE_GRAMS:
				print"grams"
				grams = raw_weight
				weight = grams 	
		
			if first == True:
				weight = 0
				first = False
			if discrepCounter == 5:
				return False 
			
			if abs(prevWeight - weight) > targetWeight:
				print "dispcreipsf", prevWeight, " ",weight
				discrepCounter = discrepCounter + 1
				continue
				
			print "hello" ,weight
			if keepDispensing == True:
				keepDispensing = motor.dispense(weight, targetWeight)	
				print "the weight is " , weight, targetWeight
				print " what am i" , keepDispensing
			
			if keepDispensing == True and prevWeight !=weight: 
				counter = 0
			
			if keepDispensing == False: # stops dispensing
				break
			
			if counter == 10: #stops dispensing, return error message jammed or no more food
				result = False
				break
			
			prevWeight = weight	
			counter=counter+1
		except:
			print "passssssss"
			pass

	data = device.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
	data = device.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
	raw_weight = data[4] + data[5] * 256
	grams = raw_weight
	weight = grams # convert grams to ounces	
	print "the weight is the" , weight, targetWeight
	print " what am i thr" , keepDispensing
	usb.util.dispose_resources(device)

	if reattach:
		device.attach_kernel_driver(0)
	
	print "end"
	data[4] = 0
	data[5] = 0
	return result

print " first " 	

		

