from datetime import datetime, date
from empresa import Empresa
from persona import Paciente, Doctor, Enfermera
import os




class Medicamento:
    _secuencia = 0

    def __init__(self, des, pre, sto, ):
        Medicamento._secuencia += 1
        self.__codigo = Medicamento._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
        

    @property
    def codigo(self):
        return self.__codigo

    def mostrarMedicamento(self):
        print(self.codigo, self.descripcion, )
        
        
class Cita:
    _secuencia = 0
    _hora=datetime.now()
    def __init__(self, des, pre, sto,doc,pac,nurse ):
        Medicamento._secuencia += 1
        self.__codigo = Medicamento._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
        self.doctor=doc
        self.fecha=date.today()
        self.hora = Cita._hora.strftime("%H:%M")
        self.paciente= pac
        self.enfermera=nurse


    @property
    def codigo(self):
        return self.__codigo

    
    def mostrarPersona(self):
        print("\nDATOS DE SU CONSULTA\n"
            f'Cita medica #{self.codigo} ---{self.descripcion}-- a las {self.hora} -- el {self.fecha} \nAsistido por Lcd. {self.enfermera} ')
        
    


class DetalleReceta:
    _codigo = 0

    def __init__(self, articulo, cantidad):
        DetalleReceta._codigo += 1
        self.codigo = DetalleReceta._codigo
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad


class Receta:
    _factura = 0
    _iva = 0.12

    def __init__(self, paciente, doctor):
        Receta._factura = Receta._factura + 1
        self.factura = str(Receta._factura)
        self.fecha = date.today()
        self.paciente = paciente
        self.subtotal = 0
        self.iva = 0
        self.total = 0
        self.detalleReceta = []
        self.doctor=doctor

    def agregarItems(self, articulo, cantidad):
        detalle = DetalleReceta(articulo, cantidad)  #Composición
        self.subtotal += round(detalle.precio*detalle.cantidad, 2)
        self.iva = round(self.subtotal*Receta._iva, 2)
        self.total = round(self.subtotal+self.iva, 2)
        self.detalleReceta.append(detalle)

    def mostrarReceta(self, empNombre, empRuc):
        print("Centro Médico: {:30} Ruc :{:}".format(empNombre, empRuc))
        print("Receta N° 00{:34}Fecha:  {}".format(self.factura, self.fecha))
        self.paciente.mostrarPersona()
        self.doctor.mostrarPersona()
        print("-"*25, "Descripción", "-"*25)
        print("Código    Medicamento              Precio Cantidad   Subtotal")
        for det in self.detalleReceta:
            x = det.precio*det.cantidad

            print("{:5} {:30} {:} {:5} {:} {:} ".format(det.codigo, det.articulo.descripcion,
                  "%.2f" % det.precio, det.cantidad, "     ", "%.2f" % x,))
        print("-"*62)
        print(" "*40, "Subtotal=> ", "%.2f" % self.subtotal)
        print(" "*45, "Iva=> ", "%.2f" % self.iva)
        print(" "*43, "Total=> ", "%.2f" % self.total)

os.system("cls") 


empresa = Empresa()
paciente = Paciente("Kylian Mbappé", "7651239874", "0912131415","da@gmail.com", 23, 45, 178, "M", "gastroenteritis")
doctor = Doctor("Jair Andrade Zambrano", "12034598712", "0912131415", "jandradez@gmail.com", 23456, "general")
enfermera=Enfermera("Gabriela Pilozo", 1102338810, 43030-455,"gpilozo@gmail.com")
cita=Cita(" CM/General", 20,40, doctor.nombre, paciente.nombre, enfermera.nombre) #agregaciones 
farmaco1 = Medicamento("Prilosec 800 mg", 35, 100)     #instancias
farmaco2 = Medicamento("Famotidina  500 mg", 12.40, 200)
farmaco3 = Medicamento("Omeprazol  500 mg", 31.18, 200)
rec = Receta(paciente,doctor)
rec.agregarItems(cita, 1)
rec.agregarItems(farmaco1, 12)
rec.agregarItems(farmaco2, 21)
rec.agregarItems(farmaco3, 14)
rec.agregarItems(cita, 1)
rec.mostrarReceta(empresa.nombre, empresa.ruc)
cita.mostrarPersona()
paciente.agendar()


