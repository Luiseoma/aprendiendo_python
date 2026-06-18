#pide una nota del 1 al 7: < 4 reprobado, 4 a 5.9 aprobado y > 6 excelente 

nota = float(input("Ingrese nota del estudiante: "))

if nota < 0: 
    print("ingrese una nota válida")
elif nota > 7:
    print("ingrese una nota")
elif nota < 4:
    print(f"Estudiante reprobado, su resultado fue {nota}")
elif nota <= 5.9:
    print(f"Estudiante aprobado, su resultado fue {nota}")
else:
    print(f"Estudiante aprobado con nota excelente, su resultado fue {nota}")