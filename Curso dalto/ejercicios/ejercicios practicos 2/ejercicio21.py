#Ejercicio 18: Contador de palabras
#
#Pide una frase.
#
#Muestra:
#
#Cantidad de palabras
#Cantidad de caracteres
#Frase en mayúsculas
#
#Pista:
#
#split()
#len()
#upper()

frase = input("Ingrese una frase: ")
frase_mayus = frase.upper()
frase2 = frase.split()

print(len(frase2))
print(frase_mayus)