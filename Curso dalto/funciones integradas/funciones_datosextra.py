#creando una funcion de 3 parametros
#def frase(nombre, apellido, adjetivo):
#    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"
#
#frase_resultante = frase("Luis", "Omaña", "alto")
#print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = "bajo"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Luis", "Omaña")
print(frase_resultante)