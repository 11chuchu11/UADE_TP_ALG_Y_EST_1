from app.utils.validar_rango import validarRango
def ingresoDatoInt(minimo, maximo, mensajeIngreso):
    ingreso=input(mensajeIngreso)
    
    while(not ingreso.isdigit()):
        ingreso = input("ERROR: Ingrese un tipo de dato numerico: ")
        
    valor = int(ingreso)
    
    while validarRango(valor, minimo, maximo) == 0:
        ingreso = input('ERROR ' + mensajeIngreso)

        while (not ingreso.isdigit()):
            ingreso = input("ERROR: Ingrese un tipo de dato numerico: ")
            
        valor = int(ingreso)
    
    return valor
