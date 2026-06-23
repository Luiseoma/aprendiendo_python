#Ejercicio 5: Cajero Automático
#Simula un cajero.
#Saldo inicial:
#saldo = 100000
#Menú:
#1. Consultar saldo
#2. Depositar
#3. Retirar
#4. Salir
#Debe validar que no se pueda retirar más dinero del disponible

opcion = int(input("Bienvenido, ingrese una opción: 1. Consultar saldo 2. Depositar 3. Retirar 4.Salir "))
saldo = 100000

while opcion != 4: 
    if opcion == 1:
        print(f"Su saldo es ${saldo}")
    elif opcion == 2: 
        deposito = float(input("Ingrese monto a depositar: "))
        saldo= saldo + deposito
        print(f"Su nuevo saldo es: ${saldo}")
    elif opcion == 3:
        retiro = float(input("Ingrese monto a retirar: "))
        if retiro > saldo:
            print("Saldo insuficiente")
        elif retiro <= 0:
            print("Ingrese un monto válido")
        else:
            saldo = saldo - retiro
            print(f"Dinero retirado. Su nuevo saldo es: ${saldo}") 
    else:
        print("Ingrese una opción válida")
        
    opcion = int(input("Ingrese una opción: 1. Consultar saldo 2. Depositar 3. Retirar 4.Salir "))

print("Gracias por preferirnos. Cerrando sesión")