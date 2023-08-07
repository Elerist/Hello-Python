# Exercise 1
"""
Si un curso tarda en explicar lo visto hasta ahora entre:
    1.5h este curso
    2.5h minimo
    4h  promedio
    7h  maximo
    
    3.5h crudo (video sin editar)
    5h   crudo

a. Diferencia en porcentaje entre el curso actual y:
    _ el mas rapido de otros cursos
    _ el mas lento de otros cursos
    _ el promedio de los cursos

b. Porcentaje de material inservible que se reduce en:
    _ el promedio de los cursos
    _ el curso actual (este curso)

c. Ver 10 horas de este curso a cuantas de otros cursos equivale? y al reves?

"""


otro_curso_min = 2.5
otro_curso_promedio = 4
otro_curso_max = 7
este_curso = 1.5

crudo_promedio = 5
crudo_este_curso = 3.5

# a
# Diferencia de duracion

diferencia_con_min = round (100 - este_curso / otro_curso_min * 100, 2)
diferencia_con_max = round (100 - este_curso / otro_curso_max * 100, 2)  # redondear mejor sin tantos decimales (si queremos correr la coma 2 lugares es: *10000 y *100)
diferencia_con_promedio = round (100 - este_curso / otro_curso_promedio * 100, 2)

print("------------------------")
print("Este curso dura: ")
print(f" {diferencia_con_min}% menos que el mas rapido")
print(f" {diferencia_con_max}% menos que el mas lento")
print(f" {diferencia_con_promedio}% menos que el promedio")
print("------------------------")


# b
# Porcentaje de tiempo vacio removido

tiempo_vacio_promedio = round (100 - otro_curso_promedio / crudo_promedio * 100, 2) 
tiempo_vacio_este_curso = round (100 - este_curso / crudo_este_curso * 100, 2)

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso  elimino el {tiempo_vacio_este_curso}% de tiempo vacio")
print("------------------------")


# c
# Mostrando diferencia si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {round(otro_curso_promedio / este_curso, 2)} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {round(este_curso  / otro_curso_promedio * 10, 2)} horas de este cursos")
print("------------------------")


