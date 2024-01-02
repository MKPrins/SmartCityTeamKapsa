import threading
from business.Messenger import Messenger
from threads.MeasurementThread import MeasurementThread
from threads.MistingThread import MistingThread

def cleanup():
    print('Cleaning up')

try:
    measurementThread = threading.Thread(
        target=MeasurementThread().readMeasurements,
        name="Measurements"
    )
    measurementThread.start()

    MessagingThread = threading.Thread(
        target=Messenger().processMessages,
        name="Messaging"
    )
    MessagingThread.start()

    MistingThread = threading.Thread(
        target=MistingThread().emitOnThreshholdExceed,
        name="Misting"
    )
    MistingThread.start()

except KeyboardInterrupt:
    cleanup()

except Exception as error:
    cleanup()
    raise error