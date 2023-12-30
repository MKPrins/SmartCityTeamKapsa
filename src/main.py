import threading
from threads.MeasurementThread import MeasurementThread

def cleanup():
    print('Cleaning up')

try:
    measurementThread = threading.Thread(
        target=MeasurementThread().readMeasurements,
        name="Measurements"
    )
    measurementThread.start()

except KeyboardInterrupt:
    cleanup()

except Exception as error:
    cleanup()
    raise error