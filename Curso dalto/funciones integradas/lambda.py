numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

#creando una funcion lambda para multiplicar *2
multiplicar_por_dos = lambda x : x*2

#usando filter con una funcion comun
def es_par(num):
    if (num%2==0):
        return True
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

#creando lo mismo pero con lambda
numeros_pares2 = filter(lambda numero:numero%2 == 0 ,numeros)

print(list(numeros_pares2))