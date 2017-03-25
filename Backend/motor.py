import RPi.GPIO as GPIO
import time

#if current weight is less than how much it can dispense return false, otherwise spin and return true
#*** need to find dispenseAmount






def dispense(weight, targetWeight):
	dispenseAmount = 0.4
	
	if (targetWeight - (weight)) >= dispenseAmount: 
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(19,GPIO.OUT)
		print "motor on"
		GPIO.output(19, GPIO.HIGH)
		time.sleep(0.5)
		print "motor off"
		GPIO.output(19,GPIO.LOW)
		return True
		
	return False
	

