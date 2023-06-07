from manejadorPersona import ManejadorPersona
from manejadorInscripcion import ManejadorInscripcion
from manejadorTalleres import ManejadorTalleres
from clasePersona import Persona
from claseInscripcion import Inscripcion
from claseTallerCapacitacion import TallerCapacitacion

def testInscripcion():
    persona = Persona("Marcos", "25 de mayo","37741502")
    taller = TallerCapacitacion(2,"Taller de carpinteria",25,2500)
    unaInscripcion = Inscripcion("25/05/2023",True, persona, taller)



if __name__=="__main__":
    mPersona = ManejadorPersona()
    mInscripcion = ManejadorInscripcion()
    #testInscripcion()
    mTalleres = ManejadorTalleres()
    mTalleres.cargarDatos()
    
    interfaz = """\n---------MENU DE OPCIONES---------
    -1- Inscribir persona
    -2- Consultar deuda
    -3- Listar alumnos inscriptos en un taller
    -4- Registrar pago
    -5- Guardar datos
    -6- Mostrar datos de personas inscriptas
    -0- SALIR"""
    print(interfaz)
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                mTalleres.inscribirPersona(mPersona,mInscripcion)
            case 2:
                dniBuscar = input("Ingrese el DNI")
                mPersona.consultarDeuda(dniBuscar,mInscripcion)
            case 3: 
                mTalleres.mostrarDatos()
                idTallerBuscado = int(input("Ingrese el ID del taller: "))
                mInscripcion.listarAlumnosTaller(idTallerBuscado)
            case 4:
                dniBuscado = input("Ingrese DNI: ")
                mInscripcion.registrarPago(dniBuscado)
            case 5:
                mInscripcion.guardarDatos()
            case 6:
                mInscripcion.mostrarDatosInscrip()

        print(interfaz)
        opcion = int(input("Ingrese una opcion: "))