from app.utils import validarNombre,validarEmail, ingresoDato,busquedaOBJ
from faker import Faker


def ingresoUsuario(legajo, liAlumnos):

    alumno = {
        'id': liAlumnos[len(liAlumnos)-1]['id']+1 if len(liAlumnos)  else 1,
        'legajo': legajo
    }

    indiceAlumno = busquedaOBJ(liAlumnos,'legajo',legajo)

    if indiceAlumno != -1:
        alumno = liAlumnos[indiceAlumno]

    else:
        mensajeNombre = "Indique su nombre: "
        nombre = ingresoDato(mensajeNombre)
        nombreValido = validarNombre(nombre)

        while (not nombreValido):
            nombre = ingresoDato(f"ERROR: Ingrese un nombre real: ")
            nombreValido = validarNombre(nombre)

        mensajeApellido = "Indique su apellido: "
        apellido = ingresoDato(mensajeApellido)
        apellidoValido = validarNombre(apellido)

        while (not apellidoValido):
            apellido = ingresoDato(f"ERROR: Ingrese un apellido real: ")
            apellidoValido = validarNombre(apellido)

        mensajeEmail = "Indique su email: "
        email = ingresoDato(mensajeEmail)
        emailValido = validarEmail(email)

        while(not emailValido):
            email = ingresoDato(f"ERROR: Ingrese un formato de email correcto: ")
            emailValido = validarEmail(email)

        alumno['nombre'] = nombre
        alumno['apellido'] = apellido
        alumno['email'] = email

        liAlumnos.append(alumno)

    return alumno


def ingresoUsuarioAutomatico(legajo, liAlumnos):

    fake = Faker("es_ES")

    alumno = {
        "id": liAlumnos[len(liAlumnos) - 1]["id"] + 1 if len(liAlumnos) else 1,
        "legajo": legajo,
    }

    indiceAlumno = busquedaOBJ(liAlumnos, "legajo", legajo)

    if indiceAlumno != -1:
        alumno = liAlumnos[indiceAlumno]

    else:
        mensajeNombre = "Indique su nombre: "
        nombre = fake.first_name()
        print(mensajeNombre, nombre)

        mensajeApellido = "Indique su apellido: "
        apellido = fake.last_name()
        print(mensajeApellido, apellido)

        mensajeEmail = "Indique su email: "
        email = f"{nombre}.{apellido}@gmail.com"
        print(mensajeEmail, email)

        alumno["nombre"] = nombre
        alumno["apellido"] = apellido
        alumno["email"] = email

        liAlumnos.append(alumno)

    return alumno
