"""
Funciones de un banco
-Crear usuario
-Estado de cuenta
-Retiro de dinero
-Ingresar dinero
"""
import sqlite3
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
            Ciudad TEXT
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

    try:
        conexion= sqlite3.connect("sistema_bancario.db")
        cursor=conexion.cursor()
        sql='''INSERT INTO usuarios (Nombre, Apellido, FechaNacimiento, Celular, Curp, Ciudad) 
                VALUES (?, ?, ?, ?, ?, ?)'''
        valores=(Nombre,Apellido,FechaNacimiento,Celular,Curp,Ciudad)
        cursor.execute(sql,valores)
        conexion.commit()
        print("****BIENVENIDO****")
        print(Nombre, Apellido)
    except sqlite3.IntegrityError:
        print("ERROR: El CURP ya está registrado...")
    finally:
        conexion.close()
crear_conexion()
usuario ()
