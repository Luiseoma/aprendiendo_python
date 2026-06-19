#Ejercicio 4: Tabla de multiplicar
#
#Pide un número y muestra su tabla del 1 al 10.
#
#Ejemplo:
#
#5 x 1 = 5
#5 x 2 = 10
#...

numero = int(input("ingrese un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")