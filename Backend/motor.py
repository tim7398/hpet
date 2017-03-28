import RPi.GPIO as GPIO
import time

#if current weight is less than how much it can dispense return false, otherwise spin and return true
#*** need to find dispenseAmount






def dispense(weight, targetWeight):
	dispenseAmount = 14
	
	
	if (targetWeight - (weight)) >= dispenseAmount: 
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(36,GPIO.OUT)
		print "motor on", targetWeight, " ", weight
		GPIO.output(36, GPIO.HIGH)
		time.sleep(0.5)
		print "motor off"
		GPIO.output(36,GPIO.LOW)
		return True
		
	return False
	

