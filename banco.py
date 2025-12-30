"""
Funciones de un banco
-Crear usuario
-Estado de cuenta
-Retiro de dinero
-Ingresar dinero
"""
import random 
def usuario ():
    datos = {
        "Nombre": None,
        "Apellido": None,
        "FechaNacimiento": None,
        "Celular": None,
        "CURP": None,
        "Ciudad": None
    }
    datos["Nombre"] = str(input("Ingresa el nombre: "))
    datos["Apellido"] = str(input("Ingresa primer apellido: "))
    datos["FechaNacimiento"] = int(input("Ingresa fecha de nacimiento ddmmaa: "))
    datos["Celular"]=int(input("Ingresa tu numero de celular: "))
    datos["CURP"]=str(input("Ingresa tu CURP: "))
    datos["Ciudad"]=str(input("Ingresa la Ciudad de nacimiento: "))
    print("********BIENVENIDO********")
    print("Nombre: ", datos["Nombre"])
    print("Apellido: ", datos["Apellido"])
    nombreUsuario = []
    nombreUsuario = datos["CURP"]
    print(nombreUsuario)
    print(type(nombreUsuario))
usuario ()

def estadoCuenta ():
    print("*******ESTADO DE CUENTA*******")

estadoCuenta()