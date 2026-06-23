#Ejercicio 3: Generador de Correos
#Una empresa necesita crear correos corporativos.
#Si el usuario escribe:
#Luis Omaña
#Debe generar:
#luis.omana@empresa.com
#Pistas:
#lower()
#replace()

nombre = (input("Ingrese nombre de usuario: "))
nombre2= nombre.replace("ñ", "n")
usuario = nombre2.lower().replace(" ", ".")

correo_listo = usuario + "@empresa.com"

print(correo_listo)