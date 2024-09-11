from app.informes import informeGeneral, informePeorValoracion,informeMejorValoracion, busquedaPorAlumno
from app.utils import ingresoDatoInt
def generarInformes(liCodOp=[], liNomOp=[], liLegajos=[], liNombres=[], liEmail=[], liOperaciones=[], liPuestosAtencion=[], liConformidad=[], liEConsulta=[]):
    opcion = 5
    if len(liLegajos):
        informeGeneral(liCodOp, liNomOp, liLegajos, liNombres, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta)
        mensaje = 'SELECCIONE UNA OPCION: \n 0. INFORME GENERAL\n 1. INFORME DE TRAMITES CON LA MEJOR VALORACION DE CONFORMIDAD \n 2. INFORME DE TRAMITES CON LA PEOR VALORACION DE CONFORMIDAD \n 3. BUSQUEDA POR ALUMNO \n 4. TERMINAR PROGRAMA \nQue desea hacer: '
    
        while opcion != 4: 
            opcion = ingresoDatoInt(0,4, mensaje)
            if opcion == 0:
                informeGeneral(liCodOp, liNomOp, liLegajos, liNombres, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta)
            elif opcion == 1:
                informeMejorValoracion(liCodOp, liNomOp, liLegajos, liNombres, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta)
            elif opcion == 2:
                informePeorValoracion(liCodOp, liNomOp, liLegajos, liNombres, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta)
            elif opcion == 3:
                busquedaPorAlumno(liCodOp, liNomOp, liLegajos, liNombres, liEmail, liOperaciones, liPuestosAtencion, liConformidad, liEConsulta)