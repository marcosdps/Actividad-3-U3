from claseInscripcion import Inscripcion
import csv

class ManejadorInscripcion:

    def __init__(self):
        self.__listaInscripcion = []

    def ingresoDatosInscripcion(self, taller, persona):
        pago = False
        fecha = input("Ingrese fecha de inscripcion: ")
        if int(input("Desea abonar? Si(1)/No(0): "))==1:
            pago = True
        self.__listaInscripcion.append(Inscripcion(fecha,pago,persona,taller))
        
    def mostrarDatosInscrip(self):
        for i in range(len(self.__listaInscripcion)):
            self.__listaInscripcion[i].mostrarInscript()

    def buscoMoroso(self, persona):
        i=0
        while i<len(self.__listaInscripcion) and  self.__listaInscripcion[i].getPersona() != persona:
            i +=1
        if i<len(self.__listaInscripcion):
            taller = self.__listaInscripcion[i].getTaller()
            taller.mostrarDatosMoroso()

    def listarAlumnosTaller(self, idTallerBuscado):
        for i in range(len(self.__listaInscripcion)):
            taller = self.__listaInscripcion[i].getTaller()
            if taller.getID() == idTallerBuscado:
                print(self.__listaInscripcion[i].getPersona())

    def registrarPago(self, dniBuscado):
        i=0
        bandera = False
        while i<len(self.__listaInscripcion) and bandera == False:
            persona = self.__listaInscripcion[i].getPersona()
            if dniBuscado == persona.getDNI():
                self.__listaInscripcion[i].pagar()
                bandera = True
            i +=1

    def guardarDatos(self):
        with open("registroDatos.csv", "w")as archi:
            writer = csv.writer(archi, delimiter=";")
            for i in range(len(self.__listaInscripcion)):
                unaPersona = self.__listaInscripcion[i].getPersona()
                dniAguardar = unaPersona.getDNI()
                unTaller = self.__listaInscripcion[i].getTaller()
                idTallerAguardar = unTaller.getID()
                fechaInscripcionAguardar = self.__listaInscripcion[i].getFecha()
                pagoAguardar = self.__listaInscripcion[i].getPago()
                writer.writerow([dniAguardar,idTallerAguardar,fechaInscripcionAguardar,pagoAguardar])







