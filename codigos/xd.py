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

def numeros_espacios(contenido, max):
    contenido 
    espacio = "0"
    if  len(contenido)<max:
        for i in range(max - len(contenido)):
            contenido  = espacio +  contenido 
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
    contenido8 = Primera_Referencia.get()
    contenido9 =  Numero_Cargo.get()
    contenido10 = Objeto_tributario.get()
    contenido11 = Codigo_Tercero.get()
    contenido12 = Tipo_Documento.get()
    contenido13 = Identificador.get()
    contenido14 = Tipo_Persona.get()
    contenido15 = Identificador_Normalizado.get()
    contenido16 = Apellido_1.get()
    contenido17 = Apellido_2.get()
    contenido18 = Particula_Apellido_1.get()
    contenido19 =  Particula_Apellido_2.get()
    contenido20 = Nombre.get()
    contenido21 =Codigo_Postal.get()
    contenido22 =  Identificador_Callejero.get()
    contenido23 = Codigo_Via.get()
    contenido24 = Tipo_Via.get()
    contenido25 =Nombre_Via.get()
    contenido26 = Numero.get()
    contenido27 = Letra_Numero.get()
    contenido28 = Kilometro.get()
    contenido29 = Bloque.get()
    contenido30 = Escalera.get()
    contenido31 = Planta.get()
    contenido32 = Puerta.get()
    contenido33 = Otra_Informacion_direccion.get()
    contenido34 =Importe_Euros.get()
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
        f.write("\nI"+espacios(contenido7,5)+espacios("",8)+espacios(contenido8,24)+espacios(contenido9,15)+espacios("",1)+espacios(contenido10,24)+espacios(contenido11,12)+numeros_espacios(contenido12,1)+espacios(contenido13,20)+espacios(contenido14,1)+espacios(contenido15,1)+espacios(contenido16,25)+espacios(contenido17,25)+espacios(contenido18,6)+espacios(contenido19,6)+espacios(contenido20,20)+numeros_espacios(contenido21,5)+espacios(contenido22,1)+numeros_espacios(contenido23,5)+espacios(contenido24,5)+espacios(contenido25,50)+numeros_espacios(contenido26,4)+espacios(contenido27,1)+numeros_espacios(contenido28,5)+espacios(contenido29,2)+espacios(contenido30,2)+espacios(contenido31,3)+espacios(contenido32,4)+espacios(contenido33,40)+numeros_espacios(contenido34,12))
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
MunicipioIne = StringVar()
Primera_Referencia = StringVar()
Objeto_tributario = StringVar()
Numero_Cargo = StringVar()
Codigo_Tercero = StringVar()
Tipo_Documento = StringVar()
Identificador = StringVar()
Tipo_Persona = StringVar()
Identificador_Normalizado = StringVar()
Apellido_1 = StringVar()
Apellido_2 = StringVar()
Particula_Apellido_1 = StringVar()
Particula_Apellido_2 =StringVar()
Nombre = StringVar()
Codigo_Postal = StringVar()
Identificador_Callejero = StringVar()
Codigo_Via = StringVar()
Tipo_Via = StringVar()
Nombre_Via = StringVar()
Letra_Numero = StringVar()
Kilometro = StringVar()
Bloque = StringVar()
Escalera = StringVar()
Planta = StringVar()
Puerta = StringVar()
Otra_Informacion_direccion = StringVar()
Importe_Euros = StringVar() 
Numero = StringVar()
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
desplegable3= Combobox(vent2,textvariable=Identificador_Normalizado)
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

lbl12_individual = Label(vent2,text="Tipo de Documento" )
lbl12_individual.grid(column=0,row=2)

lbl13_individual = Label(vent2,text="Identificador")
lbl13_individual.grid(column=2,row=2)

lbl14_individual = Label(vent2,text="Tipo de persona")
lbl14_individual.grid(column=4,row=2)

lbl15_individual = Label(vent2,text="Identificador normalizado")
lbl15_individual.grid(column=6,row=2)

lbl16_individual = Label(vent2,text="1º Apellido")
lbl16_individual.grid(column=8,row=2)

lbl17_individual = Label(vent2,text="2º Apellido")
lbl17_individual.grid(column=0,row=3)

lbl18_individual = Label(vent2,text=" 1º Apellido Particula")
lbl18_individual.grid(column=2,row=3)

lbl19_individual = Label(vent2,text=" 2º Apellido Particula")
lbl19_individual.grid(column=4,row=3)

lbl20_individual = Label(vent2,text="Nombre")
lbl20_individual.grid(column=6,row=3)

lbl21_individual = Label(vent2,text="Codigo postal")
lbl21_individual.grid(column=8,row=3)

lbl22_individual = Label(vent2,text="Codigo postal")
lbl22_individual.grid(column=0,row=4)

lbl23_individual = Label(vent2,text="Identificador Callejero")
lbl23_individual.grid(column=2,row=4)

lbl24_individual = Label(vent2,text="Codigo de via")
lbl24_individual.grid(column=4,row=4)

