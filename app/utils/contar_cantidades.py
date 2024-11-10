def contarCantidadesListas(liTurnos, listaCantidades):
    for turno in liTurnos:
        conformidad = turno['conformidad']
        estado = turno['estado']
        listaCantidades['conformidad'][conformidad-1] = listaCantidades['conformidad'][conformidad-1]+1
        listaCantidades['estado'][estado-1] = listaCantidades['estado'][estado-1]+1
            