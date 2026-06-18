#Ejercicio 5 Pide una frase y muestra cuántas palabras tiene.

palabra = input("Ingrese una frase: ")


palabra_list = palabra.split()


conteo = len(palabra_list)

print(conteo)