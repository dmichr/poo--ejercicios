
import time
from time import strftime
import os
from recursos import gotoxy, borrarPantalla, compararFechas, generaFechas
from componentes import Menu, Validar
from cartera_de_Clientes  import Cliente, Factura, CabCredito
from crudArhivos import Archivo , Listas
open("./archivos/facturas.txt", 'a')
open("./archivos/clientes.txt", 'a')
open("./archivos/pagos.txt", 'a')
open("./archivos/confpagos.txt", 'a')

#procesos menu opc 1

def grabarCliente():
    borrarPantalla();gotoxy(1, 4);print("="*20, "REGISTRO DE CLIENTES", "="*20)
    user = Validar.ingreso_nombre("Nombre:", "error", 5, 6)
    item = Validar.ingreso_cedula("Cedula:", "error", 6, 7)
    archiClientes = Archivo("./archivos/clientes.txt", "|")
    with open("./archivos/clientes.txt", 'r') as fp:
        lines = fp.readlines()
        r = []
        for line in lines: 
            if line.find(item) != -1:
                r.append(str(line))
    if r:
        gotoxy(5, 10);input(
            f'Ya existe un usuario registrado con la CI. {item}  \n\n  Presione una tecla para continuar...')
    else:
        gotoxy(5, 10);print("Guardar datos de cliente (s/n):")
        gotoxy(40, 10);grabar = input().lower()
        if grabar == "s":
            cliente = Cliente(user, item, True)
            archiClientes = Archivo("./archivos/clientes.txt", "|")
            clientes = archiClientes.leer()
            if clientes:
                idSig = int(clientes[-1][0])+1
            else:
                idSig = 1
            datos = [str(idSig), cliente.nombre, cliente.cedula]
            datos = '|'.join(datos)
            archiClientes.escribir([datos], "a")
            gotoxy(5, 13);input(
                "Registro exitoso ✅\nPresione una tecla para continuar...")
        else:
            gotoxy(5, 13);input("Registro No fue Grabado\npresione una tecla para continuar...")




#procesos menu opc 2 FACTURAS
#generar una factura


    # numeroCuota = int(input("Total meses de diferido:  "))
    # cuota = (total/numeroCuota)
    # cuota = "{:.2f}".format(cuota)
    # print("Cuota mensual corresponde a  ", cuota, "$")             
    
    # PARA USAR EN CABECERA CREDITO
    
    
    
    
    
    


