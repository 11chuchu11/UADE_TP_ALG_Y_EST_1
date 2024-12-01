from random import randint
from app.utils import ingresoDatoInt, horaRandom,ingresoDatoIntAutomatico
from app.ingreso_usuario import ingresoUsuario, ingresoUsuarioAutomatico
from app.ingreso_operacion import ingresoOperacion, ingresoOperacionAutomatico
from datetime import datetime

def cargaTurnos(liOps, liAlumnos, liTurnos ):    

    fecha = datetime.now()
    mensajeConformidad = "Del 1 al 3 que tan conforme esta con la atencion, siendo 1 inconforme, 2 regular y 3 conforme: "
    mensajeEstado = 'Siendo 1 No solucionado, 2 en revisión y 3 Solucionado cual es el estado de su consulta: '
    legajo = ingresoDatoInt(11000,12000, 'Ingrese un numero de legajo entre 11000 y 11999, 12000 para terminar: ')

    while legajo != 12000:

        turno = {'id': liTurnos[-1]['id']+1 if len(liTurnos) else 1 }
        usuario = ingresoUsuario(legajo, liAlumnos)

        turno['idAlumno'] = usuario['id']
        idOperacion = ingresoOperacion(liOps)
        puestoAtencion = randint(1,5)
        print('Dirijase al puesto ', puestoAtencion)
        turno['puestoAtencion'] = puestoAtencion

        turno['conformidad'] = ingresoDatoInt(1,3, mensajeConformidad)
        turno['estado'] = ingresoDatoInt(1,3, mensajeEstado)
        turno['idOperacion'] = idOperacion
        turno['fecha'] = str(datetime.date(fecha))
        turno['hora'] = horaRandom(9,18)

        liTurnos.append(turno)
        legajo = ingresoDatoInt(11000, 12000, 'Ingrese un numero de legajo entre 11000 y 11999, 12000 para terminar: ')


def cargaTurnosAutomatica(
    cantidadTurnos, liOps, liAlumnos, liTurnos, cantidadLegajos=50
):

    fecha = datetime.now()
    mensajeConformidad = "Del 1 al 3 que tan conforme esta con la atencion, siendo 1 inconforme, 2 regular y 3 conforme: "
    mensajeEstado = "Siendo 1 No solucionado, 2 en revisión y 3 Solucionado cual es el estado de su consulta: "
    legajo = ingresoDatoIntAutomatico(
        11000,
        (11000+cantidadLegajos),
        "Ingrese un numero de legajo entre 11000 y 11999, 12000 para terminar: ",
    )

    for _ in range(cantidadTurnos):

        turno = {"id": liTurnos[-1]["id"] + 1 if len(liTurnos) else 1}
        usuario = ingresoUsuarioAutomatico(legajo, liAlumnos)

        turno["idAlumno"] = usuario["id"]
        idOperacion = ingresoOperacionAutomatico(liOps)
        puestoAtencion = randint(1, 5)
        print("Dirijase al puesto ", puestoAtencion)
        turno["puestoAtencion"] = puestoAtencion

        turno["conformidad"] = ingresoDatoIntAutomatico(1, 3, mensajeConformidad)
        turno["estado"] = ingresoDatoIntAutomatico(1, 3, mensajeEstado)
        turno["idOperacion"] = idOperacion
        turno["fecha"] = str(datetime.date(fecha))
        turno["hora"] = horaRandom(9, 18)

        liTurnos.append(turno)
        legajo = ingresoDatoIntAutomatico(
            11000,
            (11000+cantidadLegajos),
            "Ingrese un numero de legajo entre 11000 y 11999, 12000 para terminar: ",
        )
