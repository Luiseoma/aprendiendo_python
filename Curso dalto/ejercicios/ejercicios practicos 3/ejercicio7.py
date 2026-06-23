#Ejercicio 7: Sistema de Nómina
#Pide:
#Nombre del empleado
#Horas trabajadas
#Valor por hora
#Calcula:
#Sueldo bruto
#Si trabajó más de 40 horas:
#Horas extras = 1.5 veces el valor normal

empleado = input("Ingrese nombre del trabajador: ")
horas = float(input("Ingrese horas trabajadas: "))
valor_hora = 30000
valor_hora_extra = valor_hora * 1.5
sueldo_bruto = horas * valor_hora


if horas <= 40:
    print(f"Sueldo del trabajador de este mes: {sueldo_bruto}")
else:
    horas_extra = horas - 40
    calculo_extra = horas_extra * valor_hora_extra
    print(f"Sueldo a base de este mes: ${sueldo_bruto}")
    print(f"Monto a pagar por horas extras: ${calculo_extra}")
    print(f"Sueldo total del mes: ${sueldo_bruto + calculo_extra}")
    
