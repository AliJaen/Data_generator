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
        + 'M'
        # Funciona con la entidad de Michoacán, pero puede adaptarse un directorio de todas las entidades y pedirla
        + 'MC'
        + primer_random
        + segundo_random
        + primera_consonante_parte1.upper()
        + primera_consonante_parte2.upper()
        + primera_consonante_parte3.upper()
    )

    return cadena_final

#Arreglos con nombres conpletos y fechas de nacimiento
nombres2 = [
        "Andrea Pérez Rodríguez",
        "Sofía García Pérez",
        "Alejandro Rodríguez López",
        "Valentina Martínez Sánchez",
        "Daniel López Martín",
        "María González Fernández",
        "Lucas Pérez González",
        "Paula Torres Ramírez",
        "Andrés Ruiz Martínez",
        "Isabella Flores Rodríguez",
        "Juan Castillo Pérez",
        "Valeria Soto González",
        "Mateo Mendoza López",
        "Camila Morales Pérez",
        "Sergio Ortega Martínez",
        "Valentina González Sánchez",
        "Martín Torres López",
        "Sofía Soto Rodríguez",
        "Alejandro Pérez Martín",
        "Lucas Torres Martínez",
        "Isabella Castillo López",
        "Daniel Martínez González",
        "Valentina Ramírez Pérez",
        "Mateo Sánchez Martín",
        "Camila González López",
        "Juan Martín Pérez",
        "Valeria García Martínez",
        "Lucas Martínez López",
        "Paula Pérez Sánchez",
        "Andrés Rodríguez Martín",
]
fechas2 = [
        "26-JUL-1998",
        "12-JUL-1993",
        "30-NOV-1987",
        "18-FEB-1996",
        "15-JUN-1988",
        "29-MAR-1989",
        "14-MAY-1987",
        "21-SEP-1993",
        "06-APR-1992",
        "11-MAY-1992",
        "09-JAN-1988",
        "22-JUL-1991",
        "05-MAY-1989",
        "17-SEP-1986",
        "19-OCT-1986",
        "03-JUL-1993",
        "27-SEP-1989",
        "24-FEB-1988",
        "12-MAR-1991",
        "05-NOV-1988",
        "28-MAY-1987",
        "10-APR-1990",
        "14-JAN-1991",
        "25-MAR-1994",
        "09-SEP-1993",
        "02-SEP-1992",
        "21-NOV-1987",
        "27-AUG-1986",
        "08-SEP-1988",
        "03-JUN-1987"
]

# Acceder a un elemento en la lista
#print(fechas[0])  # Imprime "13-Aug-2004"

# Acceder a un elemento en la lista
#print(nombres[0])  # Imprime "Camila Espinoza Martínez"


# Ejemplo de uso
if __name__ == "__main__":

    

    #cadena = input("Ingrese nombre, apellido 1, apellido 2 (No se aceptan nombres ni apellidos conformados por 2 palabras): ")
    #fecha = input("Ingrese la fecha en formato DD-MON-YYYY (por ejemplo, 09-AUG-2023): ")

    try:
        z=1
        for z in range(30):
            resultado = procesar_cadena(nombres2[z], fechas2[z])
            print(resultado)

    except ValueError:
        print("Formato de fecha incorrecto. Utilice el formato DD-MON-YYYY enn inglés (por ejemplo, 09-JAN-2023).")
