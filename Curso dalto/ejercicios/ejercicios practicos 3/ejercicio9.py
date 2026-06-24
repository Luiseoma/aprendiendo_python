#Ejercicio 9: Menú de Reportes
#Imagina que trabajas en una petrolera (como donde trabajas actualmente).
#Cada día se registran barriles producidos.
#El programa debe permitir:
#Agregar producción
#Ver total producido
#Ver promedio diario
#Ver producción máxima
#Salir
#Aquí practicas listas, ciclos y funciones.


produccion = []

def agregar_produccion(lista, valor):
    if valor < 0:
        print("Ingrese un valor válido.")
    else:
        lista.append(valor)

def total_producido(lista):
    return sum(lista)
    
def prom_data(lista):
    return sum(lista) / len(lista) if lista else 0
        
def max_producc(lista):
    return max(lista) if lista else 0
        
        
while True:
    print("\n--- SISTEMA DE PRODUCCIÓN ---")
    print("1. Agregar producción")
    print("2. Ver total producido")
    print("3. Ver promedio diario")
    print("4. Ver producción máxima")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        valor = float(input("Ingrese producción: "))
        agregar_produccion(produccion, valor)
    elif opcion == 2:
        print(f"El total producido en este período fue: {total_producido(produccion)}")
    elif opcion == 3:
        print(f"El promedio producido fue de: {prom_data(produccion)}")
    elif opcion == 4:

        print(f"El máximo producido fue de: {max_producc(produccion)}")
    elif opcion == 5:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida, intente nuevamente.")
    
