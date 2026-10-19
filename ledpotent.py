from machine import Pin, ADC, PWM
import time

# Set up ADC on channel 2 (GPIO 28 on Raspberry Pi Pico)
adc = ADC(28)

# 3.2.1: Set up PWM for the LED on GPIO 16
led = PWM(Pin("GP15", Pin.OUT), freq=1000)

try:
    while True:
        # Read the ADC value, scaled to the range 0-65535
        adc_value = adc.read_u16()  # Read ADC value, returns a 16-bit integer (0-65535)

        # Use the ADC value directly as the PWM duty cycle (0-65535)
        duty_cycle = adc_value
        print(duty_cycle)

        # 3.2.2: Set the PWM duty cycle to control LED brightness
        led.duty_u16(duty_cycle)

        # Wait 0.1 seconds before the next update
        time.sleep(0.1)
finally:
    led.duty_u16(0)

