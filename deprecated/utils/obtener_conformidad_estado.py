def obtenerConformidadYEstado(id, lista, listaMensajes):
    iColumna = 0
    mensaje = ""
    i=0
    longLista = len(lista)
    maximo = len(listaMensajes)-1
    while(i < longLista or mensaje == ""):
        fila = lista[i]

        for columna in fila:
            if columna != id:
                iColumna +=1
                
                if (iColumna > maximo):
                    iColumna=0
            
            else:
                mensaje = listaMensajes[iColumna]
        i+=1
    return mensaje