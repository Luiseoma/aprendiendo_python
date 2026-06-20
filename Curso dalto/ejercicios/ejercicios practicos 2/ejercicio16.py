#Ejercicio 13
#
#Pide 5 números y guárdalos en una lista.
#
#Luego muestra:
#
#max(lista)
#min(lista)
#sum(lista)

lista = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)
    


print(max(lista))
print(min(lista))
print(sum(lista))