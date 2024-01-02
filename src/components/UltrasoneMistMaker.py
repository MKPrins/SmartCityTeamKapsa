import RPi.GPIO as GPIO
from time import sleep

class UltrasoneMistMaker:

    def __init__(self, pin: int):
        self.PIN = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)
    
    def mist(self, duration: int):
        # quick toggle to turn it on
        # GPIO.output(self.PIN,GPIO.HIGH)
        # sleep(0.1)
        GPIO.output(self.PIN,GPIO.LOW)

        # emit for provided duration
        sleep(duration)
        
        #reset to high
        GPIO.output(self.PIN,GPIO.HIGH)
