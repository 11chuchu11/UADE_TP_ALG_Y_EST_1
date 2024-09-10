def validarOperaciones(op, liCod,liNom):
    liNomNormalizada = [nom.lower() for nom in liNom]
    indiceOp = -1
    
    if op.isdigit():
        if int(op) in liCod:
            indiceOp = liCod.index(int(op))
    else:
        if op.lower() in liNomNormalizada:
            indiceOp = liNomNormalizada.index(op.lower())
    
    return indiceOp