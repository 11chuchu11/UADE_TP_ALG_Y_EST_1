def contarCantidadesLista(valorMinimo, valorMaximo, listaBase, lista):
    valorAContar = valorMinimo
    for fila in listaBase:
        for columna in fila:
            if columna != -1:
                lista[valorAContar-1] = lista[valorAContar-1] + 1
            
            valorAContar +=1
            if valorAContar > valorMaximo:
                valorAContar = valorMinimo
            