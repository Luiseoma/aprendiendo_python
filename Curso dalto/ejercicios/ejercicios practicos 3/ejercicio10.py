#Ejercicio 10 (Nivel Junior Real)
#Sistema de Gestión de Empleados.
#Menú:
#1. Agregar empleado
#2. Buscar empleado
#3. Listar empleados
#4. Eliminar empleado
#5. Salir
#Cada empleado tendrá:
#Nombre
#Cargo
#Sueldo
#Ejemplo:
#empleados = {
#    "Luis": {
#        "cargo": "Analista",
#        "sueldo": 1200000
#    }
#}

empleados = {}

def agregar():
    nombre = input("Ingrese nombre del empleado: ")
    
    if nombre in empleados:
        print("El empleado ya existe.")
        return
    cargo = input("Agregue el cargo del empleado: ")
    
    try:
        sueldo = int(input("Agregue sueldo del empleado: "))
    except ValueError:
        print("Sueldo inválido. Debe ser un número.")
        return
    
    empleados[nombre] = {"cargo": cargo, "sueldo": sueldo}
    print("Empleado agregado correctamente.")
    
def buscar():
    nombre = input("Ingrese nombre de empleado: ")
    busqueda = empleados.get(nombre)
    if busqueda:
        print(f"{nombre} - Cargo: {busqueda["cargo"]} - Sueldo: {busqueda["sueldo"]}")
    else:
        print("Empleado no encontrado.")
    
def listar():
    if not empleados:
        print("No hay empleados registrados.")
        return
    
    for nombre, datos in empleados.items():
        print(f"{nombre} - Cargo: {datos['cargo']} - Sueldo: {datos['sueldo']}")

def eliminar():
    nombre = input("Ingrese nombre a eliminar: ")
    if nombre in empleados:
        empleados.pop(nombre)
        print("Empleado eliminado correctamente.")
    else:
        print("Empleado no encontrado.")
        
def update():
    nombre = input("Ingrese nombre para actualizar datos: ")
    
    if nombre in empleados:
        datos = empleados[nombre]
        print(f"\nDatos actuales:")
        print(f"Cargo actual: {datos['cargo']}")
        print(f"Sueldo actual: {datos['sueldo']}")
        
        print("\n¿Qué desea modificar?")
        print("1. Cargo")
        print("2. Sueldo")
        
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            nuevo_cargo = input("Ingrese nuevo cargo: ")
            empleados[nombre]["cargo"] = nuevo_cargo
            print("Cargo actualizado correctamente.")
        elif opcion == "2":
            try:
                nuevo_sueldo = int(input("Ingrese nuevo sueldo: "))
                empleados[nombre]["sueldo"] = nuevo_sueldo
                print("Sueldo actualizado correctamente.")
            except ValueError:
                print("Sueldo inválido.")
                
        else:
            print("Opción inválida.")
    else:
        print("Empleado no encontrado.")
        
        
while True:
    print("\n---SISTEMA DE GESTIÓN DE EMPLEADOS---")
    print("1. Agregar empleado")
    print("2. Buscar empleado")
    print("3. Listar empleados")
    print("4. Eliminar empleado")
    print("5. Actualizar empleado")
    print("6. Salir")
    
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue
    
    if opcion == 1:
        agregar()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        listar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        update()
    elif opcion == 6:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida, ingrese nuevamente")