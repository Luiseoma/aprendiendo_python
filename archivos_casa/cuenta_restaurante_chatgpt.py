cantidad_a_pagar = float(input('¿Cuánto costó la cuenta? '))

porcentaje_propina = float(input('¿Qué porcentaje de propina desea dejar? '))

división_cuenta = int(input('¿Entre cuántas personas se dividirá la cuenta? '))

monto_propina = cantidad_a_pagar * porcentaje_propina / 100

total_a_pagar = cantidad_a_pagar + monto_propina

if división_cuenta > 0:
    monto_por_persona = total_a_pagar / división_cuenta
   
    print (f'El monto de la propina es: ${monto_propina:.2f}')

    print (f'El total a pagar es: ${total_a_pagar:.2f}')

    print (f'Cada persona debe pagar: ${monto_por_persona:.2f}')
else:
    print('El número de personas debe ser mayor que cero para dividir la cuenta.')

    


