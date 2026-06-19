#Ejercicio 8: Función para saber si un número es positivo
#
#Crea:
#
#def es_positivo(numero):
#
#Debe devolver:
#
#True
#
#o
#
#False

def es_positivo(numero):
    if numero < 0:
        return False
    
    return True
        
numero = float(input("Ingrese un número: "))

print(es_positivo(numero))