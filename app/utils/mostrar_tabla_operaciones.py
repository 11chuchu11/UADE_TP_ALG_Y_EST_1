def mostrarTablaOperaciones(liOps):
    print("CODIGO OPERACION\tNOMBRE OPERACION")
    for op in liOps:
        print(f"{op['codigo']}{' '*16}\t{op['nombre'].capitalize()}")