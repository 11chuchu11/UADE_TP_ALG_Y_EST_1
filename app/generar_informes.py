from app.utils import generarCSV
from app.informes import informeGeneral

def generarInformes(liOp, liAlumnos, liTurnos):
    try:

        informeGeneral(liOp, liAlumnos, liTurnos)
        tuplasTurnos = [(turno['id'], turno['idAlumno'], turno['puestoAtencion'], turno['conformidad'], turno['estado'], turno['idOperacion'], turno['fecha'], turno['hora'])  for turno in liTurnos]
        tuplasAlumnos = [ (alumno['id'], alumno['nombre'], alumno['apellido'], alumno['legajo'], alumno['email']) for alumno in liAlumnos]
        tuplasOperaciones = [ (op['id'],op['codigo'], op['nombre']) for op in liOp]
    
        generarCSV(tuplasAlumnos,'alumnos')
        generarCSV(tuplasTurnos,'turnos')
        generarCSV(tuplasOperaciones,'operaciones')
    
    except:
        print('Ocurrio un error al generar los informes')