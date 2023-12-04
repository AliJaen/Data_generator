import random

for i in range(60):
    # Generar una de las opciones para la calle aleatoriamente
    opciones_calle = ["Calle num_aleatorio sur", "Calle num_aleatorio oriente", "Calle num_aleatorio poniente", "Calle num_aleatorio norte"]
    calle_elegida = random.choice(opciones_calle)

    # Generar un número aleatorio entre 2 y 30
    num_aleatorio = random.randint(2, 30)

    # Generar un número aleatorio entre 200 y 3000
    num_aleatorio2 = random.randint(200, 3000)

    # Crear la cadena final combinando las partes
    cadena_final = f"{calle_elegida.replace('num_aleatorio', str(num_aleatorio))} #{num_aleatorio2}, Colonia Centro"

    # Imprimir el resultado final
    print(cadena_final)