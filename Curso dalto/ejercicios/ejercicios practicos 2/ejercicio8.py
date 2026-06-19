#Ejercicio 5: Suma acumulada
#
#Pide números al usuario hasta que escriba 0.
#
#Al final muestra la suma total.
#
#Ejemplo:
#
#Número: 5
#Número: 3
#Número: 2
#Número: 0
#
#Total = 10

numero = float(input("Ingrese numeros hasta llegar al 0: "))
total = 0

while numero != 0:
    total = total + numero
    numero = float(input("Ingrese otro número: "))

print(total)