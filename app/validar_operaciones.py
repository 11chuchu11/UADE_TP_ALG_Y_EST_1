from app.utils import busquedaOBJ


def validarOperaciones(op, liOps):
    idOP = -1
    
    try:
        codigoOP = int(op)
        indiceOp = busquedaOBJ(liOps, 'codigo', codigoOP)
        
        if indiceOp != -1:
            idOP = liOps[indiceOp]['id']
            
    except:
        indiceOp = busquedaOBJ(liOps, 'nombre', op)
        if indiceOp != -1:
            idOP = liOps[indiceOp]['id']
            
    return idOP