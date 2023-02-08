'''  para operar fechas'''
import pandas as pd
from calendar import month
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# ahora=datetime.now()
# ahora = datetime.strftime(ahora, '%d-%m-%Y')
# dentro_de_un_mes = ahora + relativedelta(months=1)


# now = datetime.now().date()
# new_date = now + timedelta(months=1)
# print(now)
# print(new_date)

# import numpy as np

# # adding months to a given date
# print('old date is : ' + str(np.datetime64('2022-04')))
# new_date = np.datetime64('2022-04') + np.timedelta64(5, 'M')
# print('new date is : '+str(new_date))



# now = datetime.now()
# format = now.strftime('%d-%m-%Y')
# print(format)
# new_date = now + relativedelta(months=1)
# format1 = new_date.strftime('%d-%m-%Y')
# print(format1)
# numeroCuotas=5
# for i in range(numeroCuotas):
#     fecha = datetime.date(2021, 7, 22)
#     fecha = fecha.replace(month=1)
#     print(fecha)


# # adding months to a particular date
# present = '2022-05-05'
# print('date : ' + present)
# new_date = pd.to_datetime(present)+pd.DateOffset(months=5)
# print('new date is : '+str(new_date) )
valor = "2023-02-06"
def generaFechas(valor:str, numeCuotas):
    c=0
    lista = []
    while c<numeCuotas: 
        valor = datetime.strptime(valor, '%Y-%m-%d')
        valor =valor + relativedelta(months=1)
        valor = datetime.strftime(valor, '%Y-%m-%d')
        lista.append(str(valor))
        c+=1
    return lista[-1]

t=generaFechas("2023-02-04",10)

# valor = "2023-02-06"
# valor = datetime.strptime(valor, '%Y-%m-%d')

#comparar fechas para generar interes 
#si alguno de los pagos es mayor a la ultima fecha interes
# def compararFechas(fecha_Ingreso, fecha_Corte,total):
    
#     fecha_Ingreso = datetime.strptime(fecha_Ingreso, '%Y-%m-%d')
#     fecha_Corte = datetime.strptime(fecha_Corte, '%Y-%m-%d')
#     if fecha_Ingreso > fecha_Corte:
#         sumarIn = (total*0.03)
#         return sumarIn
#     else:
#         return None


# impuesto = compararFechas("2025-03-05", t, 2500)
# if impuesto:
#     print (impuesto)
    






