

class Persona:
    __nombre: str
    __direccion: str
    __dni: str
    
    def __init__(self, nombre = None, direccion = None, dni = None):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni


    def __str__(self):
        return f"{self.__nombre} {self.__direccion} {self.__dni}"
    
    def getDNI(self):
        return self.__dni
    
    def __ne__(self, otro):
        bandera = False
        if self.__nombre != otro.__nombre and self.__direccion != otro.__direccion and self.__dni != otro.__dni:
            bandera = True
        return bandera