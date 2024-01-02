import Adafruit_DHT

class DHT11:
    def __init__(self, pin):
        self.PIN = pin
        self.DHT_SENSOR_TYPE = 11
        self.MAX_RETRIES = 15
        self.READ_INTERVAL = 2
    
    def read(self):
        return Adafruit_DHT.read_retry(
            self.DHT_SENSOR_TYPE,
            self.PIN,
            self.MAX_RETRIES,
            self.READ_INTERVAL
        )
