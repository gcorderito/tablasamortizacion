from datetime import date
from datetime import datetime
from datetime import timedelta
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

def calcular_amortizacion_frances(monto, tasa, n, frecuencia, diapago, fechaprimerpago):
    #Obtener la primera fecha mínima de pago
    fechamaxima = fechaprimerpago
    if frecuencia == 12: #mensual
        fechaminima = fechamaxima - timedelta(days=30)
    elif frecuencia == 24: #Quicenal
        fechaminima = fechamaxima - timedelta(days=15)
    elif frecuencia == 52: #Semanal
        fechaminima = fechamaxima - timedelta(days=7)
    elif frecuencia == 360 or frecuencia == 365: #diario
        fechaminima = fechamaxima - timedelta(days=1)
    else:
        fechaminima = fechamaxima

    # Convertir la tasa de interés anual a tasa periódica
    i = tasa / (frecuencia * 100)

    # Calcular la cuota periódica
    c = (i * monto) / (1 - (1 + i)**(-n))

    # Inicializar las variables
    saldo_insoluto = monto
    amortizacion_total = 0
    tabla_amortizacion = []


    # Calcular la tabla de amortización
    for periodo in range(1, n + 1):
        # Calcular seguros
        seguros = saldo_insoluto*(0.1/100)
        
        # Calcular los intereses
        intereses = saldo_insoluto * i

        # Calcular la amortización
        amortizacion = c - intereses
        amortizacion_total += amortizacion

        # Calcular el saldo insoluto
        saldo_insoluto -= amortizacion
        if saldo_insoluto < 0:
            saldo_insoluto = 0

        # Calcular el total a pagar
        apagar = c + seguros

        #Calcular la diferencia de días entre la fecha máxima y la fecha mínima de pago
        diferenciadias = fechamaxima - fechaminima

        # Agregar los datos a la tabla de amortización
        tabla_amortizacion.append({
            "Periodo": periodo,
            "Cuota": round(c, 2),
            "Intereses": round(intereses, 2),
            "Capital": round(amortizacion, 2),
            "Saldo capital": round(saldo_insoluto, 2),
            "Seguros" : round(seguros, 2),
            "A pagar" : round(apagar, 2),
            "Fecha Minima" : str(fechaminima),
            "Fecha Maxima" : str(fechamaxima),
            "Diferencia dias" : diferenciadias.days + 1
        })

        #Sumar el siguiente mes para la próxima cuota
        fechaminima = fechamaxima + timedelta(days=1)
        if frecuencia == 12: #Si el plazo es mensual
            fechamaxima = sumar_mes_fecha(fechamaxima)
            if diapago > fechamaxima.day:
                fechamaxima = sumar_dias_faltantes(fechamaxima,diapago)
        elif frecuencia == 24: #Si el plazo es Quicenal
            fechamaxima = fechamaxima + timedelta(days=15)
        elif frecuencia == 52: #Si el plazo es Semanal
            fechamaxima = fechamaxima + timedelta(days=7)
        elif frecuencia == 360 or frecuencia == 365: #Si el plazo es diario
            fechamaxima = fechamaxima + timedelta(days=1)

    # Devolver la tabla de amortización y la amortización total
    return tabla_amortizacion, round(amortizacion_total, 2)

#Valores de ejemplo
monto = 100000
tasa = 15.6
numcuotas = 60
frecuencia = 12
diapago = 15
fechaprimerpago = date(2023,4,15)

tabla, amortizacion_total = calcular_amortizacion_frances(monto, tasa, numcuotas, frecuencia, diapago, fechaprimerpago)

print("Tabla de amortización:")
for fila in tabla:
    print(fila)

print("Amortización total:", amortizacion_total)