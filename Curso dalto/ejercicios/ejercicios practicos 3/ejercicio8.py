#Ejercicio 8: Agenda de Contactos
#Permite:
#1. Agregar contacto
#2. Buscar contacto
#3. Ver todos
#4. Salir
#Puedes guardar los contactos en un diccionario.
#Ejemplo:
#{
#    "Luis": "987654321",
#    "Ana": "123456789"
#}

opcion = int(input("Ingrese una opción: 1. Agregar contacto 2. Buscar contacto 3. Ver todos 4. Salir  "))
contactos = {}

while opcion != 4:
    if opcion == 1:
        nombre = input("Ingrese nombre: ")
        numero = int(input("Ingrese número: "))
        contactos[nombre] = numero
    elif opcion == 2:
        buscar = (input("Ingrese nombre: "))
        busqueda = contactos.get(buscar)
        if buscar not in contactos:
            print("Contacto no encontrado.")
        else:
            print(busqueda)
        
    elif opcion == 3:
        for nombre, numero in contactos.items():
            print(f"{nombre}: {numero}")
        
    opcion = int(input("Ingrese una opción: 1. Agregar contacto 2. Buscar contacto 3. Ver todos 4. Salir  "))