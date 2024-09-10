from app.utils import validarNombre,validarEmail

def ingresoUsuario(legajo,liLegajos, liNombre,liEmail):
    
    if legajo in liLegajos:
        indiceLegajo = liLegajos.index(legajo)
        liNombre.append(liNombre[indiceLegajo])
        liEmail.append(liEmail[indiceLegajo])
    
    else:
        
        mensajeNombre = "Indique su nombre y apellido: "
        nombre = input(mensajeNombre)
        nombreValido = validarNombre(nombre)
        while (not nombreValido):
            nombre = input(f"ERROR: Ingrese un nombre real: ")
            nombreValido = validarNombre(nombre)
            
        liNombre.append(nombre)
        
        
        mensajeEmail = "Indique su email: "
        email = input(mensajeEmail)
        emailValido = validarEmail(email)
        while(not emailValido):
            email = input(f"ERROR: Ingrese un formato de email correcto: ")
            emailValido = validarEmail(email)
        
        liEmail.append(email)
        
    liLegajos.append(legajo)