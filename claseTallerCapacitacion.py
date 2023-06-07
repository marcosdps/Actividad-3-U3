

class TallerCapacitacion:
    __idTaller: int
    __nombre: str
    __vacantes: int
    __montoInscripcion: float
    __inscripciones: list

    def __init__(self, idTaller = None, nombre = None, vacantes = None, montoInscripcion = None):
        self.__idTaller = int(idTaller)
        self.__nombre = nombre
        self.__vacantes = int(vacantes)
        self.__montoInscripcion = float(montoInscripcion)
        self.__inscripciones = []

    def __str__(self):
        return f"{self.__idTaller} {self.__nombre} {self.__vacantes} {self.__montoInscripcion}"
    
    def getID(self):
        return self.__idTaller
    
    def getVacantes(self):
        return self.__vacantes
    
    def modificarVacante(self):
        self.__vacantes -=1

    def mostrarDatosMoroso(self):
        print(f"{self.__nombre} //// Monto Adeudado: {self.__montoInscripcion}")