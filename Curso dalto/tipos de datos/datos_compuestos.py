#lista (se puede modificar)

lista = ["Luis", "Omaña", 1.83]


#tupla (no se puede modificar)

tupla = ["Luis", "Enrique", "Omaña", 1.83, 29]

print(tupla[3])

#esto es valido
lista[2] = "Enrique"

print(lista[2])

#esto no
#tupla[2] = "Enrique"

#creando un conjunto (set)

conjunto = {"Luis", "Omaña", "Morales", 1.83, 29}

#print(conjunto[3]) -> no puede acceder al elemento (se hace con bucles)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    "nombre": "Luis Enrique",
    "apellido": "Omaña Morales",
    "altura": 1.83,
    "peso": 110
}

print(diccionario["altura"])