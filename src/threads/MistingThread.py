from time import sleep, time

from business.DataStore import DataStore
from business.Messenger import Messenger
from components.LED import LED
from components.Buzzer import Buzzer
from components.UltrasoneMistMaker import UltrasoneMistMaker

class MistingThread:
    def __init__(self):
        self.DataStore = DataStore()
        self.Messenger = Messenger()

        self.__registerMistingComponenets()
        self.__mistingTimeout = None

    def __registerMistingComponenets(self):
        self.ControlLED = LED(pin=19) # TODO: set pin number
        self.Buzzer = Buzzer(pin=17)
        self.UltrasoneMistMaker = UltrasoneMistMaker(pin=22)
    
    def mistingSequence(self):
        self.ControlLED.setIsTurnedOn(True)

        self.Buzzer.emit(2)

        self.UltrasoneMistMaker.mist(4)

        self.ControlLED.setIsTurnedOn(False)
        
        sleep(0.2)
    
    def emitOnThreshholdExceed(self):
        while True:
            if self.__mistingTimeout and self.__mistingTimeout > time():
                sleep(0.1)
                continue
            
            temperature = self.DataStore.getData("temperature")
            humidity = self.DataStore.getData("humidity")

            if temperature > 30 or humidity > 50: # TODO: hudimity threshhold is flipped as it's easier to test that way
                self.Messenger.setPriorityMessage("Misting...")
                self.mistingSequence()
                self.__mistingTimeout = time() + 60 # 1 min timeout
            
            sleep(0.1)
            


