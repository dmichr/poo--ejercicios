
from datetime import  datetime 
import time
from recursos import gotoxy, valida


class Menu:
    def __init__(self, titulo="", opciones=[], col=6, fil=1):
        self.titulo = titulo
        self.opciones = opciones
        self.col = col
        self.fil = fil

    def menu(self):
        gotoxy(self.col, self.fil)
        print(self.titulo)
        self.col -= 5
        self.fil += 1
        for opcion in self.opciones:
            self.fil += 1
            gotoxy(self.col, self.fil)
            print(opcion)
        gotoxy(self.col+5, self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc






class Validar:
    
    @staticmethod
    def ingreso_fecha( mensaje, mensajeError):
        while True:
            valor = (input("{} ".format(mensaje)))
            try:
                valor = datetime.strptime(valor, '%d-%m-%Y') 
                if valor :
                    break
            except ValueError:
                print(mensajeError)        
        return(valor.date()) 
        
    @staticmethod
    def solo_decimales( mensaje, mensajeError):
        while True:
            valor = str(input(" {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("  {} ".format(mensajeError))
        return valor
    
    @staticmethod
    def ingreso_cedula(mensaje, mensajeError, col, fil):
        while True:
            gotoxy(col, fil);valor = str(input(" {} ".format(mensaje)))
            if len(valor) == 10 and valor.isdigit():
                break
            else:
                gotoxy(col, fil);print(" {}            ".format(mensajeError)) 
                time.sleep(1)
                gotoxy(col, fil);print(" "*40)
        return valor

    

    @staticmethod   #funcion lista para validar nombres
    def ingreso_nombre(mensaje, mensajeError, col, fil):
        while True:
            gotoxy(col, fil);valor = str(input("  {} ".format(mensaje)))
            if valida(valor):
                break
            else:
                gotoxy(col, fil)
                print(" {} ".format(mensajeError), " "*20)
                time.sleep(1)
                gotoxy(col, fil);print(" "*100)
        return valor.upper()

    @staticmethod
    def solo_numeros(mensaje,mensajeError, col, fil):
        while True:
            gotoxy(col, fil)
            valor = input(mensaje)
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col, fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil);print(" "*20)
        return valor
    
    

#n= Validar.solo_numeros("numero: ", "Dato no valido!", 5,4)
# print(n)
#Validar.ingreso_fecha("Ingrese fecha dd-mm-aaaa :","error")
# numeroCedula = []  # creamos lista

# for digito in cedula1:  # para cada digito de cedula1 entonces agregalo a la lista
# numeroCedula.append(digito)
