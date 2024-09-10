from app.carga_operaciones import cargaOperaciones
from app.carga_turnos import cargaTurnos
from app.generar_informes import generarInformes


def main():
    #codsPrueba = [100,200,300,400]
    #codnomPrueba = ["OP 1", "OP 2", "OP3", "op 4"]
    #legprueba=[11111, 11450,11345]
    #nomPrueba=["franco veron Peralta", "jose Angel Rivas", "facundo zacariaz" ]
    #emailPrueba = ["francoveronperalta@gmail.com", "facuzacariaz@gmail.com", "joseAngelRivas@gmail.com"]
    #operacionesPrueba=[0,2,1]
    #puestosAtencionPrueba=[1,2,3]
    #conformidadPrueba=[[0,1,2]]
    #estadoPrueba =[[0,1,2]]
    
    codOps = []
    nomOps = []
    legajos = []
    nombre = []
    email = []
    operaciones=[]
    puestosAtencion=[]
    liConformidad=[]
    liEstadoConsulta = []
    
    liConformidad.append([-1]*3)
    liEstadoConsulta.append([-1]*3)
    
    cargaOperaciones(codOps, nomOps, 5)
    cargaTurnos(codOps, nomOps,legajos, nombre, email, operaciones, puestosAtencion, liConformidad, liEstadoConsulta)
    generarInformes(codOps, nomOps,legajos, nombre, email, operaciones, puestosAtencion, liConformidad, liEstadoConsulta)
    
    #cargaTurnos(codsPrueba, nomPrueba,legajos, nombre, email, operaciones, puestosAtencion, liConformidad, liEstadoConsulta)
    #generarInformes(codsPrueba, codnomPrueba,legprueba, nomPrueba, emailPrueba, operacionesPrueba, puestosAtencionPrueba, conformidadPrueba, estadoPrueba)
    
if __name__ == "__main__":
    main()