# Tuples ()
# Conjunto de valores

# La diferencia entre Tupla y Lista es que las Tuplas tienen valores CONSTANTES  no te los deja cambiar
# Tuplas son inmutables 
# Se usan cuando hacemos solo lectura, manejan mejor los datos


my_tuple = tuple()
my_other_tuple = () # Solo parentesis tupla

# Otra forma de crear tublas de multiples datos
tuple_2 = "data",  "Barrio 140"
# Otra forma de crear tublas de un dato
tuple_2 = "data",


my_tuple = (35, 1.77, "Leonel", "Rodriguez", "Leonel")
my_other_tuple = (24, 39, 60)


print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[-3])
print(my_tuple[2])



print(my_tuple.count("Leonel"))
print(my_tuple.index(1.77))
print(my_tuple.index("Rodriguez"))

# Se pueden sumar y crear una nueva sumando 2

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_tuple) # sin perder la original


print(my_sum_tuple[3:6])


# Si se quiere pasar una Tupla a List, agregar y volver a Tupla
# No es lo mas recomendable

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Elersit"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


# del my_tuple la elimina 

