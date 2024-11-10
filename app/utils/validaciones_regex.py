from re import match
from app.utils.expresiones_regulares import regexNombre, regexEmail, regexEnteros

def validarNombre(nombre):
    return match(regexNombre, nombre)

def validarEmail(email):
    return match(regexEmail, email)

def validarEntero(numero):
    return match(regexEnteros, numero)