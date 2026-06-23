#Ejercicio 1: Sistema de Login
#Crea un programa que:
#Tenga un usuario y contraseña guardados.
#Pida usuario y contraseña.
#Si son correctos, muestre:
#Bienvenido Luis
#Si falla 3 veces, bloquee el acceso.
#Ejemplo:
#Usuario: admin
#Contraseña: 1234
#Bienvenido admin

usuario = "Luisenoma"
contraseña = "luis1234"
intentos = 3

while intentos > 0:
    ingreso = input("Ingrese su usuario: ")
    password = input("Ingrese contraseña: ")
    
    if ingreso == usuario and password == contraseña:
        print("Bienvenido, accediendo...")
        break
    
    intentos -= 1
    print("Acceso denegado, reintente.")
    
    if intentos > 0: 
        print(f"Intentos restantes: {intentos}")   
    else:
        print("Usuario bloqueado")


    
    