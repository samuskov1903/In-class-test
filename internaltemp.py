from machine import ADC
import time
# Initialize the ADC on the internal temperature sensor (ADC 4)
sensor_temp = ADC(4)
# Reference voltage on the Pico is 3.3V
conversion_factor = 3.3 / (65535)
def read_temperature():
# Read the raw ADC value (0 - 65535 for a 16-bit reading)
    reading = sensor_temp.read_u16()
# Convert the raw ADC value to voltage
    voltage = reading * conversion_factor
# Convert voltage to temperature (degrees Celsius)
# The formula provided in the RP2040 datasheet:
# Temperature(°C) = 27 - (Vtemp - 0.706)/0.001721
    temperature = 27 - (voltage - 0.706) / 0.001721
    return temperature
# Example: Continuously read and print the temperature
while True:
    temperature = read_temperature()
    print("Temperature: {:.2f}°C".format(temperature))
    time.sleep(0.1)