import pandas as pd
from crudArhivos import Archivo
arch = Archivo("./archivos/facturas.txt",".")
lista=arch.leerArchivo()
codigos = []
fechas = []
nombres = []
cedulas = []
total=[]
for i in lista:
    codigos.append(i[0])
    fechas.append(i[1])
    cedulas.append(i[2])
    nombres.append(i[3])
    total.append(i[4])
dict = {"Cod": codigos, "Fecha": fechas, "Cliente": nombres, "CI": cedulas, "Total":total}
df = pd.DataFrame(dict)
df.style.set_properties(**{'text-aling': 'center'}).hide_index()

arch = Archivo("./archivos/clientes.txt", ".")
lista2 = arch.leerArchivo()
codigos = []
nombres = []
cedulas = []
for i in lista2:
    cedulas.append(i[2])
    nombres.append(i[1])
    codigos.append(i[0])

dict = {"Cod": codigos, "Cliente": nombres, "CI": cedulas}
df = pd.DataFrame(dict)
df.style.set_properties(**{'text-aling': 'center'}).hide_index()

