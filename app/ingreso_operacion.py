from app.utils import mostrarTablaOperaciones, ingresoDato
from app.validar_operaciones import validarOperaciones
def ingresoOperacion(liOps):
    mensajeOperacion = 'Elija una operacion: '
    mostrarTablaOperaciones(liOps)
    operacion = ingresoDato(mensajeOperacion)
        
    idOperacionSeleccionada = validarOperaciones(operacion, liOps)
        
    while idOperacionSeleccionada == -1:
        mostrarTablaOperaciones(liOps)        
        operacion = ingresoDato(f"ERROR: Elija una operacion disponible: ")
        idOperacionSeleccionada = validarOperaciones(operacion, liOps)
        
    return idOperacionSeleccionada