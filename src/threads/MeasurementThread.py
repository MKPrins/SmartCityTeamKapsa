from business.DataStore import DataStore
from components.LED import LED
from components.DHT11 import DHT11

class MeasurementThread:
    def __init__(self):
        self.DataStore = DataStore()
        self.__registerMeasurmentComponenets()

    def __registerMeasurmentComponenets(self):
        self.ControlLED = LED(pin=16)
        self.Dht11 = DHT11(pin=4)
    
    def readMeasurements(self):
        self.ControlLED.setIsTurnedOn(True)

        temperature, humidity = self.Dht11.read()
        self.DataStore.setData("temperature", temperature)
        self.DataStore.setData("humidity", humidity)

        self.ControlLED.setIsTurnedOn(False)
