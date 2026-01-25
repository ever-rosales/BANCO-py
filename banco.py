"""
Funciones de un banco
-Crear usuario
-Estado de cuenta
-Retiro de dinero
-Ingresar dinero
"""
import sqlite3
import random
import pandas as pd
Nombre= None
Apellido = None
FechaNacimiento = None
Celular = None
Curp = None
Ciudad = None
Contraseña = None
Monto = 0
NombreUsuario=None
def crear_conexion(): 
    global Nombre, Apellido, FechaNacimiento, Celular, Curp, Ciudad, Contraseña, Monto, NombreUsuario
    conexion = sqlite3.connect("sistema_bancario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            FechaNacimiento INTEGER,
            Celular INTEGER,
            Curp TEXT UNIQUE,
            Ciudad TEXT,
            NombreUsuario TEXT,
            Constraseña TEXT,
            Monto INTEGER
        )
    ''')
    conexion.commit()
    conexion.close()
"""
def usuario (): #Funcion que permite registrar un usuario con los valores establecidos
    global Nombre, Apellido, FechaNacimiento, Celular, Curp, Ciudad, Contraseña, Monto, NombreUsuario
    Nombre = input("Ingresa el nombre: ")
    Apellido = input("Ingresa el apellido: ")
    FechaNacimiento = input("Ingresa fecha de nacimiento ddmmaa: ")
    Celular=input("Ingresa numero de celular: ")
    Curp=input("Ingresa CURP: ")
    Ciudad=input("Ingresa tu ciudad de origen: ")
    #Creando nombre de usuario
    numero = random.randrange(100)
    valor = str(numero)
    NombreUsuario=Nombre+Apellido+valor
    Constraseña=input("Ingresa una contraseña: ")
    try:
        conexion= sqlite3.connect("sistema_bancario.db")
        cursor=conexion.cursor()
        sql='''INSERT INTO usuarios (Nombre, Apellido, FechaNacimiento, Celular, Curp, Ciudad, NombreUsuario, Constraseña, Monto) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        valores=(Nombre,Apellido,FechaNacimiento,Celular,Curp,Ciudad,NombreUsuario,Constraseña,Monto)
        cursor.execute(sql,valores)
        conexion.commit()
        print("****BIENVENIDO****")
        print("Usuario: ", NombreUsuario)
        print("*******")
    except sqlite3.IntegrityError:
        print("ERROR: El CURP ya está registrado...")
        print("La columna ya existe o hubo error")
    finally:
        conexion.close()
crear_conexion()
usuario()
"""
def estadoCuenta (): #Funcion que permite conocer el estado de cuenta del usuario
    conexion=sqlite3.connect("sistema_bancario.db")
    print("Ingresa los siguientes datos")
    nombreUsuario=input("Nombre de Usuario: ")
    contraseña=input("Contraseña: ")
    query="SELECT * FROM usuarios WHERE NombreUsuario=? AND Constraseña=?"
    parametros=(nombreUsuario, contraseña)
    df=pd.read_sql_query(query,conexion, params=parametros)
    if not df.empty:
        Nombre=df["Nombre"]
        Apellido=df["Apellido"]
        monto=df["monto"]
        print("Bienvenido {Nombre} {Apellido}")
    else:
        print("Usuario no encontrado")
    conexion.close()
estadoCuenta()
"""
def ingresarDinero (): 
    nombreUsuario=input("Ingresa tu nombre de usuario: ")
    Contraseña=input("Ingresa tu contraseña: ")
    if (nombreUsuario==nombreUsuario) and (Contraseña==Contraseña):
        print("Usuario: ", nombreUsuario)
        Monto=int(input("Ingresa el monto a tu cuenta: "))
        Monto+=Monto
        print("Monto disponible $", Monto)
    else:
        print("Usuario no encontrado")
ingresarDinero()


def retirarDinero():
    nombreUsuario=input("Ingresa tu nombre de usuario: ")
    Contraseña=input("Ingresa tu contraseña: ")
    if (nombreUsuario==nombreUsuario) and (Contraseña==Contraseña):
        print("Usuario: ", nombreUsuario)
        Monto=int(input("Ingresa el monto a retirar de tu cuenta: "))
        Monto-=Monto
        print("Monto disponible $", Monto)
    else:
        print("Usuario no encontrado")

retirarDinero()
"""