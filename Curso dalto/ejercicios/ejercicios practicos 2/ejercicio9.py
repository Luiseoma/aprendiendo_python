#Ejercicio 6: Adivina el número
#
#Crea una variable:
#
#numero_secreto = 7
#
#Y permite que el usuario siga intentando hasta acertar.

numero_secreto = 7 

adivina = float(input("Adivina el número: "))

while adivina != numero_secreto:
    adivina = float(input("Sigue intentando: "))
    
print("Has acertado")