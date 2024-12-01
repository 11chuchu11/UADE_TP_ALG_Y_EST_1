from app.utils.validaciones_regex import validarEntero
from app.utils.validar_rango import validarRango
from random import randint
def ingresoDatoInt(minimo, maximo, mensajeIngreso):
    try:
        
        ingreso=input(mensajeIngreso)

        while(not validarEntero(ingreso)):
            ingreso = input("ERROR: Ingrese un tipo de dato numerico: ")

        valor = int(ingreso)

        while validarRango(valor, minimo, maximo) == 0:
            ingreso = input('ERROR ' + mensajeIngreso)

            while (not validarEntero(ingreso)):
                ingreso = input("ERROR: Ingrese un tipo de dato numerico: ")

            valor = int(ingreso)
        return valor
    except: 
        print('Ocurrio un error al ingresar el numero entero')


ingresoDato = lambda mensaje : input(mensaje).lower()


def ingresoDatoIntAutomatico(minimo, maximo, mensajeIngreso):
    dato = randint(minimo, maximo)
    
    print(f"{mensajeIngreso} {dato}")
    
    return dato
