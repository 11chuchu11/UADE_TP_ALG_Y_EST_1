def validarRango(valor, minimo, maximo):
    valido = 1
    if valor < minimo or valor > maximo:
        valido = 0
    return valido
