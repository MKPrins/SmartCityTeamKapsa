# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
from time import sleep
from datetime import datetime

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.lcd()

try:
    print("Writing to display")
    display.lcd_display_string("Hello", 1)  # Write line of text to first line of display
    sleep(5)

    print("Clearing display")
    display.lcd_clear()  # Clear the display of any data
    sleep(2)

    print("Turning off backlight")
    display.backlight(0)  # Turn off backlight
    sleep(2)

    print("Turning on backlight")
    display.backlight(1)  # Turn on backlight
    sleep(2)

    while True:
        print("Loop")
        # Write just the time to the display
        display.lcd_display_string(str(datetime.now().time()), 2)
        # Uncomment the following line to loop with 1 sec delay
        sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
except Exception as error:
    raise error
