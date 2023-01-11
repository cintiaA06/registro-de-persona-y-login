import tkinter as tk 
import registroUsuarioDB
from tkinter import messagebox
import sys

ventana=tk.Tk()
ventana.title("LOGING DE USUARIO")
ventana.geometry("300x200")
ventana['bg']="cadetblue2"
##########################################
lUsuario=tk.Label(text="Usuario: ",bg="cadetblue2", font="cooper")
lUsuario.place(x=10,y=30)

cTUsuario=tk.Entry()
cTUsuario.place(x=10,y=50)
#########################################
lContra=tk.Label(text="Contraseña: ",bg="cadetblue2", font="cooper")
lContra.place(x=10,y=70)

cTContra=tk.Entry(show="*")#show es para que no se vea la contraseña
cTContra.place(x=10,y=90)

def limpiarFormulario():
    cTUsuario.delete(0,tk.END)
    cTContra.delete(0,tk.END)

def login ():
    usuario=cTUsuario.get()
    password=cTContra.get()

    if registroUsuarioDB.loginData(usuario,password):
        messagebox.showinfo("Mensaje", "Bienvenido a la plataforma")
    else:
        messagebox.showinfo("Mensaje","usuario o contraseña incorrecta")

    limpiarFormulario()
    sys.exit()






##################################
btLogin=tk.Button(text="Loging", bg="dodgerblue",fg="white", font="cooper", width="15", command= login)
btLogin.place(x=90, y=120)
##############################################

tk.mainloop()