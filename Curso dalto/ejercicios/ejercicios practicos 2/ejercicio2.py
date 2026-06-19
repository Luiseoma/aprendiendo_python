#Crea una funcion que devuelva numeros primos desde el 0 hasta el numero que pasemos


#crear una funcion que verifica si un numero es primo
def es_primo(num):
    #verificamos que un numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creando función que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos

#creamos el resultado llamando a la función y lo mostramos
resultado = primos_hasta(13)        
print(resultado)

#con lambda
primos_hasta2 = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta2(15))
