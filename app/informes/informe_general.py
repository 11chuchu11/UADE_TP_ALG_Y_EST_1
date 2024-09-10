from app.utils import contarCantidadesLista, calcularPorcentaje, obtenerConformidadYEstado
def informeGeneral(liCodOp=[], liNomOp=[], liLegajos=[], liNombres=[], liOperaciones=[], liPuestosAtencion=[], liConformidad=[], liEConsulta=[]):
    cantidadTramites = len(liLegajos)
    
    liCantidadesConformidad = [0]*3
    liCantidadesEstado = [0]*3
    
    contarCantidadesLista(1,3,liConformidad, liCantidadesConformidad)
    contarCantidadesLista(1,3,liEConsulta, liCantidadesEstado)    
    
    liPorcentajesConformidad = []
    liPorcentajesEstado = []
    
    calcularPorcentaje(cantidadTramites, liCantidadesConformidad, liPorcentajesConformidad)
    calcularPorcentaje(cantidadTramites, liCantidadesEstado, liPorcentajesEstado)
    
    mensajesConformidad = ["Inconforme", "Regular", "Conforme"]
    mensajesEstado = ["No Solucionado", "En Revisión", "Solucionado"]
    
    print("-"*155)
    print("%75s" % 'INFORME GENERAL')
    print("-"*155)
    
    print("CANT. TRAMITES\t% SOLUCIONADOS\tCANT. SOLUCIONADOS\t% EN REVISION\tCANT. EN REVISION\t% NO SOLUCIONADOS\tCANT. NO SOLUCIONADOS")
    print("%14d\t%14d\t%18d\t%13d\t%17d\t%17d\t%21d" % (cantidadTramites, liPorcentajesEstado[2], liCantidadesEstado[2], liPorcentajesEstado[1], liCantidadesEstado[1], liPorcentajesEstado[0], liCantidadesEstado[0]))
    print("%14s\t%14s\t%18s\t%13s\t%17s\t%17s\t%21s" % ("CANT. TRAMITES","% CONFORMES","CANT. CONFORMES","% REGULAR","CANT. REGULAR","% INCONFORMES","CANT. INCONFORMES"))        
    print("%14d\t%14d\t%18d\t%13d\t%17d\t%17d\t%21d" % (cantidadTramites, liPorcentajesConformidad[2], liCantidadesConformidad[2], liPorcentajesConformidad[1], liCantidadesConformidad[1], liPorcentajesConformidad[0], liCantidadesConformidad[0]))
    print()
    print(
        "%14s\t%20s\t%18s\t%13s\t%17s\t%17s\t%25s"
        %
        ("LEGAJO", "NOMBRE","P. ATENCION","CONFORMIDAD","ESTADO", "COD. OPERACION", "OPERACION"))
    for i in range(len(liLegajos)):
        op = liOperaciones[i]
        mensajeConf = obtenerConformidadYEstado(i,liConformidad, mensajesConformidad)
        mensajeEst = obtenerConformidadYEstado(i, liEConsulta, mensajesEstado)
        print("%14d\t%20s\t%18d\t%13s\t%17s\t%17d\t%25s" % (liLegajos[i], liNombres[i].title(),liPuestosAtencion[i], mensajeConf, mensajeEst, liCodOp[op], liNomOp[op].title()) )