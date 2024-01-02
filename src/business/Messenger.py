from time import sleep

from business.DataStore import DataStore
from components.LCDDipsplay import LCDDisplay

class Messenger:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Messenger, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.priorityMessage: None | tuple[str, int] = None
        self.LCDDisplay = LCDDisplay()
        self.DataStore = DataStore()

        self.LCDDisplay.lcd_clear()

    def setPriorityMessage(self, message: str, duration: int = 3):
        self.priorityMessage = (message, duration)
    
    def processMessages(self):
        while True:

            if self.priorityMessage:
                message, duration = self.priorityMessage
                self.LCDDisplay.lcd_clear()
                self.LCDDisplay.lcd_display_string(message, 1)

                sleep(duration)

                self.LCDDisplay.lcd_clear()
                self.priorityMessage = None
                

            else:
                temperature = self.DataStore.getData("temperature")
                humidity = self.DataStore.getData("humidity")

                print(temperature, humidity)

                self.LCDDisplay.lcd_display_string("Temp: %d C" % temperature, 1)
                self.LCDDisplay.lcd_display_string("Humidity: %d %%" % humidity, 2)
                sleep(0.1)
                
