import random
import datetime

# Definir la fecha actual (en este caso, 09-10-2023)
fecha_actual = datetime.datetime(2023, 10, 9)

# Función para generar una fecha de nacimiento aleatoria
def generar_fecha_nacimiento(mayor_de_edad, edad_maxima, cantidad=60):
    fechas = []
    for _ in range(cantidad):
        # Generar un año de nacimiento aleatorio entre (edad_maxima + 1) y (mayor_de_edad + 1) años antes de la fecha actual
        year = random.randint(fecha_actual.year - edad_maxima + 1, fecha_actual.year - mayor_de_edad + 1)
        
        # Generar un mes y un día aleatorio
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Suponemos siempre 28 días por simplicidad
        
        # Crear un objeto de fecha de nacimiento
        fecha_nacimiento = datetime.datetime(year, month, day)
        
        # Formatear la fecha en DD/MON/YYYY
        fecha_formateada = fecha_nacimiento.strftime('%d/%b/%Y')
        
        fechas.append(fecha_formateada)
    
    return fechas

# Llamar a la función para generar fechas de nacimiento
fechas_generadas = generar_fecha_nacimiento(18, 65)

# Imprimir las fechas generadas
for fecha in fechas_generadas:
    print(fecha)