def generarFactura():
    borrarPantalla()
    
    item = Validar.ingreso_cedula("CI: ", "error!", 15, 7)
    with open("./archivos/clientes.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        r = []
        for line in lines:
            # check if string present on a current line
            if line.find(item) != -1:
                r.append(str(line))
    if r:
        cadenaCliente=Listas.presentarLista(r)
        gotoxy(32, 7);print(cadenaCliente[1])
        cliente = Cliente(cadenaCliente[1], cadenaCliente[2], True)
        input("[continuar]")
        borrarPantalla()
        fecha = Validar.ingreso_fecha(" Fecha (dd-mm-aaaa) :", "error!")
        total= Validar.solo_decimales("Total de factura: ", "Error!")
        factura=Factura(cliente,fecha,total, True)
        gotoxy(1, 7); print("Registrar factura (s/n):")
        gotoxy(30, 7);grabar = input().lower()
        if grabar == "s":
            archiFacturas = Archivo("./archivos/facturas.txt", "|")
            archiPagos = Archivo("./archivos/pagos.txt", "|")
            facturas = archiFacturas.leer()
            if facturas:
                idSig = int(facturas[-1][0])+1
            else:
                idSig = 1
            datos = [str(idSig), str(factura.fecha),factura.cliente.cedula, factura.cliente.nombre,
                    str(factura.total)]
            datos = '|'.join(datos)
            archiFacturas.escribir([datos], "a")
            datos2= [str(idSig), factura.cliente.cedula, "" ]
            datos2 = '|'.join(datos2)
            archiPagos.escribir([datos2], "a")
            gotoxy(1, 14);input("Factura generada con éxito ✅  ")
        else: 
            gotoxy(1, 14);input("El ingreso no fue grabado\npresione una tecla para continuar...")
    else:
       gotoxy(15, 10); print("No hay registros!")
       gotoxy(15, 12);input("Para continuar presione enter▶ ")
    

    
    
   
def eliminarFactura():
    borrarPantalla()
    item = Validar.ingreso_cedula("Busqueda por CI: ", "Dato no valido", 5,5)
    with open("./archivos/facturas.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        r=[]
        for line in lines:
            # check if string present on a current line
            if line.find(item) != -1:
                r.append (str(line))
                
    if  r:
        borrarPantalla()
        gotoxy(5, 3);print("-"*25, "Facturas encontradas:", "-"*25)
        def presenta(r):
            lista=[]
            for i in r:
                x=(''.join(i))
                x= i[:-1]
                x=(x.split("|"))
                lista.append(x)
                print(
                    f'       N° 00{x[0]}---fecha: {x[1]}---CI {x[2]}--Cliente: {x[3]} --total: {x[4]} ')
            return lista
        mostrarlista=presenta(r)
        
        
        codigo = Validar.solo_numeros("Digite codigo de factura a eliminar:  ", "Dato no valido",3,10 )
        for cod in mostrarlista :
            if cod[0]==str(codigo):
                borrarPantalla()
                gotoxy(5,5);print ("el sistema está borrando la factura...")
                def operacionOS():   
                    with open("archivos/facturas.txt", "r") as input:
                        with open("temp.txt", "w") as output:
                            for line in input:
                                if not line.strip("\n").startswith(str(codigo)):
                                    output.write(line)
                    os.replace('temp.txt', 'archivos/facturas.txt')
                operacionOS()
                gotoxy(5, 6);input(f'la factura #{codigo} ha sido eliminada ✅ ')
        else:
            input("(presione enter para continuar)...")
             
    else: 
        gotoxy(5, 14);input("No se encontraron registros!\n     presione una tecla para continuar...")
    




def buscarFactura():
    borrarPantalla()
    item = Validar.ingreso_cedula("CI: ", "Dato no valido", 5, 5)
    with open("./archivos/facturas.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        r = []
        for line in lines:
            # check if string present on a current line
            if line.find(item) != -1:
                r.append(str(line))

    if r:
        borrarPantalla()
        gotoxy(7, 3);print("-"*33, "Resultados de la busqueda:", "-"*33, "\n \n")
        
        for i in r:
            
            x = (''.join(i))
            x = i[:-1]
            x = (x.split("|"))
            print(f'      Factura N° 00{x[0]}---fecha: {x[1]}--- CI: {x[2]}---Cliente: {x[3]}---total: {x[4]} ')
        (input("\n \n \n presione una tecla para continuar..."))
        
    else:
        
        gotoxy(5, 8);input("No se encontraron registros!\n     presione una tecla para continuar...")


#procesos menu opc 3 CREDITOS
#apertura de credito

def aperturarCredito():
    #buscar factura por id
    borrarPantalla()
    item = Validar.ingreso_cedula("Busqueda por CI: ", "Dato no valido", 5, 5)
    with open("./archivos/facturas.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        r = []
        for line in lines:
            # check if string present on a current line
            if line.find(item) != -1:
                r.append(str(line))

    if r:
        borrarPantalla()
        gotoxy(5, 3);print("-"*25, "Facturas generadas al cliente:", "-"*25)

        def presenta(r):
            lista = []
            for i in r:
                x = (''.join(i))
                x = i[:-1]
                x = (x.split("|"))
                lista.append(x)
                print(
                    f'       N° 00{x[0]}---fecha: {x[1]}---CI {x[2]}--Cliente: {x[3]} --total: {x[4]} ')
            return lista
        mostrarlista = presenta(r)

        codigo = Validar.solo_numeros(
            "Digite codigo de factura para configurar credito:  ", "Dato no valido", 3, 10)
        for cod in mostrarlista:
            if cod[0] == str(codigo):
                facCliente=Factura(cod[2],cod[1],cod[4],True)
                cliente=Cliente(cod[3],cod[2], True)
                borrarPantalla()
                gotoxy(1, 4);print("="*20, "CONFIGURACION DEL CREDITO", "="*20)
                meses = Validar.solo_numeros("Meses a diferir:", "error!",1,6)
                cuota= float(cod[4])/int(meses)
                cuota = float("{:.2f}".format(cuota))
                gotoxy(1, 7);print(f'la factura #{cod[0]} se ha diferido para {meses} meses ')
                gotoxy(1, 8);print(f'cuota mensual a cancelar ----> {cuota} $ por el cliente {cliente.nombre} ')
                gotoxy(3, 10);print("Guardar configuracion (s/n):")
                gotoxy(35, 10);grabar = input().lower()
                if grabar == "s":
                    archiConfPago = Archivo("./archivos/confpagos.txt", "|")
                    datos = [codigo, str(meses),str(cuota)]
                    datos = '|'.join(datos)
                    archiConfPago.escribir([datos], "a")
                    gotoxy(5, 14)
                    input("Configuracion con éxito ✅  ")
                else:
                    gotoxy(5, 14)
                    input("El ingreso no fue grabado\npresione una tecla para continuar...")
        else:
            input("(presione enter para continuar)...")
    else:
        gotoxy(5, 14);input("No se encontraron registros!\n     presione una tecla para continuar...")
    


def revisarCredito():
    #buscar factura por id
    borrarPantalla()
    item = Validar.ingreso_cedula("Busqueda por CI: ", "Dato no valido", 5, 5)
    with open("./archivos/facturas.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        r = []
        for line in lines:
            # check if string present on a current line
            if line.find(item) != -1:
                r.append(str(line))

    if r:
        borrarPantalla()
        gotoxy(8, 3);print("-"*25, "Facturas encontradas al cliente:", "-"*25)

        def presenta(r):
            lista = []
            for i in r:
                x = (''.join(i))
                x = i[:-1]
                x = (x.split("|"))
                lista.append(x)
                print(
                    f'       N° 00{x[0]}---fecha: {x[1]}---CI {x[2]}--Cliente: {x[3]} --total: {x[4]} ')
            return lista
        mostrarlista = presenta(r)

        codigo = Validar.solo_numeros(
            "Digite codigo de factura para revisar credito:  ", "Dato no valido", 3, 10)
        for cod in mostrarlista:
            if cod[0] == str(codigo):
                borrarPantalla()
                fac = Factura(cod[2], cod[1], cod[4], True)
                #ir a buscar la conf del credito por id codigo 
                buscarconf = Archivo("archivos/confpagos.txt","|")
                confg=buscarconf.leer()
                def configuracion(confg):
                    for i in confg:
                        if i[0] == str(codigo):
                            return i 
                confPago=configuracion(confg)
                meses=confPago[1]
                cuotavalor = confPago[2]
                clase = CabCredito (fac, fac.total, fac.fecha, meses,True)
                fechaVencimiento= generaFechas(fac.fecha,int(meses))
                #mandar a buscar los pagos 
                arch = Archivo("./archivos/pagos.txt", "|")
                p = arch.leerArchivo()
                #print(p)
                def extraer(p,codigo):
                    for line in p:
                        # check if string present on a current line
                        if line[0] == codigo:
                            line.pop()
                            line.pop(0)
                            line.pop(0)
                            return line   
                r=extraer(p,codigo)
                for i,k in zip(r[0::2],r[1::2]):
                    det = clase.agregarDetalle(i, k, cuotavalor, fac.fecha, True)
                for i, k in zip(r[0::2], r[1::2]):
                    lista=[]
                    impuesto = compararFechas(i, fechaVencimiento, fac.total)
                    if impuesto:
                        lista.append(impuesto)
                def Extract(lst):
                    return [item[0] for item in lst]
                numeros=Extract(det)
                print(f'pagos realizados:{numeros} ')
                result = sum(map(float, numeros))
                result = float("{:.2f}".format(result))
                print(f'total: -{result}' )
                pendiente=float(fac.total)-result
                pendiente = float("{:.2f}".format(pendiente))
                print('pendiente ', (pendiente))
                print('intereses ', (lista))
                
                
        input("continuar:") 
    else:
        input("No se encontraron registros!\n     presione una tecla para continuar...")
                 
    






#procesos de OPCION 4 PAGOS
''' registrar pago '''

def registrarPago():
    borrarPantalla()
    item = Validar.ingreso_cedula("Busqueda por CI: ", "Dato no valido", 5, 5)
    with open("./archivos/facturas.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        r = []
        for line in lines:
            # check if string present on a current line
            if line.find(item) != -1:
                r.append(str(line))

    if r:
        borrarPantalla()
        gotoxy(5, 3);print("-"*30, "Facturas encontradas:", "-"*30)

        def presenta(r):
            lista=[]
            for i in r:
                x = (''.join(i))
                x = i[:-1]
                x = (x.split("|"))
                lista.append(x)
                print(
                    f'       N° 00{x[0]}---fecha: {x[1]}---CI {x[2]}--Cliente: {x[3]} --total: {x[4]} ')
            return lista
        lista=presenta(r)

        codigo = Validar.solo_numeros(
            "Digite codigo de factura a pagar:  ", "Dato no valido", 3, 10)
        for cod in lista:
            if cod[0] == str(codigo):
                borrarPantalla()
                fechaPago=Validar.ingreso_fecha(" Fecha (dd-mm-aaaa): ", "error")
                valor=Validar.solo_decimales('Monto de pago:', "error")
                
                print("Registrar pago (s/n):")
                gotoxy(26, 3);grabar = input().lower()
                if grabar == "s":
                    with open('archivos/pagos.txt', 'r') as file:
                        # read a list of lines into data
                        data = file.readlines()
                        dat = Listas.presentarLL(data)
                        def bus():
                            for i in dat:
                                if i[0] == (str(codigo)):
                                    return (i)

                        busqueda = bus()
                        #print(busqueda)
                        index = dat.index(bus())

                        
                        # now change the 2nd line, note that you have to add a newline
                        linea = data[index]
                        datos = [str(fechaPago), str(valor), ""]
                        datos = '|'.join(datos)

                        data[index] = (linea[:-1]) + datos+'\n'
                        
                    # and write everything back
                        with open('archivos/pagos.txt', 'w') as file:
                            file.writelines(data)
                    gotoxy(5, 13);input(
                        "Pago registrado con exito ✅\nPresione una tecla para continuar...")
                else:
                    input('No se guardó el pago (presione enter para continuar)...')
        else:
            input(" (presione enter para continuar)...")

    else:
        gotoxy(5, 14);input("No se encontraron registros!\n     presione una tecla para continuar...")
 
    
#procesos de OPCION CONSULTA GENERALES
#procesos de VER NOMINA CLIENTES
def mostrarNomina():
    borrarPantalla()
    nominaArchivo=Archivo("archivos/clientes.txt","|")
    data = nominaArchivo.leer()
    encabezados = [["Codigo ","Nombre","Cedula", ]]
    n = max(len(item[0]) for item in data) + 8
    m = max(len(item[0]) for item in encabezados) + 8
    gotoxy(22, 3);print("NOMINA CLIENTES")
    gotoxy(7, 4);print("."*60)
    for item in encabezados:
        gotoxy(7, 5);print('  {:<{m}}  {:<{m}}   {:<{m}} '.format(*item, m=m))
    gotoxy(7, 6);print("."*60)
    for item in data:
        print("         {:<{n}}   {:<{n}}        {:<{n}} ".format(*item, n=n))
    (input("\n\n\n     seleccione un tecla para continuar:  "))


#procesos de VER REGISTRO FACTURAS
def mostrarRegistro():
    borrarPantalla()
    nominaArchivo = Archivo("archivos/facturas.txt", "|")
    data = nominaArchivo.leer()
    
    encabezados = [["Codigo ", "Fecha", "CI." , "Nombre", "Total"]]
    n = max(len(item[0]) for item in data) + 8
    m = max(len(item[0]) for item in encabezados) + 5

    gotoxy(40, 3);print("REGISTRO FACTURAS")
    gotoxy(7, 4);print("."*100)
    for item in encabezados:
        gotoxy(7, 5);print('  {:<{m}}  {:<{m}}   {:<{m}}   {:<{m}} {:<{m}} '.format(*item, m=m))
    gotoxy(7, 6);print("."*100)
    for item in data:
        print(
            "         {:<{n}}{:<{n}}    {:<{n}}     {:<{n}}          {:<{n}} ".format(*item, n=n))
    (input("\n\n\n     seleccione un tecla para continuar:  "))
  

borrarPantalla()

# Menu Proceso Principal
opc = ''
while opc != '6':
    borrarPantalla()
    menu = Menu('CARTERA DE CLIENTES', [ "1) Cliente", "2) Factura", "3) Credito", "4) Pagos", "5) Consultas generales","6) Salir"], 30, 5)
    opc = menu.menu()
    if opc == "1":
        grabarCliente()        
        
    elif opc == "2":
        borrarPantalla()
        opc2 = ''
        while opc2 != '4':
            borrarPantalla()
            gotoxy(0,3);print("="*20, "PORTAL DE FACTURACIÓN", "="*20)
            menu2 = Menu("Servicios", ["1) Generar factura", "2) Buscar factura",
                        "3) Eliminar factura", "4) Salir"], 25, 5)
            opc2 = menu2.menu()
            if opc2 == "1":
                generarFactura()   
                
            elif opc2 == "2":
                buscarFactura()
                  
            elif opc2 == "3":
                eliminarFactura()
                
                
    elif opc == "3":
        borrarPantalla()
        opc2 = ''
        while opc2 != '3':
            borrarPantalla()
            gotoxy(0, 3)
            print("="*20, "PORTAL DE CREDITO", "="*20)
            menu2 = Menu("Servicios", ["1) Apertura credito", "2) Revisar credito/cliente",
                                       "3) Regresar"], 25, 5)
            opc2 = menu2.menu()
            if opc2 == "1":
                aperturarCredito()

            elif opc2 == "2":
                revisarCredito()

    
    
    elif opc == "4":
        registrarPago()
        
        
    elif opc == "5":
        borrarPantalla()
        
        menu = Menu("-------------------------------", ["1) Ver Nomina Clientes", "2) Ver Registro Facturas",
                "3) Salir"], 30, 5)
        opc = menu.menu()
        
        if opc == "1":
            mostrarNomina()

        elif opc == "2":
            mostrarRegistro()
            
    else:
        print("Opcion no valida")

input("Presione una tecla para salir")
borrarPantalla()


