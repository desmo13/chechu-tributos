def espacios(contenido, max):
    contenido 
    espacio = "0"
    if  len(contenido)<max:
        for i in range(max - len(contenido)):
            contenido  = espacio +  contenido 
        print(contenido)
    return contenido

espacios("100",11)