from app.utils import ingresoDatoInt, ingresoDato,cargaJSON, busquedaOBJ, generarJson

def cargaOperacionesManual(ops,cantidadOperaciones):
    mensajeCod = "Ingrese un codigo de operacion entre 100 y 999: "
    mensajeNom = "Ingrese el nombre de la operacion: "
    if len(ops) < cantidadOperaciones:
        op ={'id':len(ops)+1}
        codigoOP = ingresoDatoInt(100,999, mensajeCod)
        
        while busquedaOBJ(ops, 'codigo', codigoOP) != -1:
            codigoOP = ingresoDatoInt(100, 999, f"ERROR: Codigo ya ingresado, {mensajeCod.lower()}")
        
        op['codigo'] = codigoOP
        
        nombreOP = ingresoDato(mensajeNom)
        
        while busquedaOBJ(ops, 'nombre', nombreOP)!=-1:
            nombreOP = ingresoDato(f"ERROR: Operacion ya ingresada, {mensajeNom.lower()}")
            
        op['nombre'] = nombreOP
        
        ops.append(op)
        cargaOperacionesManual(ops,cantidadOperaciones)

def cargaOperaciones(ops, cantidadOperaciones):
    
    pathArchivoOperaciones = 'operaciones'
    operaciones = cargaJSON(pathArchivoOperaciones)    
    
    if  len(operaciones) != cantidadOperaciones:
        
        operaciones.clear()
        cargaOperacionesManual(operaciones,cantidadOperaciones)
        generarJson(operaciones, pathArchivoOperaciones)
    
    for op in operaciones:
        ops.append(op)