def calcularPorcentaje(total, listaCantidades, lista):
    for cantidad in listaCantidades:
        lista.append((cantidad/total)*100)