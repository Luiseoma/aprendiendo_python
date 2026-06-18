#Pide un nombre y muestra: Todo en mayúsculas, Todo en minúsculas, Cuántas letras tiene

nombre = input("Ingrese su nombre: ")

nombre_mayus = nombre.upper()

nombre_min = nombre.lower()

conteo = len(nombre)

print(nombre_mayus)
print(nombre_min)
print(conteo)