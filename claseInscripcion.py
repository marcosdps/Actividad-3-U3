from clasePersona import Persona
from claseTallerCapacitacion import TallerCapacitacion

class Inscripcion:
    __fechaInscripcion: str
    __pago: bool
    __persona: object
    __taller: object

    def __init__(self, fechaInscripcion, pago, persona, taller):
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = bool(pago)
        self.__persona = persona
        self.__taller = taller

    def mostrarInscript(self):
        print(f"{self.__fechaInscripcion} {self.__pago}")
        print(self.__taller)
        print(self.__persona)

    def getTaller(self):
        return self.__taller
    
    def getPersona(self):
        return self.__persona

    def pagar(self):
        self.__pago = True
    
    def getFecha(self):
        return self.__fechaInscripcion
    
    def getPago(self):
        return self.__pago