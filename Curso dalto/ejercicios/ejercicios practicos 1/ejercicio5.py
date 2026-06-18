#Pide el precio de un producto y calcula el precio con IVA del 19%.

precio = float(input("Ingresa valor del producto para calcular el IVA: "))
iva = precio * 1.19

if precio > 0:
    print(f"el IVA de tu producto es {iva - precio}")
    print(f"El valor final de tu compra es ${iva}")
else:
    print("Ingrese un monto mayor a 0")




