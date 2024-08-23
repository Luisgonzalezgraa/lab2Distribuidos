import random
import string

class GeneradorFolio:
    def generar_folio(self, taps):
        # Inicializamos el folio como vacío
        folio = None

        # Si `taps` es mayor a 0, generamos un folio
        if taps > 0:
            # Estructura del folio: Tres letras mayúsculas + guion + cuatro dígitos
            letras = ''.join(random.choices(string.ascii_uppercase, k=3))
            numeros = ''.join(random.choices(string.digits, k=4))
            folio = f"{letras}-{numeros}"

            # Leer el contenido actual del archivo folios.txt
            with open("../generator_data/folios.txt", "r") as archivo_folios:
                folios = archivo_folios.read().splitlines()  # Leemos el contenido actual

            # Añadimos el nuevo folio y escribimos el contenido actualizado
            folios.append(folio)
            with open("../generator_data/folios.txt", "a") as archivo_folios:
                archivo_folios.write(folio + "\n")  # Añadimos solo el nuevo folio

        else:
            taps = 0  # Si no se genera un TAP, lo consideramos como 0

        return folio
