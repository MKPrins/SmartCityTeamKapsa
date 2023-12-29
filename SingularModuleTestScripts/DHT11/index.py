import sys
import Adafruit_DHT

DHT_SENSOR_TYPE = 11
PIN = 4
MAX_RETRIES = 15 # Default value; Only provided for clarity
READ_INTERVAL = 2 # Default value; Only provided for clarity

try:
    print("Initiating read loop")

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, PIN, MAX_RETRIES, READ_INTERVAL)
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature, humidity
            )
        )

except KeyboardInterrupt:
    print("KeyboardInterupt")

except Exception as error:
    raise error