#Pide al usuario su edad y muestra cuantos años tendrá dentro de 10 años

edad = int(input("Ingresa tu edad para calcular cuantos años tendrás en 10 años: "))

print(f"En diez años tendrás {edad + 10}")
print(f"Hace 5 años tenias {edad - 5}")


if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad :)")
    
if edad + 45 > 95:
    print("Probablemente estes en otro plano en 45 años")
else:
    print("Te falta para irte al otro plano")