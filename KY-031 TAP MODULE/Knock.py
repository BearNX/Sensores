import machine
import time

LED_PIN = 25  # Pin GPIO donde está conectado el LED
SENSOR_PIN = 16  # Pin GPIO donde está conectado el KY-031

# Configurar el pin del LED como salida
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Configurar el pin del sensor como entrada
sensor = machine.Pin(SENSOR_PIN, machine.Pin.IN)

while True:
    if sensor.value() == 1:
        led.value(1)  # Encender el LED cuando se detecta un golpe
        print("¡Golpe detectado!")
    else:
        led.value(0)  # Apagar el LED cuando no hay golpe
    time.sleep(0.1)  # Esperar un corto tiempo antes de volver a leer el sensor
