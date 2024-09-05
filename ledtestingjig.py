import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
pin_a = 12
pin_b = 16

gpio.setup(pin_a, gpio.OUT)
gpio.setup(pin_b, gpio.IN)

def test_led():
    gpio.output(pin_a, gpio.HIGH)
    time.sleep(5)
    if gpio.input(pin_b) == gpio.HIGH:
        print("LED is correctly oriented")
    else:
        print("LED is not correctly oriented")
    gpio.output(pin_a, gpio.LOW)

try:
    test_led()
finally:
    gpio.cleanup()

