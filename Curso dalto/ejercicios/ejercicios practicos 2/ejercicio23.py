#Ejercicio 20: Menú interactivo
#
#Haz un programa que muestre:
#
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Salir
#
#Mientras el usuario no elija 4, el menú debe seguir apareciendo.
#
#Aquí practicas:
#
#while
#if/elif
#funciones
#input
#operadores

opcion = int(input("Ingrese una opción: "))

while opcion != 4:
    if opcion == 1:
        print("Elegiste sumar")
        num1 = float(input("Ingrese numero: "))
        num2 = float(input("Ingrese numero: "))
        print(f"El resultado es: {num1 + num2}")
    elif opcion == 2: 
        print("Elegiste restar")
        num1 = float(input("Ingrese numero: "))
        num2 = float(input("Ingrese numero: "))
        print(f"El resultado es: {num1 - num2}")
    elif opcion == 3:
        print("Elegiste multiplicar")
        num1 = float(input("Ingrese numero: "))
        num2 = float(input("Ingrese numero: "))
        print(f"El resultado es: {num1 * num2}")
    else:
        print("Ingrese una opción válida")

    opcion = int(input("Ingrese una opción: "))    

print("Saliendo del sistema")  