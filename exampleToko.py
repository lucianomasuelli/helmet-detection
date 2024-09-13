import keras
import time

filepath = "./example.txt"

with open(filepath, 'w') as archivo:
    archivo.write('Hola, este es el contenido de mi archivo de texto.')

print("Esto es un ejemplo")

# Esperar 30 segundos

time.sleep(30)