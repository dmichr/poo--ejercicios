from abc import ABC, abstractmethod
from datetime import date, time
import datetime

class Persona(ABC):
    _secuencia = 0

    def __init__(self, nombre, estado):
        Persona._secuencia = Persona._secuencia+1
        self.__id = Persona._secuencia
        self.nombre = nombre
        self.estado = estado
        
    #input("Ingrese el nombre: ").upper()
 
    @property
    def id(self):
        return self.__id

    @abstractmethod
    def mostrarDatos(self):
        pass

class Cliente(Persona):
   
    def __init__(self,  nombre, cedula, estado):
        super().__init__(nombre, estado)
        self.cedula =cedula
    #Validar.ingreso_cedula("Ingrese cedula: ", "Dato incorrecto!")
        

    def mostrarDatos(self):
        print(f'Cliente #  {self.id} Nombre:  {self.nombre} con C.I  {self.cedula} ')
    
cl=Cliente("michel","1010101010",True)
# cl.mostrarDatos()
class Factura:
    _idFactura = 0
    def __init__(self, cliente,fecha, total,estado):
        Factura._idFactura += 1
        self.__idFactura=Factura._idFactura
        self.fecha = fecha
        self.cliente = cliente
        self.total = total
        self.estado=estado

#Validar.ingreso_fecha( "Ingrese fecha dd-mm-aaaa :", "error")
#Validar.solo_decimales("Total de factura: ", "Error!")


    @property
    def idF(self):
        return self.__idFactura

    def mostrarDatos(self):
        print("Factura N° 00{:34}Fecha:  {}".format(self.idF, self.fecha))
        print(self.cliente.mostrarDatos())
        print(f'Total de factura: {self.total} ')
        
fac=Factura(cl,"01200",500,True)

class Calcuo(ABC):  # interface

    @abstractmethod
    def realizarPago(self):
        pass


class Pago(Calcuo):
    _idPago = 0

    def __init__(self,fecha,valor ):
        Pago._idPago += 1
        self.__idPago = Pago._idPago
        self.fecha = fecha  
        self.valor = valor

    @property
    def idF(self):
        return self.__idPago

    def mostrarDatos(self):
        print(f'codigo de pago #{self.idF} ---  {self.fecha} --- {self.valor} ')

    def realizarPago(self):
        return self.valor 


# fecha = Validar.ingreso_fecha(" Fecha de pago: ", "error")
# valor = Validar.solo_decimales("Cantidad a pagar:", "dato no válido")
# asd=Pago(fecha, valor)
# asd.realizarPago()
# asd.mostrarDatos()

class DetCredito:
    _id = 0

    def __init__(self,cuota,aamm, estado):
        DetCredito._id += 1
        self.__idDetCredito = DetCredito._id
        self.aamm = aamm
        self.cuota = cuota
        self.detPago = []
        self.estado = estado
        

    @property
    def idDetC(self):
        return self.__idDetCredito

    def mostrarDatos(self):
        print(f'----------- Control de Credito---------')
        print(self.detPago)

    def agregarPago(self,fecha,valor):
        pago=Pago(fecha, valor)
        abono=pago.realizarPago()
        self.detPago.append(abono)
        return self.detPago
   
# credito= DetCredito(20,2023,False)  
# credito.agregarPago ()
# print(credito.detPago)
# credito.agregarPago()
# print(credito.detPago)

class CabCredito:
    _id = 0

    def __init__(self, factura,deuda, finicio,numeroCuotas,estado):
        DetCredito._id += 1
        self.__idCabCredito = CabCredito._id
        self.factura= factura 
        self.fecha = str(datetime.date.today())
        self.deuda= deuda
        self.numeroCuotas= numeroCuotas
        self.cuota = float
        self.aammInicial=finicio
        self.detCredito = []
        self.estado = estado

    @property
    def idDetC(self):
        return self.__idCabCredito

    def mostrarDatos(self):
        print(f'----------- Control de Credito---------')
        print(self.detPago)
        
    @staticmethod
    def getInteres(fpago,fvencimiento, cuota:float):
        if fpago>fvencimiento:
            sumarIn=cuota+(cuota*0.05)
        else:
            sumarIn = cuota
        return sumarIn
        
    
    def agregarDetalle(self, fecha, valor,cuota, aamm, estado=True,):
        detalle=DetCredito(cuota,aamm,estado)
        cred=detalle.agregarPago(fecha, valor)  #retorna una lista del valor capturado
        self.detCredito.append(cred)
        return self.detCredito
    
    
# clase=CabCredito(fac,fac.total,fac.fecha,True)
# det=clase.agregarDetalle("2020",40,14,fac.fecha,True)
# det = clase.agregarDetalle("2020", 50, 14, fac.fecha, True)
# det = clase.agregarDetalle("2020", 60, 14, fac.fecha, True)

# print(det)

# def Extract(lst):
#     return [item[0] for item in lst]

# a=Extract(det)
# p=sum(a)
# print(p)


