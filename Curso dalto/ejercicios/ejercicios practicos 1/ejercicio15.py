#Ingresa nombre y edad y dile si es menor de edad, adulto o adulto mayor

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Ingrese una edad válida")
elif edad < 18:
    print(f"{nombre} usted tiene {edad} años, usted es menor de edad")
elif edad <= 64:
    print(f"{nombre} usted tiene {edad} años, usted es un adulto")
else:
    print(f"{nombre} usted tiene {edad} años, usted es un adulto mayor")
