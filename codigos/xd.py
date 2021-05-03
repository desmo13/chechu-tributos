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
    
    contenido35 = Pais_Fiscal.get()
    contenido36 = Provincia_Fiscal.get()
    contenido37 = Poblacion_Fiscal.get()
    contenido38 = Codigo_Postal_Direcion_Fiscla.get()
    contenido39 = Identificador_Callejero_Fiscal.get()
    contenido40 = Codigo_Via_Fiscal.get()
    contenido41 = Tipo_Via_Fiscal.get()
    contenido42 = Nombre_Via_Fiscal.get()
    contenido43 = Numero_Fiscal.get()
    contenido44 = Letra_Numero_Fiscal.get()
    contenido45 = Kilometro_Fiscal.get()
    contenido46 = Bloque_Fiscal.get()
    contenido47 = Escalera_Fiscal.get()
    contenido48 = Planta_Fiscal.get()
    contenido49 = Puerta_Fiscal.get()
    contenido50 = Otra_Informacion_direccion_Fiscal.get()

    contenido51 = L1.get()
    contenido52 = L2.get()
    contenido53 = l3.get()
    contenido54 = l4.get()
    contenido55 = l5.get()
    contenido56 = l6.get()
    contenido57 = l7.get()
    contenido58 = l8.get()


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
        f.write("\nF"+numeros_espacios(contenido35,3)+numeros_espacios(contenido36,2)+numeros_espacios(contenido37,3)+numeros_espacios(contenido38,5)+espacios(contenido39,1)+numeros_espacios(contenido40,5)+espacios(contenido41,5)+espacios(contenido42,50)+numeros_espacios(contenido43,4)+espacios(contenido44,1)+numeros_espacios(contenido45,5)+espacios(contenido46,2)+espacios(contenido47,2)+espacios(contenido48,3)+espacios(contenido49,4)+espacios(contenido50,40)+espacios("",198))
        f.write("\nL1"+espacios(contenido51,80)+espacios("",252))
        f.write("\nL2"+espacios(contenido52,80)+espacios("",252))
        f.write("\nL3"+espacios(contenido53,80)+espacios("",252))
        f.write("\nL4"+espacios(contenido54,80)+espacios("",252))
        f.write("\nL5"+espacios(contenido55,80)+espacios("",252))
        f.write("\nL6"+espacios(contenido56,80)+espacios("",252))
        f.write("\nL7"+espacios(contenido57,80)+espacios("",252))
        f.write("\nL8"+espacios(contenido58,80)+espacios("",252))
        f.close() # `()` was missing.






#ventana
window = Tk()

ventanas =Notebook(window)

window.title("Chechu V1.7")

window.geometry("900x900")

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

Pais_Fiscal = StringVar()
Provincia_Fiscal = StringVar()
Poblacion_Fiscal = StringVar()
Codigo_Postal_Direcion_Fiscla =StringVar()
Identificador_Callejero_Fiscal =StringVar()
Codigo_Via_Fiscal = StringVar()
Tipo_Via_Fiscal = StringVar()
Nombre_Via_Fiscal = StringVar()
Numero_Fiscal = StringVar()
Letra_Numero_Fiscal =StringVar()
Kilometro_Fiscal = StringVar()
Bloque_Fiscal = StringVar()
Escalera_Fiscal = StringVar()
Planta_Fiscal = StringVar()
Puerta_Fiscal = StringVar()
Otra_Informacion_direccion_Fiscal = StringVar()

L1 =StringVar()
L2 = StringVar()
l3 = StringVar()
l4 = StringVar()
l5 = StringVar()
l6 = StringVar()
l7 = StringVar()
l8 = StringVar()
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
lbl11_individual.grid(column=0,row=2)

lbl12_individual = Label(vent2,text="Tipo de Documento" )
lbl12_individual.grid(column=2,row=2)

lbl13_individual = Label(vent2,text="Identificador")
lbl13_individual.grid(column=4,row=2)

lbl14_individual = Label(vent2,text="Tipo de persona")
lbl14_individual.grid(column=6,row=2)

