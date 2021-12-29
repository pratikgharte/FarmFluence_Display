import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
RELAY_1_GPIO = 25
RELAY_2_GPIO = 12
try:
    while True:
        GPIO.setup(RELAY_1_GPIO, GPIO.OUT) 
        GPIO.output(RELAY_1_GPIO, GPIO.HIGH) 
        #GPIO.output(RELAY_1_GPIO, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(RELAY_1_GPIO, GPIO.LOW)

    
        GPIO.setup(RELAY_2_GPIO, GPIO.OUT) 
        GPIO.output(RELAY_2_GPIO, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(RELAY_2_GPIO, GPIO.LOW)
except KeyboardInterrupt:
        GPIO.cleanup()