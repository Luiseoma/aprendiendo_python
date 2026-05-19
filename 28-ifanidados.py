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

#Evaluar si una estación existe en el arreglo
if 'Exposicion' in nombre_estacion:
    print('La estación Exposicion existe en el arreglo')
else:
    print('La estación Exposicion no existe en el arreglo')

#if anidados
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print("Bienvenido, tienes acceso de administrador")
    else:
        print("Bienvenido, puedes acceder a tu cuenta")
else:
    print("Debes iniciar sesión para acceder a tu cuenta")