#cada persona promedio habla 2 palabras por segundo 
#Pedirle al usuario que diga cualquier texto real y:
#calcular cuanto tardaría en decir esa frase
#Si se tarda más de 1 minuto:
#decirle: "habla más rápido o di menos palabras"
#Dalto habla un 30% más rápido: ¿Cuánto tardaría él en decirlo?

frase = input("Dime algo y calculo cuanto tardarías en decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras/2} segundos en decirlo")
print (f'Dalto lo diría en {cantidad_de_palabras * 100 // 2 // 1.3 / 100} segundos en decirlo')
if cantidad_de_palabras > 120:
    print("tampoco te pedí tantas palabras")