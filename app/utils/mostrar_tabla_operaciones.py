def mostrarTablaOperaciones(liCod, liNom):
    print("CODIGO OPERACION\tNOMBRE OPERACION")
    for i, cod in enumerate(liCod):
        print(f"{cod}{' '*16}\t{liNom[i]}")