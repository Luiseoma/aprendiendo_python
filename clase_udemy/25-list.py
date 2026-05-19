nombre_estacion = [
    'Calera',
    'Cerrillos',
    'Grecia',
    'La Florida',
    'Lampa',
    'Nos',
    'Quilpue',
    'Santa Rosa',
]

def encontrar_estacion(estacion_buscada): 

    encontrada = False

    for estacion in nombre_estacion:
        print(estacion)

    if estacion == estacion_buscada: 
        print(f'Encontramos la estación {estacion_buscada}')
        encontrada = True

    if not encontrada :       
        print(f'No encontramos la estación {estacion_buscada}')       

encontrar_estacion('Exposicion')

#Ordenar los nombres de las estaciones
nombre_estacion.sort() 
print(nombre_estacion)

#Acceder a una estación por su índice
deuda = f'La estación {nombre_estacion[3]} tiene deuda con la empresa de transporte'
print(deuda)

#Modificar valores de un arreglo
nombre_estacion[2] = 'N/A'
print(nombre_estacion)

#Agregar una nueva estación
nombre_estacion.append('Exposicion')
print(nombre_estacion)

#Eliminar por nombre
nombre_estacion.remove('N/A')
print(nombre_estacion) 

#eliminar con del
del nombre_estacion[2]
print(nombre_estacion)

#eliminar el ultimo elemento
nombre_estacion.pop()
print(nombre_estacion)


#eliminar con pop una posicion en especifico
nombre_estacion.pop(1)
print(nombre_estacion)


