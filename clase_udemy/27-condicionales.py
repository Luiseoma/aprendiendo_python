#Condicionales
edad = 17
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

#Condicionales con operadores logicos
edad = 30
if edad >= 18 and edad < 30:
    print("Eres un joven adulto")  
elif edad >= 30 and edad < 60:
    print("Eres un adulto")
elif edad >= 60:
    print("Eres un adulto mayor")
else:
    print("Eres un niño")


#Revisar si una condición es mayor a 
balance = 500
if balance > 51:
    print("Puedes pagar")

#else

balance = 0
if balance > 0:
    print("Tienes dinero en tu cuenta")
else:
    print("No tienes dinero en tu cuenta")

 #Likes
likes = 100
if likes >= 100:
    print("Tu publicación es popular")   
else:
    print("Tu publicación no es popular")

#If con texto
lenguaje = 'Python'
if not lenguaje == 'Python':
    print("¡Me encanta Python!")

#Evaluar un boolean
usuario_autenticado = True

if usuario_autenticado:
    print("Bienvenido, puedes acceder a tu cuenta")
else:
    print("Debes iniciar sesión para acceder a tu cuenta")

