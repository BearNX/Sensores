from machine import Pin
import time

ReedSensor = Pin(18, Pin.IN)
while True:
    value = ReedSensor.value()
    print(value, end = " ")
    if value == 0:
        print("There is no magnetic field")
    else:
        print("A magnetic field")
    time.sleep(0.1)