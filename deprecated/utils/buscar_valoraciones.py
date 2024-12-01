def buscarMejorValoracion(liConformidad:list[list[int]]):
    mejorValoracion = -1
    i = 0


    while mejorValoracion != 3 and i < len(liConformidad):
        fila = liConformidad[i]
        
        for index, columna in enumerate(fila):
            if columna != -1:
                valoracionActual = index + 1  

                if mejorValoracion < valoracionActual:
                    mejorValoracion = valoracionActual
        i+=1

    return mejorValoracion

def buscarPeorValoracion(liConformidad):
    peorValoracion = -1
    i = 0

    while peorValoracion != 1 and i <len(liConformidad):
        print("MIRAAAA ACAAA: ", i, liConformidad)
        fila = liConformidad[i]
        
        for index, columna in enumerate(fila):
            if columna != -1:
                valoracionActual = index + 1  

                if peorValoracion == -1:
                    peorValoracion = valoracionActual
                elif peorValoracion != -1 and peorValoracion > valoracionActual:
                    peorValoracion = valoracionActual
        i+=1

    return peorValoracion