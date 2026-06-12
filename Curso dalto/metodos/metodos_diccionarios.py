diccionario = {
    "nombre": "Luis",
    "apellido": "Omaña",
    "edad": 29
}

#"keys()" devuelve las claves (también sirve para iterar)

claves = diccionario.keys()

#"get()" devuelve el valor de una clave

claves = diccionario.get("nombre")

#"clear()" elimina todos los elementos del diccionario

#diccionario.clear()

#"pop()" elimina un elemento del diccionario

#diccionario.pop("nombre")

#"items()" sirve para iterar el diccionario

dict_iterable = diccionario.items()

print(dict_iterable)