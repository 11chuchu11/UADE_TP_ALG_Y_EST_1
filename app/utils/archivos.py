from json import loads, dumps

def cargaCSV(path):
    resultado = []
    try:
        archivo = open(f'./files/{path}.csv', 'rt', encoding="utf-8")
        linea = archivo.readline()
        while linea: 
            linea = linea.replace('\n', '')
            tupla = tuple(linea.split(';'))
            resultado.append(tupla)
            linea = archivo.readline()
        
    except OSError as msg:
        print(f"Ocurrio un error al leer: {path}.csv\n{msg}")
    else:
        archivo.close()
    finally:
        return resultado

def cargaJSON(path):
    json = []
    try:
        archivo = open(f"./files/{path}.json", "rt", encoding="utf-8")
        lineas = archivo.read()
    except OSError as msg:
        print(f"Ocurrio un error al leer: {path}.json\n{msg}")
    else:
        archivo.close()
        json = loads(lineas)

    finally:
        return json

def generarCSV(arrTuplas, path):
    resultado = True
    try:
        archivo = open(f"./files/{path}.csv", "wt", encoding="utf-8")

        for e in arrTuplas:
            fila = ';'.join(str(elemento) for elemento in e) + '\n'
            archivo.write(fila)
    except OSError as msg:
        print(f'Ocurrio un error al crear: {path}.csv\n{msg}')
        resultado = False
    else:
        archivo.close()
    finally:
        return resultado

def generarJson(data, path):
    try:
        archivo = open(f"./files/{path}.json", "w", encoding="utf-8")
        jsonData = dumps(data, indent=4)
        archivo.write(jsonData)
    except OSError as msg:
        print(f'Ocurrio un error al crear: {path}.json\n{msg}')
    else:
        archivo.close()
