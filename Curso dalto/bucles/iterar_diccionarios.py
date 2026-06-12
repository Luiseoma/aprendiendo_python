diccionario = {
    "nombre": "Luis",
    "apellido": "Omaña",
    "edad": 29
}

#recorriendo diccionario para obtener las claves
for datos in diccionario:
    print(datos)

#recorriendo diccionario con .items para obtener clave y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")