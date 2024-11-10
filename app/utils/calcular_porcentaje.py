def calcularPorcentaje(total, cantidades, porcentajes):

    for i in range(len(cantidades['conformidad'])):
        porcentajes['conformidad'][i] = cantidades['conformidad'][i]/total*100
        porcentajes['estado'][i] = cantidades['estado'][i]/total*100