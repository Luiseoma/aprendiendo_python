usuario = 'Luis Omaña'
contraseña = 123456
intentos = 0



while intentos < 3:
     
    validacion_usuario = input('Ingrese usuario: ')
    validacion_contraseña = int(input('Ingrese contraseña: '))

    if validacion_usuario != usuario:
        print('Usuario incorrecto')
        intentos = intentos + 1
        
    elif validacion_contraseña != contraseña:
        print('Contraseña incorrecta')
        intentos = intentos + 1
    else:
        print (f'Inicio de sesión exitoso')

        while True: 
            print('1. Ver saldo')
            print('2. Retirar dinero')
            print('3. Salir')
            
            opcion = input('Seleccione una opción: ')

            if opcion == '1':

                saldo = 100000
                print(f'Su saldo es: ${saldo}')

            elif opcion == '2':

                monto_retiro = float(input('Ingrese monto a retirar: '))

                if monto_retiro < saldo :
                    saldo = saldo - monto_retiro

                    print(f'Retiro exitoso')
                    print(f'Saldo restante: ${saldo}')

                else:
                    print('Fondos insuficientes')

            elif opcion == '3':
                print('Cerrando sesión...')
                break
        break

if intentos == 3:
    print('Cuenta bloqueada')


