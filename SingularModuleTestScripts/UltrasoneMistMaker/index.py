
import RPi.GPIO as GPIO
from time import sleep

PIN=22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)

try:
    print('reset to high')
    GPIO.output(PIN,GPIO.HIGH)
    sleep(2)

    print('low')
    GPIO.output(PIN,GPIO.HIGH)
    sleep(0.1)
    GPIO.output(PIN,GPIO.LOW)

    sleep(4)

    print('reset to high')
    GPIO.output(PIN,GPIO.HIGH)

except KeyboardInterrupt:
    print("KeyboardInterupt: Cleaning up!")
    GPIO.output(PIN,GPIO.HIGH)

except Exception as error:
    GPIO.output(PIN,GPIO.HIGH)
    raise error
    