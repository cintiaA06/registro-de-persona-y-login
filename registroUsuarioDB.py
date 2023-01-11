import sqlite3
conexion= sqlite3.connect("registroUsuario.db")

cursor=conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        numeroRegistro INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        e_mail  VARCHAR(50) NOT NULL UNIQUE,
        usuario VARCHAR(50) NOT NULL, 
        password VARCHAR(50) NOT NULL,
        fechaNac VARCHAR(40) NOT NULL)""")

def guardarDatos(nombre, apellido,e_mail,usuario,password,fechaNac):
    cursor.execute("""INSERT INTO usuarios VALUES(NULL,?,?,?,?,?,?)""",( nombre,apellido,
    e_mail,usuario,password,fechaNac))
    
    conexion.commit()

def loginData (usuario, password):
        cursor.execute("SELECT * FROM  usuarios WHERE usuario=? AND password=?",(usuario,password))
        #cuando se coloca el ? es que va a tomar el valor que se le pasa despues de la coma 
        # en donde se le pasa las campos usuario y contraseña
        if cursor.fetchone() is not None:# trae un único valor (fetch one) busca el primer dato
                return True
        else:
                return False