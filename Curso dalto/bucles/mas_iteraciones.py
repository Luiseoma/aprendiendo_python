frutas = ["banana", "fresas", "platano", "mango"]
cadena = "hola mundo"
numeros = [2, 5, 8, 10]

#evitando que se coma una banana con la sentencia continue
for fruta in frutas:
    if fruta == "banana":
        continue
    print(f"me voy a comer una {fruta}")

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "platano":
        break
else:
    print("terminado")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una linea de codigo
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)

#tambien se puede ocupar
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)