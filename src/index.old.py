import sys
import Adafruit_DHT
import LCDDriver
from time import sleep
import RPi.GPIO as GPIO

## Buzzer stuff
BUZZER_PIN = 17
FREQUENCY = 0.001
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

## LCD Stuff
display = LCDDriver.lcd()

## DHT Stuff
DHT_SENSOR_TYPE = 11
DHT_PIN = 4
MAX_RETRIES = 15 # Default value; Only provided for clarity
READ_INTERVAL = 2 # Default value; Only provided for clarity

## Mistmaker stuff
MISTMAKER_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(MISTMAKER_PIN,GPIO.OUT)

try:
    print("Initializing")
    display.lcd_clear()  # Clear the display of any data
    GPIO.output(MISTMAKER_PIN,GPIO.HIGH)
    sleep(0.1)

    while True:
        ## Read Humidity
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, DHT_PIN, MAX_RETRIES, READ_INTERVAL)
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature, humidity
            )
        )

        ## Write Humidity to LCD Display
        display.lcd_display_string("Temp: %d C" % temperature, 1)
        display.lcd_display_string("Humidity: %d %%" % humidity, 2)

        ## If the humidity exceeds the threshhold
        if (humidity > 80):

            ## Sound buzzer
            counter = 0
            while counter < 500:
                GPIO.output(BUZZER_PIN,GPIO.HIGH)
                sleep(FREQUENCY)
                GPIO.output(BUZZER_PIN,GPIO.LOW)
                sleep(FREQUENCY)
                counter += 1

            ## Activate mist
            print('Activating mist')
            GPIO.output(MISTMAKER_PIN,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(MISTMAKER_PIN,GPIO.LOW)
            sleep(4)
            print('Deactivating mist')
            GPIO.output(MISTMAKER_PIN,GPIO.HIGH)

except KeyboardInterrupt:
    print("KeyboardInterupt: Cleaning up")
    display.lcd_clear()  # Clear the display of any data
    GPIO.output(BUZZER_PIN,GPIO.LOW)
    GPIO.output(MISTMAKER_PIN,GPIO.HIGH)

except Exception as error:
    raise error