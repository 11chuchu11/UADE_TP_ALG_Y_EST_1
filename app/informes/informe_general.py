from app.utils import contarCantidadesListas, calcularPorcentaje, busquedaOBJ
def informeGeneral(liOp, liAlumnos, liTurnos):
    cantidadTramites = len(liTurnos)
    

    
    cantidades = {
        'conformidad':[0]*3,
        'estado':[0]*3
    }
    
    contarCantidadesListas(liTurnos, cantidades) 
    
    porcentajes = {
        'conformidad':[0]*3,
        'estado':[0]*3
    }
    
    calcularPorcentaje(cantidadTramites, cantidades, porcentajes)
    
    
    mensajesConformidad = ["Inconforme", "Regular", "Conforme"]
    mensajesEstado = ["No Solucionado", "En Revisión", "Solucionado"]
    
    print("-"*155)
    print("%75s" % 'INFORME GENERAL')
    print("-"*155)
    
    print("CANT. TRAMITES\t% SOLUCIONADOS\tCANT. SOLUCIONADOS\t% EN REVISION\tCANT. EN REVISION\t% NO SOLUCIONADOS\tCANT. NO SOLUCIONADOS")
    print("%14d\t%14d\t%18d\t%13d\t%17d\t%17d\t%21d" % (cantidadTramites, porcentajes["estado"][2], cantidades["estado"][2], porcentajes['estado'][1], cantidades['estado'][1], porcentajes['estado'][0], cantidades['estado'][0]))
    print("%14s\t%14s\t%18s\t%13s\t%17s\t%17s\t%21s" % ("CANT. TRAMITES","% CONFORMES","CANT. CONFORMES","% REGULAR","CANT. REGULAR","% INCONFORMES","CANT. INCONFORMES"))        
    print("%14d\t%14d\t%18d\t%13d\t%17d\t%17d\t%21d" % (cantidadTramites, porcentajes['conformidad'][2], cantidades['conformidad'][2], porcentajes['conformidad'][1], cantidades['conformidad'][1], porcentajes['conformidad'][0], cantidades['conformidad'][0]))
    print()
    print(
        "%14s\t%20s\t%18s\t%13s\t%17s\t%17s\t%25s"
        %
        ("LEGAJO", "NOMBRE","P. ATENCION","CONFORMIDAD","ESTADO", "COD. OPERACION", "OPERACION"))
    
    for turno in liTurnos:
        
        alumno = liAlumnos[busquedaOBJ(liAlumnos, 'id', turno['idAlumno'])]
        legajo = alumno['legajo']
        nombreApellido = f'{alumno["nombre"]} {alumno["apellido"]}'.title()
        puestoAtencion = turno['puestoAtencion']
        
        
        op = liOp[busquedaOBJ(liOp, 'id', turno['idOperacion'])]
        print("%14d\t%20s\t%18d\t%13s\t%17s\t%17d\t%25s" % (legajo, nombreApellido, puestoAtencion, mensajesConformidad[turno['conformidad']-1], mensajesEstado[turno['estado']-1], op['codigo'], op['nombre'].title()) )