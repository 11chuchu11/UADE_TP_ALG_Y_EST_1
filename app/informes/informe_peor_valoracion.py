from app.utils import buscarPeorValoracion, obtenerConformidadYEstado

def informePeorValoracion(liCodOp, liNomOp, liLegajos, liNombres, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta):
    mensajesConformidad = ["Inconforme", "Regular", "Conforme"]
    mensajesEstado = ["No Solucionado", "En Revisión", "Solucionado"]
    peorValoracion = buscarPeorValoracion(liConformidad)

    
    idsPeorValorados = [fila[peorValoracion-1] for fila in liConformidad if fila[peorValoracion-1] != -1]
    
    print("-"*156)
    print("%94s" % 'INFORME TRAMITES PEOR VALORADOS')
    print("-"*156)
    
    print(
        "%14s\t%20s\t%18s\t%13s\t%17s\t%17s\t%25s"
        %
        ("LEGAJO", "NOMBRE","P. ATENCION","CONFORMIDAD","ESTADO", "COD. OPERACION", "OPERACION"))
    for id in idsPeorValorados:
        op = liOperaciones[id]
        mensajeConf = obtenerConformidadYEstado(id,liConformidad, mensajesConformidad)
        mensajeEst = obtenerConformidadYEstado(id, liEConsulta, mensajesEstado)
        print("%14d\t%20s\t%18d\t%13s\t%17s\t%17d\t%25s" % (liLegajos[id], liNombres[id].title(),liPuestosAtencion[id], mensajeConf, mensajeEst, liCodOp[op], liNomOp[op].title()) )