#Ejercicio 2: Número par o impar
#
#Pide un número al usuario y determina si es par o impar.
#
#Pista:
#
#numero % 2
#


numero = int(input("Ingrese un número para determinar si es par o impar: "))

if numero % 2 == 0:
    print("Tu numero es par")
else:
    print("Tu numero es impar")