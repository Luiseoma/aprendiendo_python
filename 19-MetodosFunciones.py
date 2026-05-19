mensajeDeBienvenida = 'bienvenido a Python es un placere tenerte aquí'



def nombre_usuario(nombre, actividad):
    print(f'Hola {nombre}, {mensajeDeBienvenida}')
    print(f'Se que lo último que hiciste fue {actividad}, espero que te haya gustado')

nombre_usuario('Pedro', 'jugar fútbol')
nombre_usuario('Maria', 'leer un libro')
nombre_usuario('Luis', 'ver una película')