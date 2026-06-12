#Pide un nombre y que muestre por que letra empieza y si no empieza por la letra dada "A"

nombre = input("Ingrese su nombre: ")

if nombre.upper().startswith ("A"):
    print("Su nombre empieza con A")
else:
    print("Su nombre no empieza con la A")
    
