from tkinter import *
import time
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *

def espacios(contenido, max):
    contenido 
    espacio = "."
    if  len(contenido)<max:
        for i in range(max - len(contenido)):
            contenido  =  contenido + espacio 
        print(contenido)
    return contenido

espacios("hola",11)
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
    contenido7 =MunicipioIne.get()
    if len(contenido1)>12:
        messagebox.showerror("ERROR","El cocepto tributario no puede ser mayor a 12 caracteres")
    if len(contenido2)>5:
        messagebox.showerror("ERROR","EL Codigo de entidad no puede tener mas de 5 caracteres")
    if len(contenido3)>4:
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
        f.write("C"+ espacios(contenido1,12)+espacios(contenido2,5)+espacios(contenido3,4)+espacios(contenido4,2)+contenido5+contenido6+espacios("",308))
        f.write("\nhola")
        f.close() # `()` was missing.






#ventana
window = Tk()

ventanas =Notebook(window)

window.title("Chechu V1.6")

window.geometry("500x500")

#variables
Concepto_Tributario= StringVar()

Codigo_Entidad = StringVar()

Ejercicio_Tributario = StringVar()

Periodo = StringVar()

Situacion_Concepto = StringVar()

Tipo_Valor = StringVar()

MunicipioIne =StringVar()


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

lbl7_individual = Label(vent2,text="Municipio INE")
lbl7_individual.grid(column=0,row=1)

lbl8_individual = Label(vent2,text="Primera referencia")
lbl8_individual.grid(column=2,row=1)

lbl9_individual = Label(vent2,text="Numero de Cargo")
lbl9_individual.grid(column=4,row=1)

lbl10_individual = Label(vent2,text="Objeto tributario")
lbl10_individual.grid(column=6,row=1)

lbl11_individual = Label(vent2,text="Codigo de Tercero")
lbl11_individual.grid(column=8,row=1)

lbl12_individual = Label(vent2,text="Tipo de Documento )
lbl12_individual.grid(column=10,row=1)

lbl13_individual = Label(vent2,text="Identificador")
lbl13_individual.grid(column=12,row=1)

lbl14_individual = Label(vent2,text="Tipo de persona")
lbl14_individual.grid(column=14,row=1)

lbl15_individual = Label(vent2,text="Identificador normalizado")
lbl15_individual.grid(column=16,row=1)

lbl16_individual = Label(vent2,text="1º Apellido")
lbl16_individual.grid(column=18,row=1)

lbl17_individual = Label(vent2,text="2º Apellido")
lbl17_individual.grid(column=20,row=1)

lbl18_individual = Label(vent2,text="Particula Apellido")
lbl18_individual.grid(column=22,row=1)

lbl19_individual = Label(vent2,text="Nombre")
lbl19_individual.grid(column=24,row=1)

lbl20_individual = Label(vent2,text="Codigo postal")
lbl20_individual.grid(column=26,row=1)

lbl21_individual = Label(vent2,text="Codigo postal")
lbl21_individual.grid(column=28,row=1)

lbl22_individual = Label(vent2,text="Identificador Callejero")
lbl22_individual.grid(column=30,row=1)

lbl23_individual = Label(vent2,text="Codigo de via")
lbl23_individual.grid(column=32,row=1)

lbl24_individual = Label(vent2,text="Tipo de via")
lbl24_individual.grid(column=34,row=1)

lbl25_individual = Label(vent2,text="Nombre de via")
lbl25_individual.grid(column=36,row=1)

lbl26_individual = Label(vent2,text="Numero")
lbl26_individual.grid(column=38,row=1)

lbl27_individual = Label(vent2,text="Letra de Numero")
lbl27_individual.grid(column=40,row=1)

lbl28_individual = Label(vent2,text="Kilometro")
lbl28_individual.grid(column=42,row=1)

lbl29_individual = Label(vent2,text="Bloque")
lbl29_individual.grid(column=44,row=1)

lbl30_individual = Label(vent2,text="Escalera")
lbl30_individual.grid(column=46,row=1)

lbl31_individual = Label(vent2,text="Planta")
lbl31_individual.grid(column=48,row=1)

lbl32_individual = Label(vent2,text="Puerta")
lbl32_individual.grid(column=50,row=1)

lbl33_individual = Label(vent2,text="Otra informacion de la direccion")
lbl33_individual.grid(column=52,row=1)

lbl33_individual = Label(vent2,text="Importe en €")
lbl33_individual.grid(column=52,row=1)
#entrada de texto

txt1 = Entry(vent1,width=10,textvariable=Concepto_Tributario)
txt1.grid(column=1,row=1)

txt2 = Entry(vent1,width=10,textvariable=Codigo_Entidad)
txt2.grid(column=3,row=1)

txt3 = Entry(vent1,width=10,textvariable=Ejercicio_Tributario)
txt3.grid(column=5,row=1)

txt3 = Entry(vent1,width=10,textvariable=Periodo)
txt3.grid(column=7,row=1)

txt4_individual = Entry(vent2,width=10,textvariable=MunicipioIne)
txt4_individual.grid(column=1,row=1)

txt5_individual = Entry(vent2,width=10,textvariable=)
txt5_individual.grid(column=3,row=1)

txt6_individual = Entry(vent2,width=10,textvariable=)
txt6_individual.grid(column=5,row=1)

txt7_individual = Entry(vent2,width=10,textvariable=)
txt7_individual.grid(column=7,row=1)

txt8_individual = Entry(vent2,width=10,textvariable=)
txt8_individual.grid(column=9,row=1)

txt9_individual = Entry(vent2,width=10,textvariable=)
txt9_individual.grid(column=11,row=1)

txt10_individual = Entry(vent2,width=10,textvariable=)
txt10_individual.grid(column=13,row=1)
#desplegables

desplegable["values"]=("E","V","P")
desplegable.grid(column=1,row=2)

desplegable2["values"]=("R","L")
desplegable2.grid(column=3,row=2)

ventanas.grid(column=0,row=0)
window.mainloop()

#archivos
