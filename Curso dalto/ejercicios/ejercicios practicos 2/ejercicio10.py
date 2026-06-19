#Ejercicio 7: Función para calcular área
#
#Crea una función:
#
#def area_rectangulo(base, altura):
#
#Que devuelva el área.
#
#Luego pide los datos al usuario y utiliza la función.

def area_rectangulo(base, altura):
    return base * altura
    
base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))
    
print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")