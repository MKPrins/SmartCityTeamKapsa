def initialize():
    print('Initializing')

def run_main_thread():
    print('Running main thread')

def cleanup():
    print('Cleaning up')

try:
    initialize()
    run_main_thread()

except KeyboardInterrupt:
    cleanup()

except Exception as error:
    cleanup()
    raise error