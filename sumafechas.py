from datetime import datetime, timedelta

# Función para sumar fechas y almacenar los resultados en una lista
def sumar_fechas(fecha_inicial, cantidad, unidad, repeticiones):
    fechas = []
    fecha = datetime.strptime(fecha_inicial, '%d/%m/%Y')
    delta = { 'dias': timedelta(days=cantidad),
              'meses': timedelta(days=cantidad*30),
              'anios': timedelta(days=cantidad*365) }[unidad]
    for i in range(repeticiones):
        fecha = fecha + delta
        fechas.append(fecha.strftime('%d/%m/%Y'))
    return fechas

# Solicitar entrada del usuario
fecha_inicial = input('Ingrese la fecha inicial en formato dd/mm/yyyy: ')
cantidad = int(input('Ingrese la cantidad a sumar: '))
unidad = input('Ingrese la unidad a sumar (dias, meses o anios): ')
repeticiones = int(input('Ingrese la cantidad de veces que se sumará la fecha: '))

# Sumar fechas y mostrar resultados
fechas = sumar_fechas(fecha_inicial, cantidad, unidad, repeticiones)
print('Las fechas sumadas son:')
for fecha in fechas:
    print(fecha)
