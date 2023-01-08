from abc import ABC,abstractmethod
from datetime import datetime, time
import time
class Persona(ABC):
    def __init__(self,nom,ced,tel,email):
         self.nombre = nom
         self.cedula = ced
         self.telefono = tel
         self.correo = email
    
    @abstractmethod 
    def mostrarPersona(self):
        pass

class Doctor(Persona):
    def __init__(self,nom,cedu,tele,mail,licen, area):
        super().__init__(nom,cedu,tele,mail)  
        self.licen = licen
        self.especialidad=area
                   
    def mostrarPersona(self):
        cuadro_doctor = [[f'Nombre: {self.nombre}', f'N° Reg. {self.licen}\n']]
        print("\nMÉDICO", "="*57)
        for row in cuadro_doctor:
            print("{: >10} {: >30} ".format(*row))


class Enfermera(Persona):
    def __init__(self,nom,ced,tel,mail):
        super().__init__(nom,ced,tel,mail)
    
    def mostrarPersona(self):
        print("ENFERMERA", "="*55)
        print(self.nombre, self.cedula, self.telefono, self.correo)
        
      
class Usuario(ABC): #interface
    
    @abstractmethod
    def mostrarPersona(self):
        pass
    @abstractmethod 
    def agendar():
        pass
      
class Paciente(Usuario):
    _hc=30274 
    def __init__(self, nom, ced, tel, mail, edad, peso, talla,sex, diagnostico):
        self.nombre = nom
        self.cedula = ced
        self.telefono = tel
        self.correo = mail
        Paciente._hc +=1
        self.hc=Paciente._hc
        self.edad=edad
        self.peso=peso
        self.talla=talla
        self.sex=sex
        self.diagnostico=diagnostico
         

    def mostrarPersona(self):
        cuadro_paciente = [[f'Nombre: {self.nombre}',f'Edad: {self.edad}', f'CI : {self.cedula} '], [
            f'Historia Clínica:{self.hc}',f'Sexo:{self.sex}',f'Cel: {self.telefono} ']]
        print ("PACIENTE","="*55)
        for row in cuadro_paciente:
            print("{: >20} {: >20} {: >20}".format(*row))
        print("Diagnóstico:", f'\npaciente que presenta un cuadro de {self.diagnostico} ')
     
     
    def agendar(self):
        citasProx=[]
        asig = input("Deseas agendar una proxima cita? (S/N):")
        while asig in ("S", "s"):
            especialidad = input("Ingrese la especialidad: ")
            fechaen= input("Ingrese la fecha   (aaaa-mm-dd): ")
            datetime.strptime(fechaen, '%Y-%m-%d')
            horaen= (input("Ingrese la hora(hh:mm): "))
            time.strptime(horaen, "%H:%M")
            citasProx.append([f'Cita en especialidad--{especialidad} para el {fechaen} en horario {horaen}']) 
            print("Usuario ha agendado con exito: \n ", citasProx)
            break
        else:
            print("-"*50)




if __name__ == '__main__':  
    print("________Personal_________")       
    medico = Doctor("Daniel Arismendi Torres","091422332","0912131415","da@gmail.com",2345,"general")
    
    enfermera= Enfermera("Damaris Zambrano", "0401459872", "0985274523", "dzambrano@medicenter.com")
    enfermo = Paciente("Leonel Messi C", "091422332", "0912131415", "da@gmail.com", 34, 60,170,"M", "nefritis ")
    medico.mostrarPersona()
    enfermera.mostrarPersona()
    enfermo.agendar()

      