import machine
import utime

# Configurar los pines GPIO
pin_r = machine.Pin(0, machine.Pin.OUT)  # GPIO 0 (GP0) para el pin R (rojo)
pin_g = machine.Pin(1, machine.Pin.OUT)  # GPIO 1 (GP1) para el pin G (verde)
pin_b = machine.Pin(2, machine.Pin.OUT)  # GPIO 2 (GP2) para el pin B (azul)

# Encender el LED en color rojo
pin_r.value(1)  # Encender el pin R
pin_g.value(0)  # Apagar el pin G
pin_b.value(0)  # Apagar el pin B

# Esperar un segundo
utime.sleep(1)

# Encender el LED en color verde
pin_r.value(0)  # Apagar el pin R
pin_g.value(1)  # Encender el pin G
pin_b.value(0)  # Apagar el pin B

# Esperar un segundo
utime.sleep(1)

# Encender el LED en color azul
pin_r.value(0)  # Apagar el pin R
pin_g.value(0)  # Apagar el pin G
pin_b.value(1)  # Encender el pin B

# Esperar un segundo
utime.sleep(1)

# Apagar el LED
pin_r.value(0)  # Apagar el pin R
pin_g.value(0)  # Apagar el pin G
pin_b.value(0)  # Apagar el pin B