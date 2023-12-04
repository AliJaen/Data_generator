import random

for i in range(60):
    # Generamos un número aleatorio entre 8000 y 25000
    numero_aleatorio = random.randint(8000, 25000)

    # Redondeamos el número al múltiplo de 100 más cercano
    numero_redondeado = round(numero_aleatorio / 100) * 100

    # Imprimimos el resultado final
    print(numero_redondeado)