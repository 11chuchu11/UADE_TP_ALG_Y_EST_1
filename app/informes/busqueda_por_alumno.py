from app.utils import obtenerConformidadYEstado
from app.validar_alumno import validarAlumno
def busquedaPorAlumno(liCodOp, liNomOp, liLegajos, liNombres, liEmail, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta):
    mensajesConformidad = ["Inconforme", "Regular", "Conforme"]
    mensajesEstado = ["No Solucionado", "En Revisión", "Solucionado"]
    
    mensaje="Ingrese el legajo, nombre y apellido o email de un alumno"
    ingreso = input(f"{mensaje}: ").lower()
    
    ocurrencias = []
    validarAlumno(ingreso, liLegajos, liNombres, liEmail, ocurrencias)
        
    while not len(ocurrencias):
        ingreso = input(f"ERROR: {mensaje} existente: ").lower()
        validarAlumno(ingreso, liLegajos, liNombres, liEmail, ocurrencias)
        
    print("CANT. TRAMITES\t% SOLUCIONADOS\tCANT. SOLUCIONADOS\t% EN REVISION\tCANT. EN REVISION\t% NO SOLUCIONADOS\tCANT. NO SOLUCIONADOS")

    print(
        "%14s\t%20s\t%18s\t%13s\t%17s\t%17s\t%25s"
        %
        ("LEGAJO", "NOMBRE","P. ATENCION","CONFORMIDAD","ESTADO", "COD. OPERACION", "OPERACION"))
    for ocu in ocurrencias:
        
        op = liOperaciones[ocu]
        mensajeConf = obtenerConformidadYEstado(ocu,liConformidad, mensajesConformidad)
        mensajeEst = obtenerConformidadYEstado(ocu, liEConsulta, mensajesEstado)
        print("%14d\t%20s\t%18d\t%13s\t%17s\t%17d\t%25s" % (liLegajos[ocu], liNombres[ocu].title(),liPuestosAtencion[ocu], mensajeConf, mensajeEst, liCodOp[op], liNomOp[op].title()) )