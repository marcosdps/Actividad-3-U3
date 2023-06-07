from clasePersona import Persona

class ManejadorPersona:
    
    def __init__(self):
        self.__listaPersona = []

    def agregarDatosPersona(self, nombre, direccion, dni):
        unaPersona = Persona(nombre, direccion, dni)
        self.__listaPersona.append(unaPersona)

    def consultarDeuda(self, dniBuscar, mInscripcion):
        i=0
        while i<len(self.__listaPersona) and self.__listaPersona[i].getDNI() != dniBuscar:
            i +=1
        if i < len(self.__listaPersona):
            mInscripcion.buscoMoroso(self.__listaPersona[i])
        