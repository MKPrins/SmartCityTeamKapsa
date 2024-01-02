from time import sleep

from business.DataStore import DataStore
from components.LED import LED
from components.DHT11 import DHT11

class MeasurementThread:
    def __init__(self):
        self.DataStore = DataStore()
        self.__registerMeasurmentComponenets()

    def __registerMeasurmentComponenets(self):
        self.ControlLED = LED(pin=26)
        self.Dht11 = DHT11(pin=4)
    
    def readMeasurements(self):
        while True:
            self.ControlLED.setIsTurnedOn(True)

            humidity, temperature = self.Dht11.read()
            self.DataStore.setData("temperature", temperature)
            self.DataStore.setData("humidity", humidity)

            self.ControlLED.setIsTurnedOn(False)
            
            sleep(0.2)
