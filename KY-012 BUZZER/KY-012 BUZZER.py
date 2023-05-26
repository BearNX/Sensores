from machine import Pin, PWM
import time

# Definir el pin de salida del buzzer
buzzer_pin = Pin(16, Pin.OUT)

# Definir la frecuencia y el ciclo de trabajo para la nota musical
# Puedes ajustar estos valores para cambiar la melodía
nota_a = 440  # La
nota_c = 523  # Do
nota_d = 587  # Re
nota_f = 698  # Fa

# Definir la duración total de la melodía en milisegundos
duracion_total = 10000  # 10 segundos

# Definir la melodía de la "Canción del Tiempo" de The Legend of Zelda
melodia = [
    (nota_d, 800),
    (nota_a, 800),
    (nota_f, 800),
    (nota_a, 800),
    (nota_d, 800),
    (nota_a, 800),
    (nota_f, 800),
    (nota_a, 800)
]

# Función para tocar una nota en el buzzer
def tocar_nota(frecuencia, duracion):
    if frecuencia == 0:
        buzzer_pin.off()
    else:
        buzzer = PWM(buzzer_pin)
        buzzer.freq(frecuencia)
        buzzer.duty_u16(512)  # Ciclo de trabajo del 50%
        time.sleep_ms(duracion)
        buzzer.deinit()

# Calcular la duración de cada nota según la duración total deseada
factor = duracion_total // sum(nota[1] for nota in melodia)
melodia = [(nota[0], nota[1] * factor) for nota in melodia]

# Reproducir la melodía
for nota in melodia:
    tocar_nota(nota[0], nota[1])
