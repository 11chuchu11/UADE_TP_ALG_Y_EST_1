def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos ==-1 and i <len(lista):
        if valorBuscado is lista[i]:
            pos=i
        i+=1
    return pos

def busquedaOBJ(lista,clave, valor):
    pos=-1
    i=0
    
    try:
        valorInt = int(valor)    
        while pos-1 and i < len(lista):
            if valorInt == lista[i][clave]:
                pos = i
            i+=1
    
    except:
        while pos-1 and i < len(lista):
            if valor.lower() == lista[i][clave].lower():
                pos = i
            i+=1
            
    return pos