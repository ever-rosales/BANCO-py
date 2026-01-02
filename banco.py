"""
Funciones de un banco
-Crear usuario
-Estado de cuenta
-Retiro de dinero
-Ingresar dinero
"""
import sqlite3
import random
def crear_conexion():
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
def usuario ():
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
        sql='''INSERT INTO usuarios (Nombre, Apellido, FechaNacimiento, Celular, Curp, Ciudad, NombreUsuario, Constraseña) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        valores=(Nombre,Apellido,FechaNacimiento,Celular,Curp,Ciudad,NombreUsuario,Constraseña)
        cursor.execute(sql,valores)
        #agregando una nueva columna
        cursor.execute("ALTER TABLE usuarios ADD COLUMN monto REAL DEFAULT 0.0")
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
def estadoCuenta ():
    nombreUsuario=input("Ingresa tu nombre de usuario: ")
    Contraseña=input("Ingresa tu contraseña: ")
    if (nombreUsuario==nombreUsuario) and (Contraseña==Contraseña):
        print("ESTADO DE CUENTA")
        print("Bienvenido ", nombreUsuario)


estadoCuenta()
"""