#Ejercicio 17: Sistema de notas
#
#Pide 5 notas.
#
#Guárdalas en una lista.
#
#Muestra:
#
#Nota más alta
#Nota más baja
#Promedio
#
#Y además:
#
#Si el promedio es 4 o más → "Aprobado"
#Si es menor → "Reprobado"

lista = []

for i in range (5):
    notas = int(input("Ingrese nota: "))
    lista.append(notas)
promedio = sum(lista) / len(lista)
print(max(lista))
print(min(lista))
print(promedio)

if promedio >= 4:
    print("Aprobado")
else:
    print("Reprobado")