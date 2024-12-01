from random import choice
from app.utils import mostrarTablaOperaciones, ingresoDato
from app.validar_operaciones import validarOperaciones


def ingresoOperacion(liOps):
    mensajeOperacion = "Elija una operacion: "
    mostrarTablaOperaciones(liOps)
    operacion = ingresoDato(mensajeOperacion)

    idOperacionSeleccionada = validarOperaciones(operacion, liOps)

    while idOperacionSeleccionada == -1:
        mostrarTablaOperaciones(liOps)
        operacion = ingresoDato(f"ERROR: Elija una operacion disponible: ")
        idOperacionSeleccionada = validarOperaciones(operacion, liOps)

    return idOperacionSeleccionada


def ingresoOperacionAutomatico(liOps):
    
    ops = [
        "100",
        "baja de materias",
        "200",
        "becas y ayudas economicas",
        "300",
        "intercambios estudiantiles",
        "400",
        "inscripciones",
        "500",
        "otros",
    ]
    
    
    mensajeOperacion = "Elija una operacion: "
    mostrarTablaOperaciones(liOps)
    operacion = choice(ops)
    print(mensajeOperacion, operacion)

    idOperacionSeleccionada = validarOperaciones(operacion, liOps)

    return idOperacionSeleccionada
