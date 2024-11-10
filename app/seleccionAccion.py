from app.utils import ingresoDatoInt
def seleccionOperaciones(ops):
    pass
def seleccionTurnos(ops, alumnos, turnos):
    pass
def seleccionInformes(ops, alumnos, turnos):
    pass

def seleccionAccion(ops, alumnos, turnos):
    mensajeAccion = f"Seleccione una opción:\n 1. Operaciones\n 2. Turnos\n 3. Informes\n-1. Terminar Programa\n"
    accion = ingresoDatoInt(-1, 3,mensajeAccion)
    
    if (accion == 1):
        seleccionOperaciones(ops)
    elif(accion == 2):
        seleccionTurnos(ops,alumnos, turnos)
    elif(accion == 3):
        seleccionInformes(ops,alumnos, turnos)
    else:
        print('Programa Finalizado')
    

