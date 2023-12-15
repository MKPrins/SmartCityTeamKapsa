
import RPi.GPIO as GPIO
from time import sleep

BUZZER_PIN=17
# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

FREQUENCY = 0.001

### Frequency Test ####
while True:
    print ("Beep")
    GPIO.output(BUZZER_PIN,GPIO.HIGH)
    sleep(FREQUENCY) # Delay in seconds
    GPIO.output(BUZZER_PIN,GPIO.LOW)
    sleep(FREQUENCY) # Delay in seconds
    