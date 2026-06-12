#"dir" devuelve todos los atributos válidos del objeto

cadena1 = "Hola,soy,Luis"
cadena2 = "Bienvenido"

#resultado = dir(cadena1)
#print(resultado)

#"upper" convierte todo en mayúscula 

resultado2 = cadena1.upper()

print(resultado2)

#"lower" convierte todo en minúscula

resultado3 = cadena1.lower()

print(resultado3)

#"capitalize" convierte la primera letra en mayuscula

resultado4 = cadena1.capitalize()

print(resultado4)

#"find" encuentra la primera aparición del objeto, si no devuelve 1

resultado5 = cadena1.find("o")

print(resultado5)

#"index" busca una cadena dentro de una cadena, pero si no consigue nada tira excepcion

resultado6 = cadena1.index("H")


#"isnumeric" si es numérico devuelve True

resultado7 = cadena1.isnumeric()

print(resultado7)

#"isalpha" si es alfanumérico devuelve True pero solo cuenta de la A-Z si tiene espacios tira False

resultado8 = cadena1.isalpha()

print(resultado8)

#"count" devuelve cuantas veces encontro una coincidencia

resultado9 = cadena1.count("o")

print(resultado9)

#"len" cuenta los caracteres de una cadena

resultado10 = len(cadena1)

print(resultado10)

#"endswith" verificamos si una cadena termina con otra cadena dada

resultado11 = cadena1.endswith("s")

print(resultado11)

#"startswith" verificamos si una cadena empieza con otra cadena dada

resultado12 = cadena1.startswith("H")

print(resultado12)


#"replace" reemplaza un valor por otro 

resultado13 = cadena1.replace(cadena1, cadena2)

print(resultado13)

#"split" separa cadenas con cadenas que le pasemos

resultado14 = cadena1.split("o")

print(resultado14[2])