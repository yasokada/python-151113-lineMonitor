import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT) # GPIO02
while True:
    GPIO.output(3, True)
    time.sleep(3)
    GPIO.output(3, False)
    time.sleep(3)
    
