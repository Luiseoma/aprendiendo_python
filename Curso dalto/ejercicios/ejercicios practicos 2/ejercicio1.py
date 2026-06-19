#Hoy falto el profesor de clases y los alumnos se organizaron para hacer la suya propia
#un alumno será el profesor y un alumno será el asistente
#A) pedir el nombre y edad de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor

def obtener_compañeros(cantidad_compañeros):
    compañeros = []

    for i in range(cantidad_compañeros):
        nombre = input("Ingrese nombre del compañero: ")
        edad = int(input("Ingrese edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compañeros(5)

print(f"El asistente es: {asistente} y el profesor es: {profesor}")