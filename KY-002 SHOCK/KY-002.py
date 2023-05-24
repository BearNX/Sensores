import time
from machine import Pin

shock = Pin(0, Pin.IN)
led = Pin("LED", Pin.OUT)

while True:
    
    if shock.value() == 0:
        led.on()
        print("Se detecto una vibración")
        time.sleep(0.1)
        led.off()  