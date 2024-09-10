from random import randint
from app.utils import ingresoDatoInt
from app.ingreso_usuario import ingresoUsuario
from app.ingreso_operacion import ingresoOperacion
from app.ingreso_conformidad_estado import ingresoConformidadYEstado

def cargaTurnos(liCodOp=[], liNomOp=[], liLegajos=[], liNombres=[], liEmails=[], liOperaciones=[], liPuestosAtencion=[], liConformidad=[], liEConsulta=[]):    
    mensajeLegajo = 'Ingrese un numero de legajo entre 11000 y 11999, 12000 para terminar: '
    print()
    legajo = ingresoDatoInt(11000,12000, mensajeLegajo)
    id = 0
    
    while legajo != 12000:
        
        ingresoUsuario(legajo,liLegajos,liNombres,liEmails)
        
        ingresoOperacion(liCodOp, liNomOp, liOperaciones)
        
        puestoAtencion = randint(1,5)
        print('Dirijase al puesto ', puestoAtencion)
        liPuestosAtencion.append(puestoAtencion)
        
        mensajeConformidad = "Del 1 al 3 que tan conforme esta con la atencion, siendo 1 inconforme, 2 regular y 3 conforme: "
        
        ingresoConformidadYEstado(id,liConformidad,mensajeConformidad)
        
        mensajeEstado = 'Siendo 1 No solucionado, 2 en revisión y 3 Solucionado cual es el estado de su consulta: '
        
        ingresoConformidadYEstado(id, liEConsulta, mensajeEstado )
        
        id += 1
        legajo = ingresoDatoInt(11000, 12000, mensajeLegajo)
        