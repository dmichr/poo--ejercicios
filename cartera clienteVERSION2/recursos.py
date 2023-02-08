import os
from datetime import datetime
from dateutil.relativedelta import relativedelta


def gotoxy(x, y):
    print("%c[%d;%df" % (0x1B, y, x), end="")


def borrarPantalla():
    os.system("cls")


def valida(name):
    return name.replace(" ", "").isalpha()#full para entrada de nombres espacios en blancos valida
    

def generaFechas(valor: str, numeCuotas):
    c = 0
    lista = []
    while c < numeCuotas:
        valor = datetime.strptime(valor, '%Y-%m-%d')
        valor = valor + relativedelta(months=1)
        valor = datetime.strftime(valor, '%Y-%m-%d')
        lista.append(str(valor))
        c += 1
    return lista[-1]


def compararFechas(fecha_Ingreso, fecha_Corte, total):

    fecha_Ingreso = datetime.strptime(fecha_Ingreso, '%Y-%m-%d')
    fecha_Corte = datetime.strptime(fecha_Corte, '%Y-%m-%d')
    if fecha_Ingreso > fecha_Corte:
        sumarIn = (float(total)*0.03)
        return sumarIn
    else:
        return None



