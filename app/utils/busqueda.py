def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos ==-1 and i <len(lista):
        if valorBuscado is lista[i]:
            pos=i
        i+=1
    return pos