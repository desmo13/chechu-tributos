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
    contenido = var_C.get()
    if len(contenido)>12:
        messagebox.showerror("ERROR","El cocepto tributario no puede ser mayor a 12 caracteres")
    else:
        f = filedialog.asksaveasfile(initialfile =str(dia),title = "Guardar como",defaultextension=".txt", filetypes=[("Text file",".txt")])
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        #text2save = txt1.get(1.0, END) # starts from `1.0`, not `0.0`
        f.write(contenido)
        f.close() # `()` was missing.






#ventana
window = Tk()

ventanas =Notebook(window)
var_C = StringVar()
window.title("Chechu V1.2")

window.geometry("500x500")



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

ventanas.add(vent1, text='Cabecera')
ventanas.add(vent2, text='Cuerpo')

#desplegable de cabezera
desplegable= Combobox(vent1)

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
lbl5_desplegable.grid(column=8, row=1)

#entrada de texto

txt1 = Entry(vent1,width=10,textvariable=var_C)
txt1.grid(column=1,row=1)

txt2 = Entry(vent1,width=10)
txt2.grid(column=3,row=1)

txt3 = Entry(vent1,width=10)
txt3.grid(column=5,row=1)

txt3 = Entry(vent1,width=10)
txt3.grid(column=7,row=1)
#desplegables

desplegable["values"]=("Ejecutiva","Voluntaria","Pruebas")
desplegable.grid(column=9,row=1)

ventanas.grid(column=0,row=0)
window.mainloop()

#archivos