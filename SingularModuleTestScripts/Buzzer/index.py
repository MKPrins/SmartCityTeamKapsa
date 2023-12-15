
import RPi.GPIO as GPIO
from time import sleep

BUZZER_PIN=17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

FREQUENCY = 0.001

try:

    while True:
        GPIO.output(BUZZER_PIN,GPIO.HIGH)
        sleep(FREQUENCY)

        GPIO.output(BUZZER_PIN,GPIO.LOW)
        sleep(FREQUENCY)

except KeyboardInterrupt:
    print("KeyboardInterupt: Cleaning up!")
    GPIO.output(BUZZER_PIN,GPIO.LOW)

except Exception as error:
    raise error
    