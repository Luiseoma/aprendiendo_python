#Pide una edad y determina si la persona es menor o mayor de edad

edad = int(input("Ingrese su edad: "))

if edad <= 0: 
    print("Ingrese una edad válida")

elif edad < 18: 
    print("🚨🚨🚨 Usted es menor de edad, no puede pasar 🚨🚨🚨")

else:
    print("⬆️ Usted es mayor de edad, si puede pasar ⬆️")