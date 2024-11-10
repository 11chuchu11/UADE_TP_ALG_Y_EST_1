from app.carga_operaciones import cargaOperaciones
from app.carga_turnos import cargaTurnos
from app.generar_informes import generarInformes



def main():

    ops = []
    alumnos = []
    turnos = []
    
    cargaOperaciones(ops, 5)
    cargaTurnos(ops, alumnos, turnos)
    generarInformes(ops, alumnos, turnos)
    

if __name__ == "__main__":
    main()