#Ejercicio 1
#Varios cursos fueron estudiados y varios demoraban en enseñar python entre 2.5 horas y 7 horas, dando un promedio de 4 horas
#el curso actual lo logro en 1.5h
#Diferencia en porcentaje entre el curso actual (1.5) y: el más rapido (2.5), el más lento(7) y el promedio (4)

#El crudo en promedio de los otros cursos es de 5 hrs y el crudo del actual es de 3.5 hrs
#Qué porcentaje de material inservible se reduce en:
#1 el promedio de los cursos y 2 el curso actual

#Ver 10 horas del curso actual sería equivalente a cuantas de otros cursos? y viceversa, cuantas horas de otros cursos es el equivalente a ver cuantas
#del curso actual


#duraciones
curso_actual = 1.5
curso_rapido = 2.5
curso_lento = 7
curso_promedio = 4

#diferencias de duración

diferencia_fast = 100 - (curso_actual / curso_rapido * 100)

print(f'El curso actual dura un {round(diferencia_fast)}% menos que el más rápido')

diferencia_low = 100 - (curso_actual / curso_lento * 100)

print(f'El curso actual dura un {round(diferencia_low)}% menos que el curso más lento')

diferencia_prom = 100 - (curso_actual / curso_promedio * 100)

print(f'El curso actual dura un {round(diferencia_prom)}% menos que el curso promedio')

crudo_otros_cursos = 5 
crudo_curso_actual = 3.5

#Material inservible

matIn_otros_cursos = 100 - (curso_promedio  / crudo_otros_cursos *100)

print(f'El material inservible de otros cursos es un {round(matIn_otros_cursos)}%')

matIn_curso_actual = 100 - (curso_actual / crudo_curso_actual *100)

print(f'El material inservible del curso actual es de un {round(matIn_curso_actual)}%')

#equivalencia de cursos
print(f'Ver 10 horas de este curso equivale a ver {round(curso_promedio / curso_actual * 10, 1)} horas de otros cursos')

print(f'Ver 10 horas de otros cursos equivale a ver {round(curso_actual / curso_promedio * 10, 1)} horas de el curso actual')





