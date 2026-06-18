#pide una frase y muestra cantidad de palabras y cantidad de caracteres si tiene mas de 20 palabras: esa frase es muy larga

frase = input("ingrese una frase: ")

conteo = len(frase.split())
conteo_car = len(frase)

if conteo > 20:
    print(f"Su frase tiene {conteo} palabras")
    print(f"Su frase tiene {conteo_car} caracteres totales")
    print("Frase muy larga te inventaste")    
elif conteo == 1:
    print(f"Su palabra tiene {conteo_car} caracteres")
else:
    print(f"Su frase tiene {conteo} palabras")
    print(f"Su frase tiene {conteo_car} caracteres totales")