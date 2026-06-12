#Pide tres numeros y muestra cual es el mayor

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese un segundo número: "))
numero3 = float(input("Ingrese un tercer número: "))

if numero1 > numero2 and numero1 > numero3: 
    print(f"El número mayor que ingresó fue el número {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número mayor que ingresó fue el número {numero2}")
else:
    print(f"El número mayor que ingresó fue el {numero3}")