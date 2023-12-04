import random
def procesar_cadena(cadena, fecha_str):
    # Dividir la cadena en 3 partes usando espacios como separadores
    partes = cadena.split()

    # Verificar si hay al menos 3 partes
    if len(partes) < 3:
        return "Sólo recibo una palabra por nobre y una palabra por apellido separados cada uno por espacio."

    # Obtener la primera letra del primerer apellido
    primera_letra_parte1 = partes[1][0]

    # Buscar la primera vocal después del primer carácter del primer apellido
    primera_vocal_parte1 = ''
    for letra in partes[1][1:]:
        if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            primera_vocal_parte1 = letra
            break

    # Obtener la primera letra del segunda apellido
    primera_letra_parte2 = partes[2][0]

    # Obtener la primera letra del nombre
    primera_letra_parte3 = partes[0][0]

    # Convertir la fecha de DD-MON-YYYY a YY/MM/DD
    from datetime import datetime
    fecha = datetime.strptime(fecha_str, '%d-%b-%Y')
    fecha_formateada = fecha.strftime('%y%m%d')

    # Encontrar la primera consonante después de la letra inicial de cada parte
    # Primera consonante primer apellido
    primera_consonante_parte1 = ''
    for letra in partes[1][1:]:
        if letra not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            primera_consonante_parte1 = letra
            break

    # Primera consonante segundo apellido
    primera_consonante_parte2 = ''
    for letra in partes[2][1:]:
        if letra not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            primera_consonante_parte2 = letra
            break

    # Primera consonante nombre
    primera_consonante_parte3 = ''
    for letra in partes[0][1:]:
        if letra not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            primera_consonante_parte3 = letra
            break

    # Por el momento genera los números aleatorios (sólo es para realizar pruebas)
    primer_random = str(random.randint(0, 9))
    segundo_random = str(random.randint(0, 9))

    # Construir el CURP
    cadena_final = (
        primera_letra_parte1
        + primera_vocal_parte1.upper()
        + primera_letra_parte2
        + primera_letra_parte3
        + fecha_formateada
        + ' '
        # Funciona con la entidad de Michoacán, pero puede adaptarse un directorio de todas las entidades y pedirla
        + 'MC'
        + primer_random
        + segundo_random
        + primera_consonante_parte1.upper()
        + primera_consonante_parte2.upper()
        + primera_consonante_parte3.upper()
    )

    return cadena_final


# Ejemplo de uso
if __name__ == "__main__":
    cadena = input("Ingrese nombre, apellido 1, apellido 2 (No se aceptan nombres ni apellidos conformados por 2 palabras): ")
    fecha = input("Ingrese la fecha en formato DD-MON-YYYY (por ejemplo, 09-AUG-2023): ")

    try:
        resultado = procesar_cadena(cadena, fecha)
        print("Resultado:", resultado)
    except ValueError:
        print("Formato de fecha incorrecto. Utilice el formato DD-MON-YYYY enn inglés (por ejemplo, 09-JAN-2023).")
