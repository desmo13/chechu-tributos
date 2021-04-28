from tkinter import *
import time
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog

def acerca():
    messagebox.showinfo('Creadores','Programador: Mario Manuel Galdon Gonzalez\nTio que sufrio mas : Sergio I. Coello Díaz')
dia = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
def clicked():
    contenido = var_C.get()
    f = filedialog.asksaveasfile(initialfile =str(dia),title = "Guardar como",defaultextension=".txt", filetypes=[("Text file",".txt")])
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return

    #text2save = txt1.get(1.0, END) # starts from `1.0`, not `0.0`
    f.write(contenido)
    f.close() # `()` was missing.






#ventana
window = Tk()
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



#texto
lbl1 = Label(window, text="C")
lbl1.grid(column=0, row=0)

lbl2 =Label(window, text="Concepto Tributario")


#entrada de texto

txt1 = Entry(window,width=10,textvariable=var_C)
txt1.grid(column=1,row=0)

#entry = MaxLengthEntry(window, maxlength=10)
#entry.pack(side=LEFT)
#root.mainloop()

window.mainloop()

#archivos
