from app.utils import mostrarTablaOperaciones
from app.validar_operaciones import validarOperaciones
def ingresoOperacion(liCodOp,liNomOp, liOperaciones):
    mensajeOperacion = 'Elija una operacion: '
    mostrarTablaOperaciones(liCodOp,liNomOp)
    operacion = input(mensajeOperacion)
        
    indiceOperacionSeleccionada = validarOperaciones(operacion, liCodOp, liNomOp)
        
    while indiceOperacionSeleccionada == -1:
        mostrarTablaOperaciones(liCodOp, liNomOp)
        operacion = input(f"ERROR: Elija una operacion disponible: ")
        indiceOperacionSeleccionada = validarOperaciones(operacion, liCodOp, liNomOp)
        
    liOperaciones.append(indiceOperacionSeleccionada)