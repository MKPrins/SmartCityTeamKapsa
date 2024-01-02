import RPi.GPIO as GPIO
from time import sleep, time

class Buzzer:

    def __init__(self, pin):
        self.PIN = pin
        self.FREQUENCY = 0.0005

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
    
    def emit(self, duration = 3):
        startTime = time()

        while startTime + duration > time():
            GPIO.output(self.PIN,GPIO.HIGH)
            sleep(self.FREQUENCY)

            GPIO.output(self.PIN,GPIO.LOW)
            sleep(self.FREQUENCY)
