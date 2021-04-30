from tkinter import *
import time
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *

def acerca():
    messagebox.showinfo('Creadores','Programador: Mario Manuel Galdon Gonzalez\nTio que sufrio mas : Sergio I. Coello Díaz')
dia = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
def clicked():
    contenido1 = Concepto_Tributario.get()
    contenido2 = Codigo_Entidad.get()
    contenido3 =  Ejercicio_Tributario.get()
    contenido4 = Periodo.get()
    contenido5 = Situacion_Concepto.get()
    contenido6 =Tipo_Valor.get()
    if len(contenido1)>12:
        messagebox.showerror("ERROR","El cocepto tributario no puede ser mayor a 12 caracteres")
    if len(contenido3)>5:
        messagebox.showerror("ERROR","EL Codigo de entidad no puede tener mas de 5 caracteres")
    if len(contenido2)>4:
        messagebox.showerror("ERROR","EL Ejercicio tributario no puede tener mas de 4 caracteres")
    if len(contenido4)>2:
        messagebox.showerror("ERROR","EL Periodo no puede ser mayor a 2")
    if contenido5==" ":
        messagebox.showerror("ERROR","Seleciona algo en el desplegable de Situacion concepto")
    if contenido6==" ":
         messagebox.showerror("ERROR","Seleciona algo en el desplegable de Tipo Valor")
    else:
        f = filedialog.asksaveasfile(initialfile =str(dia),title = "Guardar como",defaultextension=".txt", filetypes=[("Text file",".txt")])
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        #text2save = txt1.get(1.0, END) # starts from `1.0`, not `0.0`
        f.write()
        f.close() # `()` was missing.






#ventana
window = Tk()

ventanas =Notebook(window)

window.title("Chechu V1.4")

window.geometry("500x500")

#variables
Concepto_Tributario= StringVar()

Codigo_Entidad = StringVar()

Ejercicio_Tributario = StringVar()

Periodo = StringVar()

Situacion_Concepto = StringVar()

Tipo_Valor = StringVar()



#menu de arriba
menu = Menu(window)

new_item = Menu(menu,tearoff=0)

new_item.add_command(label='Guardar Como ',command=clicked)

new_item.add_command(label="Acerca De ",command=acerca)

menu.add_cascade(label='Menu', menu=new_item)

window.config(menu=menu)

#ventanas
vent1 = Frame(ventanas)
vent2 = Frame(ventanas)
vent3 = Frame(ventanas)
vent4 = Frame(ventanas)
vent5 = Frame(ventanas)
vent6 = Frame(ventanas)
vent7 = Frame(ventanas)
vent8 = Frame(ventanas)
vent9 = Frame(ventanas)
ventanas.add(vent1, text='Cabecera')
ventanas.add(vent2, text='Cuerpo')
ventanas.add(vent3, text='Cuerpo')
ventanas.add(vent4, text='Cuerpo')
ventanas.add(vent5, text='Cuerpo')
ventanas.add(vent6, text='Cuerpo')
ventanas.add(vent7, text='Cuerpo')
ventanas.add(vent8, text='Cuerpo')
ventanas.add(vent9, text='Cuerpo')
#desplegable de cabezera
desplegable= Combobox(vent1,textvariable=Situacion_Concepto)
desplegable2= Combobox(vent1,textvariable=Tipo_Valor)

#texto

lbl1 = Label(vent1, text="Concepto Tributario: ")
lbl1.grid(column=0, row=1)

lbl2 =Label(vent1, text="Codigo de Entidad: ")
lbl2.grid(column=2, row=1)

lbl3 =Label(vent1, text="Ejercicio tributario:")
lbl3.grid(column=4, row=1)

lbl4 =Label(vent1, text="Periodo: ")
lbl4.grid(column=6, row=1)

lbl5_desplegable =Label(vent1,text="Situacion conocidad:")
lbl5_desplegable.grid(column=0, row=2)

lbl6_desplegable =Label(vent1,text="Tipo Valor:")
lbl6_desplegable.grid(column=2, row=2)

#entrada de texto

txt1 = Entry(vent1,width=10,textvariable=Concepto_Tributario)
txt1.grid(column=1,row=1)

txt2 = Entry(vent1,width=10,textvariable=Codigo_Entidad)
txt2.grid(column=3,row=1)

txt3 = Entry(vent1,width=10,textvariable=Ejercicio_Tributario)
txt3.grid(column=5,row=1)

txt3 = Entry(vent1,width=10,textvariable=Periodo)
txt3.grid(column=7,row=1)
#desplegables

desplegable["values"]=("E","V","P")
desplegable.grid(column=1,row=2)

desplegable2["values"]=("R","L")
desplegable2.grid(column=3,row=2)

ventanas.grid(column=0,row=0)
window.mainloop()

#archivos