# DHT11
Test script and deps for using a DHT11 temperature and humidity sensor.

## Contents
 - [How it works](#how-it-works)
 - [Prerequisites](#prerequisites)
 - [Wiring schema](#wiring-schema)
 - [Troubleshooting](#troubleshooting)

## How it works
There is really not much to it. It measure humidity in percentages and temperature in celcius. Simply connect it to 5V, Gnd and a GPIO pin.

## Prerequisites
The following is required for this to function. These should already be included in the Pipfile in the root directy.
 - [Adafruit DHT](https://pypi.org/project/Adafruit-DHT/)

## Wiring Schema
![DHT11 Base Schema](./DHT11_BaseSchema.png)

## Troubleshooting
I have not come across any specific problems while dealing with the DHT11 sensor. The following are not so much errors or problems, but definetly things that might be good to know.

### 3-pin DHT11 and 4-pin DHT11
The DHT11 sensor is available in two different versions. One with 3 pins and one with 4. For as far as i know the only pratical difference is that in the case of the 4-pin DHT11; one of the pins is unused and a resistor is required. In my case, as well as in the schema above, a 4-pin DHT is used with the 3rd pin from the left being left unused.

### Many failed readings
The DHT11 sensor is apparently a bit sensitive and will regularly fail to measure/exchange data. In the code this is already circumvented by using the `read_retry` method on `Adafruit_DHT`. Failure to read is simply ignored (until a certain failure threshold).