lbl15_individual = Label(vent2,text="Identificador normalizado")
lbl15_individual.grid(column=0,row=3)

lbl16_individual = Label(vent2,text="1º Apellido")
lbl16_individual.grid(column=2,row=3)

lbl17_individual = Label(vent2,text="2º Apellido")
lbl17_individual.grid(column=4,row=3)

lbl18_individual = Label(vent2,text=" 1º Apellido Particula")
lbl18_individual.grid(column=6,row=3)

lbl19_individual = Label(vent2,text=" 2º Apellido Particula")
lbl19_individual.grid(column=0,row=4)

lbl20_individual = Label(vent2,text="Nombre")
lbl20_individual.grid(column=2,row=4)

lbl21_individual = Label(vent2,text="Codigo postal")
lbl21_individual.grid(column=4,row=4)

lbl23_individual = Label(vent2,text="Identificador Callejero")
lbl23_individual.grid(column=6,row=4)

lbl24_individual = Label(vent2,text="Codigo de via")
lbl24_individual.grid(column=0,row=5)

lbl25_individual = Label(vent2,text="Tipo de via")
lbl25_individual.grid(column=2,row=5)

lbl26_individual = Label(vent2,text="Nombre de via")
lbl26_individual.grid(column=4,row=5)

lbl27_individual = Label(vent2,text="Numero")
lbl27_individual.grid(column=6,row=5)

lbl28_individual = Label(vent2,text="Letra de Numero")
lbl28_individual.grid(column=0,row=6)

lbl29_individual = Label(vent2,text="Kilometro")
lbl29_individual.grid(column=2,row=6)

lbl30_individual = Label(vent2,text="Bloque")
lbl30_individual.grid(column=4,row=6)

lbl31_individual = Label(vent2,text="Escalera")
lbl31_individual.grid(column=6,row=6)

lbl32_individual = Label(vent2,text="Planta")
lbl32_individual.grid(column=0,row=7)

lbl33_individual = Label(vent2,text="Puerta")
lbl33_individual.grid(column=2,row=7)

lbl34_individual = Label(vent2,text="Otra informacion de la direccion")
lbl34_individual.grid(column=4,row=7)

lbl35_individual = Label(vent2,text="Importe en €")
lbl35_individual.grid(column=6,row=7)

lbl1_fiscal = Label(vent3,text="Pais Fiscal")
lbl1_fiscal.grid(column=0,row=1)

lbl2_fiscal = Label(vent3,text="Provincia Fiscal")
lbl2_fiscal.grid(column=2,row=1)

lbl3_fiscal = Label(vent3,text="Poblacion Fiscal")
lbl3_fiscal.grid(column=4,row=1)

lbl4_fiscal = Label(vent3,text="Código Postal Dirección Fiscal")
lbl4_fiscal.grid(column=6,row=1)

lbl5_fiscal = Label(vent3,text="Identificador de Callejero ")
lbl5_fiscal.grid(column=0,row=2)

lbl6_fiscal = Label(vent3,text="Código de Vía")
lbl6_fiscal.grid(column=2,row=2)

lbl7_fiscal = Label(vent3,text="Tipo de Vía")
lbl7_fiscal.grid(column=4,row=2)

lbl8_fiscal = Label(vent3,text="Nombre de Vía")
lbl8_fiscal.grid(column=6,row=2)

lbl9_fiscal = Label(vent3,text="Número Número")
lbl9_fiscal.grid(column=0,row=3)

lbl10_fiscal = Label(vent3,text=" Letra de Número")
lbl10_fiscal.grid(column=2,row=3)

lbl11_fiscal = Label(vent3,text=" Kilómetro")
lbl11_fiscal.grid(column=4,row=3)

lbl12_fiscal = Label(vent3,text=" Bloque")
lbl12_fiscal.grid(column=6,row=3)

lbl13_fiscal = Label(vent3,text=" Escalera")
lbl13_fiscal.grid(column=0,row=4)

lbl14_fiscal = Label(vent3,text=" Planta")
lbl14_fiscal.grid(column=2,row=4)

