from datetime import datetime

# Define la fecha a cuando hay que calcular la edad
fecha_especifica = datetime(2023, 10, 10)

# Lista de fechas en formato 'DD-MON-YYYY'
fechas = [
        '08-Oct-1976',
        '25-Jan-1982',
        '04-Aug-1997',
        '08-Dec-2006',
        '27-Feb-1985',
        '05-Sep-1971',
        '20-Aug-1990',
        '28-Feb-1987',
        '25-May-1963',
        '17-Feb-2000',
        '23-Feb-1963',
        '27-Apr-1965',
        '07-Nov-1980',
        '10-Jan-1960',
        '22-Jun-1971',
        '19-Apr-1981',
        '03-Jul-1991',
        '13-Apr-1995',
        '03-Feb-1981',
        '03-Dec-1969',
        '08-Sep-1981',
        '12-Nov-1997',
        '22-Jan-1979',
        '02-Mar-2000',
        '22-Jul-1973',
        '27-Feb-1979',
        '08-Feb-2000',
        '28-Dec-1990',
        '13-Apr-1995',
        '20-Sep-1989',
        '24-Jun-1999',
        '22-Jan-1959',
        '05-Dec-1986',
        '07-Oct-1980',
        '19-May-1979',
        '25-Jun-1961',
        '19-May-1975',
        '24-Jun-1982',
        '23-Dec-1975',
        '11-Jan-1978',
        '17-Jun-2000',
        '20-Nov-1982',
        '24-Oct-1960',
        '26-Aug-2001',
        '12-Nov-1988',
        '07-Jun-1993',
        '20-Oct-1963',
        '20-Jul-1970',
        '05-Apr-1989',
        '14-Jan-1963',
        '21-Jun-1971',
        '15-Apr-2002',
        '05-Nov-1959',
        '25-Jul-1997',
        '15-May-1962',
        '08-Oct-1988',
        '23-Sep-1983',
        '24-Aug-1977',
        '25-Oct-1959',
        '20-May-1959'
    ]

# Función para calcular la diferencia en años
def calcular_diferencia_anios(fecha_str):
    fecha = datetime.strptime(fecha_str, '%d-%b-%Y')
    diferencia = fecha_especifica - fecha
    return diferencia.days // 365

# Calcular y mostrar la diferencia en años para cada fecha
for fecha_str in fechas:
    diferencia_anios = calcular_diferencia_anios(fecha_str)
    print(f'{diferencia_anios}')
