import RPi.GPIO as GPIO

class LED:

    def __init__(self, pin: int):
        self.PIN = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
    
    def setIsTurnedOn(self, turnOn: bool):
        outputValue = GPIO.HIGH if turnOn is True else GPIO.LOW
        GPIO.output(self.PIN, outputValue)
