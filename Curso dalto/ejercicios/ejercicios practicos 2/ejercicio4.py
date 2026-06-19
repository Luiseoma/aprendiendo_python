#Nivel 1: Variables, entrada de datos y condicionales
#Ejercicio 1: Mayor de edad
#
#Pide la edad al usuario y muestra:
#
#"Eres mayor de edad" si tiene 18 o más.
#"Eres menor de edad" en caso contrario.

edad = int(input("Ingrese su edad: "))


if edad <= 0:
    print("Ingrese una Edad válida")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
    
    