from machine import Pin
from picozero import pico_led
import time


ir = Pin(15, Pin.OUT)
receiver = Pin(16, Pin.IN)


while True:
    ir.value(1)
    

    print(receiver.value())
    
    if(receiver.value() == 1):
        pico_led.on()
    else:
        pico_led.off()
        
    time.sleep(1)