lbl25_individual = Label(vent2,text="Tipo de via")
lbl25_individual.grid(column=6,row=4)

lbl26_individual = Label(vent2,text="Nombre de via")
lbl26_individual.grid(column=8,row=4)

lbl27_individual = Label(vent2,text="Numero")
lbl27_individual.grid(column=0,row=5)

lbl28_individual = Label(vent2,text="Letra de Numero")
lbl28_individual.grid(column=2,row=5)

lbl29_individual = Label(vent2,text="Kilometro")
lbl29_individual.grid(column=4,row=5)

lbl30_individual = Label(vent2,text="Bloque")
lbl30_individual.grid(column=6,row=5)

lbl31_individual = Label(vent2,text="Escalera")
lbl31_individual.grid(column=8,row=5)

lbl32_individual = Label(vent2,text="Planta")
lbl32_individual.grid(column=0,row=6)

lbl33_individual = Label(vent2,text="Puerta")
lbl33_individual.grid(column=2,row=6)

lbl34_individual = Label(vent2,text="Otra informacion de la direccion")
lbl34_individual.grid(column=4,row=6)

lbl35_individual = Label(vent2,text="Importe en €")
lbl35_individual.grid(column=8,row=6)
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

txt5_individual = Entry(vent2,width=10,textvariable=Primera_Referencia)
txt5_individual.grid(column=3,row=1)

txt6_individual = Entry(vent2,width=10,textvariable=Numero_Cargo)
txt6_individual.grid(column=5,row=1)

txt7_individual = Entry(vent2,width=10,textvariable=Objeto_tributario)
txt7_individual.grid(column=7,row=1)

txt8_individual = Entry(vent2,width=10,textvariable=Codigo_Tercero)
txt8_individual.grid(column=9,row=1)

txt9_individual = Entry(vent2,width=10,textvariable=Tipo_Documento)
txt9_individual.grid(column=1,row=2)

txt10_individual = Entry(vent2,width=10,textvariable=Identificador)
txt10_individual.grid(column=3,row=2)

txt11_individual = Entry(vent2,width=10,textvariable=Tipo_Persona)
txt11_individual.grid(column=5,row=2)

#txt12_individual = Entry(vent2,width=10,textvariable=Identificador_Normalizado)
#txt12_individual.grid(column=17,row=1)

txt13_individual = Entry(vent2,width=10,textvariable=Apellido_1)
txt13_individual.grid(column=9,row=2)

txt14_individual = Entry(vent2,width=10,textvariable=Apellido_2)
txt14_individual.grid(column=1,row=3)

txt15_individual = Entry(vent2,width=10,textvariable=Particula_Apellido_1)
txt15_individual.grid(column=3,row=3)

txt16_individual = Entry(vent2,width=10,textvariable=Particula_Apellido_1)
txt16_individual.grid(column=5,row=3)

txt17_individual = Entry(vent2,width=10,textvariable=Nombre)
txt17_individual.grid(column=7,row=3)

txt18_individual = Entry(vent2,width=10,textvariable=Codigo_Postal)
txt18_individual.grid(column=9,row=3)

txt19_individual = Entry(vent2,width=10,textvariable=Identificador_Callejero)
txt19_individual.grid(column=1,row=4)

txt21_individual = Entry(vent2,width=10,textvariable=Codigo_Via)
txt21_individual.grid(column=3,row=4)

txt22_individual = Entry(vent2,width=10,textvariable=Tipo_Via)
txt22_individual.grid(column=5,row=4)

txt23_individual = Entry(vent2,width=10,textvariable=Nombre_Via)
txt23_individual.grid(column=7,row=4)

txt24_individual = Entry(vent2,width=10,textvariable=Numero)
txt24_individual.grid(column=9,row=4)

txt25_individual = Entry(vent2,width=10,textvariable=Letra_Numero)
txt25_individual.grid(column=1,row=5)

txt26_individual = Entry(vent2,width=10,textvariable=Kilometro)
txt26_individual.grid(column=3,row=5)

txt27_individual = Entry(vent2,width=10,textvariable=Bloque)
txt27_individual.grid(column=5,row=5)

txt28_individual = Entry(vent2,width=10,textvariable=Escalera)
txt28_individual.grid(column=7,row=5)

txt29_individual = Entry(vent2,width=10,textvariable=Planta)
txt29_individual.grid(column=9,row=5)

txt30_individual = Entry(vent2,width=10,textvariable=Puerta)
txt30_individual.grid(column=1,row=6)

txt31_individual = Entry(vent2,width=10,textvariable=Otra_Informacion_direccion)
txt31_individual.grid(column=3,row=6)

txt32_individual = Entry(vent2,width=10,textvariable=Importe_Euros)
txt32_individual.grid(column=5,row=6)


#desplegables

desplegable["values"]=("E","V","P")
desplegable.grid(column=1,row=2)

desplegable2["values"]=("R","L")
desplegable2.grid(column=3,row=2)

desplegable3["values"]=("S" ,"N")
ventanas.grid(column=7,row=2)
window.mainloop()

#archivos
