#pide dos numeros y muestra: suma resta multiplicacion y division

numero1= int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

print(f"La suma de {numero1} + {numero2} es {numero1 + numero2}")
print(f"La resta de {numero1} - {numero2} es {numero1 - numero2}")
print(f"La multiplicacion de {numero1} * {numero2} es {numero1 * numero2}")



if numero2 == 0: 
    print("Ingresa un número mayor a 0")
else:
    print(f"La division de {numero1} / {numero2} es {numero1 / numero2}") 
    print(f"El residuo de {numero1} / {numero2} es {numero1 % numero2}")
    
print(f"La potencia de {numero1} es {numero1 ** numero2}")

if numero1 > numero2:
    print(f"El número mayor es {numero1}")
elif numero1 == numero2:
    print("Ambos números son iguales")
else:
    print(f"El número mayor es {numero2}")