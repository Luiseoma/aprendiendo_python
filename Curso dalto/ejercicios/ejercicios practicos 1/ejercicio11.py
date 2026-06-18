#Pide una contraseña

contraseña_correcta = "python123"

contraseña_ingresada = input("Ingrese contraseña: ")

if contraseña_ingresada == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")