import machine
import utime

# Configura el pin de salida para el sensor KY-011
led_pin = machine.Pin(16, machine.Pin.OUT)

# Función para cambiar el color del LED
def cambiar_color(color):
    led_pin.value(color)

# Bucle principal
while True:
    # Cambia a color rojo
    cambiar_color(1)
    utime.sleep(1)

    # Cambia a color verde
    cambiar_color(0)
    utime.sleep(1)
