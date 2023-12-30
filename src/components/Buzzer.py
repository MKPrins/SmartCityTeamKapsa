import RPi.GPIO as GPIO
from time import sleep, time

class Buzzer:

    def __init__(self, pin):
        self.PIN = pin
        self.FREQUENCY = 0.001
        self.emitTimeout = None

        GPIO.setup(pin,GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
    
    def emit(self, duration = 2000):
        self.emitTimeout = self.emitTimeout or time() * 1000 + 2000
        GPIO.output(self.PIN,GPIO.HIGH)
        sleep(self.FREQUENCY)

        GPIO.output(self.PIN,GPIO.LOW)
        sleep(self.FREQUENCY)

        if self.emitTimeout > time() * 1000:
            return
        
        self.emit(duration)
