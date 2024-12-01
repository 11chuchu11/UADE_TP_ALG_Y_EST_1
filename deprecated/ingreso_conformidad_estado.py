from app.utils import ingresoDatoInt
def ingresoConformidadYEstado(id, lista, mensaje):
        
    valoracion = ingresoDatoInt(1,3, mensaje)
    if lista[-1][valoracion-1] == -1:
        lista[-1][valoracion-1:valoracion] = [id]
    else:
        nuevaFila = [-1]*3
        nuevaFila[valoracion-1:valoracion] = [id]
        lista.append(nuevaFila)