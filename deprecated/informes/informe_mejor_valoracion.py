from app.utils import buscarMejorValoracion, obtenerConformidadYEstado

def informeMejorValoracion(liCodOp, liNomOp, liLegajos, liNombres, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta):
    mensajesConformidad = ["Inconforme", "Regular", "Conforme"]
    mensajesEstado = ["No Solucionado", "En Revisión", "Solucionado"]
    mejorValoracion = buscarMejorValoracion(liConformidad)
    
    idsMejorValorados = [fila[mejorValoracion-1] for fila in liConformidad if fila[mejorValoracion-1] != -1]
    
    print("-"*156)
    print("%94s" % 'INFORME TRAMITES MEJOR VALORADOS')
    print("-"*156)
    
    print(
        "%14s\t%20s\t%18s\t%13s\t%17s\t%17s\t%25s"
        %
        ("LEGAJO", "NOMBRE","P. ATENCION","CONFORMIDAD","ESTADO", "COD. OPERACION", "OPERACION"))
    for id in idsMejorValorados:
        op = liOperaciones[id]
        mensajeConf = obtenerConformidadYEstado(id,liConformidad, mensajesConformidad)
        mensajeEst = obtenerConformidadYEstado(id, liEConsulta, mensajesEstado)
        print("%14d\t%20s\t%18d\t%13s\t%17s\t%17d\t%25s" % (liLegajos[id], liNombres[id].title(),liPuestosAtencion[id], mensajeConf, mensajeEst, liCodOp[op], liNomOp[op].title()) )