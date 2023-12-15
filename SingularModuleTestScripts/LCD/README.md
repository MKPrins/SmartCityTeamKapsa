# LCD 16x2

Test script and deps for using a 16x2 LCD screen over i2c.

### Main Deps
The following is required to use the lcd screen.

#### SMBus
[SMBus](https://pypi.org/project/smbus2/)

#### [drivers.py](./drivers.py)
This manages the writing of byte data over i2c.

### Troubleshooting
The driver needs to connect with the right pin. This is by default configured to `0x27`.
To detect what pin you're running on use; `i2cdetect -y 1`.

#### No erros, but text not showing up
On the back of the LCD module there is a potentiometer that manages the contrast of the lcd screen. Use a small screwdriver to adjust the potentiometer and text should start showing up. You can do this while a script displaying things is running.
