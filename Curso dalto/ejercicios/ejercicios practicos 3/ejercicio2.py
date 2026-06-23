#Ejercicio 2: Registro de Ventas
#Una tienda registra las ventas del día.
#El programa debe:
#Preguntar cuánto vendió cada cliente.
#Seguir preguntando hasta que el usuario escriba 0.
#Mostrar:
#Cantidad de ventas
#Total vendido
#Promedio por venta
#Ejemplo:
#Ingrese venta: 15000
#Ingrese venta: 20000
#Ingrese venta: 10000
#Ingrese venta: 0
#Ventas realizadas: 3
#Total vendido: 45000
#Promedio: 15000

venta = float(input("Ingrese monto de la venta: "))
ventas = 0
total = 0

while venta > 0:
    total += venta 
    ventas += 1
    venta = float(input("Ingrese monto de la venta: "))
    
    
print(f"El monto total de la venta fue: ${total}")
print(f"Hubo {ventas} en el día")

if ventas > 0:
    print(f"El promedio de ticket fue de: ${total / ventas:.2f}")
else:
    print("No se registraron ventas.")    
    