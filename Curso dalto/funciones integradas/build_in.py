numeros = [4, 7, 1 ,24, 15]


#encontrando el número mayor de una lista
numero_alto = max(numeros)
print(numero_alto)

#encontrando el número menor de una lista
numero_bajo = min(numeros)
print(numero_bajo)

#redondeando a 6 decimales
numero = round(12.345678,5)
print (numero)

#retorna False --> 0, vacio, False, ninguno --> numero o dato distinto devuelve True
resultado_bool = bool(["Luis", "Pedro", "Veronica"])
print(resultado_bool)

#retorna True si todos los valores son verdaderos
resultado_all = all([1234, "true", [344, 23]])

print(resultado_all)

#Suma todos los valores de un iterable

suma_total = sum(numeros)
print(suma_total)
