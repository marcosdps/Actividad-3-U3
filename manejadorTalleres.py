from claseTallerCapacitacion import TallerCapacitacion
from clasePersona import Persona
import csv

class ManejadorTalleres:

    def __init__(self):
        self.__listaTalleres = []

    def cargarDatos(self):
        with open("talleres.csv", "r")as archi:
            reader = csv.reader(archi, delimiter=";")
            reader.__next__()
            for fila in reader:
                print(fila)
                self.__listaTalleres.append(TallerCapacitacion(*fila))
    
    def mostrarDatos(self):
        for i in range(len(self.__listaTalleres)):
            print(self.__listaTalleres[i])

    
    def inscribirPersona(self,mPersona, mInscripcion):
        print("Lista de Talleres")
        self.mostrarDatos()
        i=0
        idTaller = int(input("ID del taller a inscribir: "))
        while i<len(self.__listaTalleres) and self.__listaTalleres[i].getID() != idTaller:
            i +=1
        if i<len(self.__listaTalleres):
            if self.__listaTalleres[i].getVacantes()>0:
                self.__listaTalleres[i].modificarVacante()
                nombre = input("Ingrese el nombre: ")
                direccion = input("Ingrese la direccion: ")
                dni = input("Ingrese el DNI: ")
                mPersona.agregarDatosPersona(nombre, direccion, dni)
                persona = Persona(nombre, direccion, dni)
                mInscripcion.ingresoDatosInscripcion(self.__listaTalleres[i],persona )
        
