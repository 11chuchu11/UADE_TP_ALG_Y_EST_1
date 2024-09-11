from app.utils import validarNombre,validarEmail, ingresoDato

def ingresoUsuario(legajo,liLegajos, liNombre,liEmail):
    
    if legajo in liLegajos:
        indiceLegajo = liLegajos.index(legajo)
        liNombre.append(liNombre[indiceLegajo])
        liEmail.append(liEmail[indiceLegajo])
    
    else:
        
        mensajeNombre = "Indique su nombre y apellido: "
        nombre = ingresoDato(mensajeNombre)
        nombreValido = validarNombre(nombre)
        while (not nombreValido):
            nombre = ingresoDato(f"ERROR: Ingrese un nombre real: ")
            nombreValido = validarNombre(nombre)
            
        liNombre.append(nombre)
        
        
        mensajeEmail = "Indique su email: "
        email = ingresoDato(mensajeEmail)
        emailValido = validarEmail(email)
        while(not emailValido):
            email = ingresoDato(f"ERROR: Ingrese un formato de email correcto: ")
            emailValido = validarEmail(email)
        
        liEmail.append(email)
        
    liLegajos.append(legajo)