lbl15_fiscal = Label(vent3,text=" Puerta ")
lbl15_fiscal.grid(column=4,row=4)

lbl16_fiscal = Label(vent3,text=" Otra Información de la Dirección ")
lbl16_fiscal.grid(column=6,row=4)

lbl1Recibo = Label(vent4,text="Línea del recibo 1:")
lbl1Recibo.grid(column=0,row=1)

lb2Recibo = Label(vent4,text="Línea del recibo 2:")
lb2Recibo.grid(column=0,row=2)

lb3Recibo = Label(vent4,text="Línea del recibo 3:")
lb3Recibo.grid(column=0,row=3)

lb4Recibo = Label(vent4,text="Línea del recibo 4:")
lb4Recibo.grid(column=0,row=4)

lb5Recibo = Label(vent4,text="Línea del recibo 5:")
lb5Recibo.grid(column=0,row=5)

lb6Recibo = Label(vent4,text="Línea del recibo 6:")
lb6Recibo.grid(column=0,row=6)

lb7Recibo = Label(vent4,text="Línea del recibo 7:")
lb7Recibo.grid(column=0,row=7)

lb8Recibo = Label(vent4,text="Línea del recibo 8:")
lb8Recibo.grid(column=0,row=8)
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
txt8_individual.grid(column=1,row=2)

txt9_individual = Entry(vent2,width=10,textvariable=Tipo_Documento)
txt9_individual.grid(column=3,row=2)

txt10_individual = Entry(vent2,width=10,textvariable=Identificador)
txt10_individual.grid(column=5,row=2)

txt11_individual = Entry(vent2,width=10,textvariable=Tipo_Persona)
txt11_individual.grid(column=7,row=2)

#txt12_individual = Entry(vent2,width=10,textvariable=Identificador_Normalizado)
#txt12_individual.grid(column=17,row=1)

txt13_individual = Entry(vent2,width=10,textvariable=Apellido_1)
txt13_individual.grid(column=3,row=3)

txt14_individual = Entry(vent2,width=10,textvariable=Apellido_2)
txt14_individual.grid(column=5,row=3)

txt15_individual = Entry(vent2,width=10,textvariable=Particula_Apellido_1)
txt15_individual.grid(column=7,row=3)

txt16_individual = Entry(vent2,width=10,textvariable=Particula_Apellido_2)
txt16_individual.grid(column=1,row=4)

txt17_individual = Entry(vent2,width=10,textvariable=Nombre)
txt17_individual.grid(column=3,row=4)

txt18_individual = Entry(vent2,width=10,textvariable=Codigo_Postal)
txt18_individual.grid(column=5,row=4)

txt19_individual = Entry(vent2,width=0,textvariable=Identificador_Callejero)
txt19_individual.grid(column=7,row=4)

txt21_individual = Entry(vent2,width=10,textvariable=Codigo_Via)
txt21_individual.grid(column=1,row=5)

txt22_individual = Entry(vent2,width=10,textvariable=Tipo_Via)
txt22_individual.grid(column=3,row=5)

txt23_individual = Entry(vent2,width=10,textvariable=Nombre_Via)
txt23_individual.grid(column=5,row=5)

txt24_individual = Entry(vent2,width=10,textvariable=Numero)
txt24_individual.grid(column=7,row=5)

txt25_individual = Entry(vent2,width=10,textvariable=Letra_Numero)
txt25_individual.grid(column=1,row=6)

txt26_individual = Entry(vent2,width=10,textvariable=Kilometro)
txt26_individual.grid(column=3,row=6)

txt27_individual = Entry(vent2,width=2,textvariable=Bloque)
txt27_individual.grid(column=5,row=6)

txt28_individual = Entry(vent2,width=10,textvariable=Escalera)
txt28_individual.grid(column=7,row=6)

txt29_individual = Entry(vent2,width=10,textvariable=Planta)
txt29_individual.grid(column=1,row=7)

txt30_individual = Entry(vent2,width=10,textvariable=Puerta)
txt30_individual.grid(column=3,row=7)

txt31_individual = Entry(vent2,width=10,textvariable=Otra_Informacion_direccion)
txt31_individual.grid(column=5,row=7)

