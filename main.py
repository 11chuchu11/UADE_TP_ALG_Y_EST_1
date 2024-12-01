from app.carga_operaciones import cargaOperaciones
from app.carga_turnos import cargaTurnos,cargaTurnosAutomatica
from app.generar_informes import generarInformes



def main():

    ops = []
    alumnos = []
    turnos = []
    
    cargaOperaciones(ops, 5)
    cargaTurnos(ops, alumnos, turnos)
    #cargaTurnosAutomatica(300,ops, alumnos, turnos,100)
    generarInformes(ops, alumnos, turnos)
    

if __name__ == "__main__":
    main()