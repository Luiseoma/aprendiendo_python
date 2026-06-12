saldo_disponible= 100000

monto_retiro = float(input('Ingrese monto a retirar: '))

if monto_retiro < saldo_disponible :
    saldo_restante = saldo_disponible - monto_retiro

    print(f'Retiro exitoso')
    print(f'Saldo restante: ${saldo_restante}')

else:
    print('Fondos insuficientes')