txt32_individual = Entry(vent2,width=10,textvariable=Importe_Euros)
txt32_individual.grid(column=7,row=7)

txt1_fiscal = Entry(vent3,width=10,textvariable=Pais_Fiscal)
txt1_fiscal.grid(column=1,row=1)

txt2_fiscal = Entry(vent3,width=10,textvariable=Provincia_Fiscal)
txt2_fiscal.grid(column=3,row=1)

txt3_fiscal = Entry(vent3,width=10,textvariable=Poblacion_Fiscal)
txt3_fiscal.grid(column=5,row=1)

txt4_fiscal = Entry(vent3,width=10,textvariable=Codigo_Postal_Direcion_Fiscla)
txt4_fiscal.grid(column=7,row=1)

txt5_fiscal = Entry(vent3,width=10,textvariable=Identificador_Callejero_Fiscal)
txt5_fiscal.grid(column=1,row=2)

txt6_fiscal = Entry(vent3,width=10,textvariable=Codigo_Via_Fiscal)
txt6_fiscal.grid(column=3,row=2)

txt7_fiscal = Entry(vent3,width=10,textvariable=Tipo_Via_Fiscal)
txt7_fiscal.grid(column=5,row=2)

txt8_fiscal = Entry(vent3,width=10,textvariable=Nombre_Via)
txt8_fiscal.grid(column=7,row=2)

txt9_fiscal = Entry(vent3,width=10,textvariable=Numero_Fiscal)
txt9_fiscal.grid(column=1,row=3)

txt10_fiscal = Entry(vent3,width=10,textvariable=Letra_Numero_Fiscal)
txt10_fiscal.grid(column=3,row=3)

txt11_fiscal = Entry(vent3,width=10,textvariable=Kilometro_Fiscal)
txt11_fiscal.grid(column=5,row=3)

txt12_fiscal = Entry(vent3,width=10,textvariable=Bloque_Fiscal)
txt12_fiscal.grid(column=7,row=3)

txt13_fiscal = Entry(vent3,width=10,textvariable=Escalera_Fiscal)
txt13_fiscal.grid(column=1,row=4)

txt14_fiscal = Entry(vent3,width=10,textvariable=Planta_Fiscal)
txt14_fiscal.grid(column=3,row=4)

txt15_fiscal = Entry(vent3,width=10,textvariable=Puerta_Fiscal)
txt15_fiscal.grid(column=5,row=4)

txt16_fiscal = Entry(vent3,width=10,textvariable=Otra_Informacion_direccion_Fiscal)
txt16_fiscal.grid(column=7,row=4)

txt1_linea_recibo = Entry(vent4,width=10,textvariable=L1)
txt1_linea_recibo.grid(column=1,row=1)

txt2_linea_recibo = Entry(vent4,width=10,textvariable=L2)
txt2_linea_recibo.grid(column=1,row=2)

txt3_linea_recibo = Entry(vent4,width=10,textvariable=l3)
txt3_linea_recibo.grid(column=1,row=3)

txt4_linea_recibo = Entry(vent4,width=10,textvariable=l4)
txt4_linea_recibo.grid(column=1,row=4)

txt5_linea_recibo = Entry(vent4,width=10,textvariable=l5)
txt5_linea_recibo.grid(column=1,row=5)

txt6_linea_recibo = Entry(vent4,width=10,textvariable=l6)
txt6_linea_recibo.grid(column=1,row=6)

txt7_linea_recibo = Entry(vent4,width=10,textvariable=l7)
txt7_linea_recibo.grid(column=1,row=7)

txt8_linea_recibo = Entry(vent4,width=10,textvariable=l8)
txt8_linea_recibo.grid(column=1,row=8)
#desplegables

desplegable["values"]=("E","V","P")
desplegable.grid(column=1,row=2)

desplegable2["values"]=("R","L")
desplegable2.grid(column=3,row=2)

desplegable3["values"]=("S" ,"N")
desplegable3.grid(column=1,row=3)
ventanas.grid(column=10,row=10)
window.mainloop()

#archivos
