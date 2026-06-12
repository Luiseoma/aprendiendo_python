#creando diccionario con dict()

diccionario = dict(nombre="Luis", apellido="Omaña")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["luis", "omaña"]):"hola"}

#creando diccionarios con fromkeys() valor por defecto none

diccionario = dict.fromkeys(["Nombre", "Apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto

diccionario = dict.fromkeys(["Nombre", "Apellido"],"N/A")

print(diccionario)