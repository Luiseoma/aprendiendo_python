#Usando open para abrir un archivo con codificacion universal (UTF-8) 

archivo = open("Curso dalto/archivos/hola_como_estas.txt", encoding="UTF-8")

#leer archivo completo
archivo = archivo.read()

#leer linea por linea 
#linea1 = archivo_sin_leer.readlines()

#leer una sola linea
#linea = archivo_sin_leer.readline(20)

#cerrar el archivo
archivo.close()

print(archivo)