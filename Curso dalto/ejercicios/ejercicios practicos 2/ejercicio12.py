#Contador de vocales
#
#Crea una función que reciba una palabra y devuelva cuántas vocales tiene.
#
#Ejemplo:
#
#contar_vocales("murcielago")
vocales = "aeiou"

def contar_vocales(palabra):
 
    contador = 0
    
    for letra in palabra:
        if letra in vocales:
            contador = contador + 1
    return contador

def contar_consonantes(palabra):
    contador = 0
    
    for letra in palabra:
        if letra not in vocales:
            contador = contador + 1
    return contador
             
palabra = input("Ingrese una palabra: ")

print(f"Su palabra tiene {contar_vocales(palabra)} vocales")
print(f"Su palabra tiene {contar_consonantes(palabra)} consonantes")