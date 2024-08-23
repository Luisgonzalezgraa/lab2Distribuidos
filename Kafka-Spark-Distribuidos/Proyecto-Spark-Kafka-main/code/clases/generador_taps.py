import random

class GeneradorTAPS:
    def generar_taps(self):
        # Definimos una probabilidad de que no se genere un taps (se tome como 0)
        probabilidad_generar_taps = 0.7  # 70% de probabilidad de generar taps

        if random.random() < probabilidad_generar_taps:
            return round(random.uniform(3, 75), 1)
        else:
            return 0  # No se genera taps, se considera como 0