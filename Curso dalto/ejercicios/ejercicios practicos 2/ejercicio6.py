#Ejercicio 3: Calculadora simple
#
#Pide:
#
#Primer número
#Segundo número
#Operación (+, -, *, /)
#
#Y realiza la operación correspondiente.

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
operacion = input("Ingrese operación: ")


#DOS FORMAS DE RESOLVER ESTE EJERCICIO

#===========
#FORMA 1
#===========
#if operacion == "+":
#    print(f"La suma de {numero1} + {numero2} es igual a: {numero1 + numero2} ")
#elif operacion == "-":
#    print(f"La resta de {numero1} - {numero2} es igual a: {numero1 - numero2}")
#elif operacion == "*":
#    print(f"La multiplicación de {numero1} * {numero2} es igual a: {numero1 * numero2}")
#elif operacion == "/":
#    if numero2 == 0:
#        print("No se puede dividir entre 0")
#    else:
#        print(f"La división de {numero1} / {numero2} es igual a: {numero1 / numero2}")
#
#else:
#    print("Ingrese una operación válida")

#===========
#FORMA 2
#===========
resultado = None

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2
else:
    print("Ingrese una operación válida")


if resultado is not None:
    print(resultado)