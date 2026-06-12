#Pide un número y determina si es: positivo, negativo, cero

numero = float(input("Ingrese un número: "))


if numero == 0:
    print(f"Su número es cero")
elif numero < 0:
    print("Su número es negativo")
else:
    print("Su número es positivo")