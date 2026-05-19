usuarios_registrados = {
    "Luis": {"contraseña": "luis1234",
             "saldo": 1000},
    "María": {"contraseña": "maria1234",
              "saldo": 1500},
    "Carlos": {"contraseña": "carlos1234",
               "saldo": 2000},
    "Ana": {"contraseña": "ana1234",
            "saldo": 1200},
    "Pedro": {"contraseña": "pedro1234",
              "saldo": 1800},
    "Laura": {"contraseña": "laura1234",
              "saldo": 2500},
    "Jose": {"contraseña": "jose1234",
             "saldo": 5000},
}

intentos = 0

while intentos < 3:
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if nombre_usuario in usuarios_registrados and usuarios_registrados[nombre_usuario]["contraseña"] == contraseña:
        
        print(f"Bienvenido, {nombre_usuario}!")

        while True:
            print("1. Ver saldo")
            print("2. Retirar dinero")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"Tu saldo actual es: ${usuarios_registrados[nombre_usuario]['saldo']}.")
            elif opcion == "2":
                print("Marque 0 para volver al menú principal.")
                monto_retiro = float(input("Ingrese el monto a retirar: "))

                while monto_retiro <= 0 or monto_retiro > usuarios_registrados[nombre_usuario]['saldo']:
                    if monto_retiro == 0: 
                        print("Volviendo al menú principal.")
                        break
                    if monto_retiro <= 0:
                        print("El monto a retirar debe ser mayor a cero.")
                    elif monto_retiro > usuarios_registrados[nombre_usuario]['saldo']:
                        print("Saldo insuficiente para realizar el retiro.")
                    monto_retiro = float(input("Ingrese un monto válido a retirar: "))
                if monto_retiro != 0:    
                    usuarios_registrados[nombre_usuario]["saldo"] -= monto_retiro
                    print(f"Has retirado ${monto_retiro}.")
                    print(f"Tu saldo actual es: ${usuarios_registrados[nombre_usuario]['saldo']}.")
            elif opcion == "3":
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

    else:
        intentos += 1
        print(f"Credenciales incorrectas. Intento {intentos} de 3.")
    if intentos == 3:
        print("Cuenta bloqueada. Por favor, intente nuevamente más tarde.")