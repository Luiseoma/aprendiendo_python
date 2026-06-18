#Pide una frase y calcula cantidad de palabras tiempo para decirla 2 PPS si tarda mas de 30 segundos: Frase muy larga 

frase = input("Ingrese una frase para calcular cuanto demoraría en decirla: ")
conteo = len(frase.split())

tiempo = conteo / 2

if tiempo > 30:
    print(f"Su frase tiene {conteo} palabras")
    print(f"Decir esta frase te llevaría {tiempo} segundos")
    print("Su frase fue muy larga")
else:
    print(f"Su frase tiene {conteo} palabras")
    print(f"Decir esta frase te llevaría {tiempo} segundos")
