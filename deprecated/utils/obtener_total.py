def obtenerTotal(lista):
    contador = 0
    for fila in lista:
        for columna in fila:
            if columna != -1:
                contador += 1
    
    return contador