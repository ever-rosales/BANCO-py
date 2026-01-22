"""
Funciones de un banco
-Crear usuario
-Estado de cuenta
-Retiro de dinero
-Ingresar dinero
"""
import sqlite3
import random
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
    global NombreUsuario,Contraseña,Monto
    nombre_usuario=input("Ingresa tu nombre de usuario: ")
    contraseña=input("Ingresa tu contraseña: ")
    #Conectar con los valores de la base de datos
    conexion=sqlite3.connect("sistema_bancario.db")
    cursor=conexion.cursor()
    #Lenguaje base de datos
    cursor.execute("SELECT NombreUsuario, Constraseña, monto FROM usuarios WHERE NombreUsuario = ?", (nombre_usuario,))
    resultado=cursor.fetchone()
    conexion.close()
    if resultado is not None:
        db_nombre=resultado[8]
        db_contraseña=resultado[8]
        if nombre_usuario==db_nombre and contraseña==db_contraseña:
            print("**BIENVENIDO**")
            print("Usuario: {db_nombre}")
            print("Saldo Disponbile:   {resultado[9]}")
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario no registrado")
        #opcion para registrar usuario
        respuesta=int(input("Deseas registrarte? 1.SI 2.NO "))
        """
        if respuesta==1:
            usuario()
        elif respuesta==2:
            print("Hasta luego")
        """
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