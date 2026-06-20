#Ejercicio 19: Números primos
#
#Crea una función:
#
#def es_primo(numero):
#
#Que determine si un número es primo.
#
#Después pide un número al usuario y utiliza la función.
#
#(Este ejercicio es excelente para practicar bucles y funciones.)



def es_primo(numero):
    for i in range(2, numero):
        if numero%i ==  0: return False
    return True

numero = int(input("Ingrese un número para saber si es primo: "))

print(es_primo(numero))