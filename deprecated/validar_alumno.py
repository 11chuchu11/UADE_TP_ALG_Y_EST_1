from app.utils import validarEmail
def validarAlumno(ingreso="", liLegajos=[], liNombres=[], liEmail=[], liOcurrencias=[]):
    liOcurrencias.clear()

    if ingreso.isdigit():
        legajo = int(ingreso)
        if legajo in liLegajos:
            liOcurrencias.extend([indice for indice, leg in enumerate(liLegajos) if leg == legajo])
    else:
        if validarEmail(ingreso):
            liEmailNormalizada = [e.lower() for e in liEmail]
            email = ingreso
            if email in liEmailNormalizada:
                liOcurrencias.extend([indice for indice, correo in enumerate(liEmailNormalizada) if correo == email])
        else:
            nombreYApellido = ingreso
            liNomNormalizada = [nomb.lower() for nomb in liNombres]
            if nombreYApellido in liNomNormalizada:
                liOcurrencias.extend([indice for indice, nomYAp in enumerate(liNomNormalizada) if nomYAp == nombreYApellido])