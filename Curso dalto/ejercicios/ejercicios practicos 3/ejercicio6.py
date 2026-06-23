#Ejercicio 6: Control de Inventario
#Una tienda tiene:
#inventario = {
#    "mouse": 15,
#    "teclado": 8,
#    "monitor": 5
#}
#Permite:
#1. Consultar stock
#2. Vender producto
#3. Salir
#Cuando se venda un producto, debe descontarse del inventario.

inventario = {
    "mouse": 15,
    "teclado": 8,
    "monitor": 5
}

opcion = int(input("Ingrese una opción: 1. Consultar stock 2. Vender producto 3. Salir  "))

while opcion != 3:
    if opcion == 1:
        for producto, stock in inventario.items():
            print(f"{producto}: {stock}")
    elif opcion == 2:
        producto = input("Ingrese producto a vender: ")
        if producto in inventario:
            if inventario[producto] > 0:
                inventario[producto] = inventario[producto] -1
            else:
                print("Stock insuficiente")
        else:
            print("Producto no existe")
                
    opcion = int(input("Ingrese una opción: 1. Consultar stock 2. Vender producto 3. Salir  "))
    
print("Gracias por usar nuestra APP!")
    
    