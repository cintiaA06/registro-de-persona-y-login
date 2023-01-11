import tkinter as tk 
import registroUsuarioDB
from tkinter import messagebox
import comprobacion
import sys
ventana=tk.Tk()
ventana.title("REGISTRO DE USUARIO")
ventana.geometry("450x350")
ventana['bg']="#E4FAFE"
##################################
lNombre=tk.Label(text="Nombre: ",bg="#E4FAFE", font="cooper")
lNombre.place(x=10,y=10)

cTNombre=tk.Entry()
cTNombre.place(x=10,y=32)

#####################################
lApellido=tk.Label(text="Apellido: ",bg="#E4FAFE",font="cooper")
lApellido.place(x=10,y=52)

cTApellido=tk.Entry()
cTApellido.place(x=10,y=72)

#####################################
lemail=tk.Label(text="e_mail: ",bg="#E4FAFE",font="cooper")
lemail.place(x=10,y=92)

cTemail=tk.Entry()
cTemail.place(x=10,y=112)

####################################
lUsuario=tk.Label(text="Usuario: ",bg="#E4FAFE",font="cooper")
lUsuario.place(x=10,y=132)

cTUsuario=tk.Entry()
cTUsuario.place(x=10,y=152)

####################################
lContra=tk.Label(text="Contraseña: ",bg="#E4FAFE",font="cooper")
lContra.place(x=10,y=172)

cTContra=tk.Entry(show="*")#show es para que no se vea la contraseña
cTContra.place(x=10,y=192)

###################################
lFechaNac=tk.Label(text="Fecha de Nacimiento: ",bg="#E4FAFE",font="cooper")
lFechaNac.place(x=10,y=212)

cTFechaNac=tk.Entry()
cTFechaNac.place(x=10,y=232)
#####################################
def guardar ():
    nombre=cTNombre.get()
    apellido= cTApellido.get()
    e_mail=cTemail.get()
    usuario=cTUsuario.get()
    password=cTContra.get()
    fechaNac=cTFechaNac.get()

    if comprobacion.nombreValidator(nombre):
        if comprobacion.dateValidator(fechaNac):
            if comprobacion.emailValidator(e_mail):
                    try:
                        registroUsuarioDB.guardarDatos(nombre,apellido,e_mail,usuario,password,fechaNac)
                        messagebox.showinfo("mensaje","usario registrado exitosamente")
                        limpiarFormulario()
                    except:
                        messagebox.showinfo("Lo siento", "El usuario no se ha podido registrar")
            else:
                messagebox.showinfo("tener en cuenta", "El correo eléctronico con formato incorrecto")
        else:
            messagebox.showinfo("", "fecha con formato incorrecto, el formato es(DD/MM/AAAA")                  
    else:
        messagebox.showinfo("Mensaje", "El nombre debe contener al menos 3 letras")   
        limpiarFormulario()
    sys.exit()

def limpiarFormulario():
    cTNombre.delete(0,tk.END)
    cTApellido.delete(0,tk.END)
    cTUsuario.delete(0,tk.END)
    cTemail.delete(0,tk.END)
    cTContra.delete(0,tk.END)
    cTFechaNac.delete(0,tk.END)
##########################################
btGuardar=tk.Button(text="GUARDAR", bg="#00ECC4",font="cooper", command=guardar)
btGuardar.place(x=30, y=292)

btCancelar=tk.Button(text="CANCELAR", bg="#FF3040",font="cooper",command= sys.exit)
btCancelar.place(x=160, y=292)


#################################################


tk.mainloop()