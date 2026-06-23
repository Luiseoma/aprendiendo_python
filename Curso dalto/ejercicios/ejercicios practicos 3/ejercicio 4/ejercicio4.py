#Ejercicio 4: Analizador de Archivo
#Usa el archivo de texto que ya sabes abrir.
#El programa debe indicar:
#Cantidad de caracteres
#Cantidad de palabras
#Cantidad de líneas
#Ejemplo:
#Caracteres: 120
#Palabras: 25
#Líneas: 4

with open ("Curso dalto/ejercicios/ejercicios practicos 3/ejercicio 4/ejercicio4.txt", encoding="UTF-8") as archivo:
    contenido = archivo.read()
    
    print(f"El archivo tiene {len(contenido)} caracteres")
    print(f"El archivo tiene {len(contenido.split())} palabras")
    print(f"El archivo tiene {len(contenido.splitlines())} líneas")
