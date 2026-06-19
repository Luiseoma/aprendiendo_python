#Ejercicio 10: Analizador de nombre
#
#Pide un nombre y muestra:
#
#Todo en mayúsculas
#Todo en minúsculas
#Cuántos caracteres tiene
#
#Ejemplo:
#
#Luis
#
#Salida:
#
#LUIS
#luis
#4

nombre = input("Inserte un nombre: ")

resultado = nombre.upper()
resultado2 = nombre.lower()
resultado3 = len(nombre)

print(f"Su nombre es {resultado}")
print(f"Su nombre es {resultado2}")
print(f"Su nombre tiene {resultado3} letras")