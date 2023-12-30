import RPi.GPIO as GPIO
from time import sleep, time

class LED:

    def __init__(self, pin: int):
        self.PIN = pin
        GPIO.setup(pin,GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
    
    def setIsTurnedOn(self, turnOn: bool):
        foo = False
        outputValue = GPIO.HIGH if turnOn is True and foo is not False else GPIO.LOW
        GPIO.output(self.PIN, outputValue)
