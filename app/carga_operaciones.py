from app.utils import ingresoDatoInt

def cargaOperaciones(listaCod, listaNom, cantidadOperaciones):
    

    mensajeCod = "Ingrese un codigo de operacion entre 100 y 999: "
    mensajeNom = "Ingrese el nombre de la operacion: "
    
    while( len(listaCod) < cantidadOperaciones):
        numOp = ingresoDatoInt(100, 999, mensajeCod)
        
        while numOp in listaCod:
            numOp = ingresoDatoInt(100, 999, f"ERROR: Codigo ya ingresado, {mensajeCod.lower()}")
        
        listaCod.append(numOp)
        
        nombreOp = input(mensajeNom)
        nombreOp = nombreOp.lower()
        
        liNomNormalizada = [nombre.lower() for nombre in listaNom]
        while nombreOp in liNomNormalizada:
            nombreOp = input(f"ERROR: Operacion ya ingresada, {mensajeNom.lower()}").lower()
        
        listaNom.append(nombreOp)
        