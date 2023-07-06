# Ejercicio 680: Crear una función para sumar un mes a una fecha.

from datetime import date, timedelta
from calendar import monthrange

def cantidad_dias_mes(mes, agnio):
    """
    Obtiene la cantidad de días de un mes y año específicos.
    """
    return monthrange(agnio, mes)[1]

def sumar_mes_fecha(fecha):
    try:
        dias_mes_siguiente = cantidad_dias_mes(fecha.month+1, fecha.year)
    except:
        dias_mes_siguiente = cantidad_dias_mes(1, fecha.year)

    dias_mes = cantidad_dias_mes(fecha.month, fecha.year)
    if fecha.day > dias_mes_siguiente:
        resultado = fecha + timedelta(days=dias_mes_siguiente)
    else:
        resultado = fecha + timedelta(days=dias_mes)
    return resultado

def sumar_dias_faltantes(fecha,diafijo):
    dias_mes = cantidad_dias_mes(fecha.month, fecha.year)

    if diafijo > dias_mes:
        fechanueva = date(fecha.year,fecha.month,dias_mes)
    else:
        fechanueva = date(fecha.year,fecha.month,diafijo)

    return fechanueva

diafijo = 15
fecha = date(2021, 7, 15)
resultado = sumar_mes_fecha(fecha)
#Se agrega días en caso de que la fecha no corresponda la día fijo
print(resultado)
if diafijo > resultado.day:
    fechanueva = sumar_dias_faltantes(resultado,diafijo)
    print(fechanueva)
