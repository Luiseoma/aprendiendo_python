animales = ("perro", "gato", "loro", "toro")
numeros = (52, 40, 5, 10)
print(type(animales))
#recorriendo la lista animales

for animal in animales:
    print(animal)

#recorriendo la lista numeros y multiplicando cada variable * 10

for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#Iterando dos listas al mismo tiempo

for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice} y el valor es {valor}")
    
#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")

else:
    print("el bucle termino")


#todo lo anterior funciona exactamente igual para listas, conjuntos y tuplas
