#Abriendo el archivo con with open
with open("Curso dalto/archivos/hola_como_estas.txt", encoding="UTF-8")as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #Mostramos el archivo
    print(contenido)
    
#no es necesario cerrar al usar with open