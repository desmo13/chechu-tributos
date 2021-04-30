def espacios(contenido, max):
    contenido 
    espacio = "."
    if  len(contenido)<max:
        for i in range(max - len(contenido)):
            contenido  =  contenido + espacio 
        print(contenido)
    return contenido

espacios("hola",11)