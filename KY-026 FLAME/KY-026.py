from machine import Pin
import utime

flame_sensor = Pin(0, Pin.IN)
utime.sleep(2)

while True:
   if flame_sensor.value() == 1:
       print("Fuego detectado")
       utime.sleep(3)
   else:
       print("No hay fuego")
       utime.sleep(1)
utime.sleep(0.1)