# Lists []
# Siempre son ordenados

my_list = list()
my_other_list = [] # Solo corchetes lista

print(len(my_list))

my_list = [35, 24, 30, 64, 30, 17]

print(my_list)
print(len(my_list))


# En listas empieza a contar desde 0
my_other_list = [34, 1.8, "Leo", "Rodriguez"]
print(my_other_list)

print(type(my_other_list))

print(my_other_list[1]) 
print(my_other_list[0]) 
print(my_other_list[-1]) 
print(my_other_list[-3]) 
#print(my_other_list[-5]) IndexError
#print(my_other_list[4])  IndexError
print(my_other_list.count(34)) # count Retorna la cantidad de veces que se repite un valor


age, height, name, last_name = my_other_list
print(name)

print(my_list + my_other_list) # Se puede sumar listas


my_other_list.append("Elerist") # append Agrega elemento a la lista
print(my_other_list)

my_other_list.insert(1,"rojo") # insert Inserta/Agrega un elemento en la posicion que digamos
print(my_other_list)

my_other_list.remove("rojo") # remove Quita el elemento por su valor
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop() # pop Quita el  elemento por su indice y tambien te muestra/guarda el valor eliminado, -1 ultimo elemento
print(my_list)

print(my_list.pop(2))
print(my_list)


del my_list[2] # del Elimina el elemento por indice
print(my_list)




print(my_other_list)

my_other_list[4] = "BlackElerist"  # Renombrar elemento de la lista 
print(my_other_list)

my_new_list = my_list.copy() # copy Copia la lista hasta como estaba en ESE MOMENTO

my_list.clear() # clear Borra la lista
print(my_list)
print(my_new_list)


my_new_list.reverse() #reverse  Revierte el orden de los valores
print(my_new_list)


my_new_list.sort()  # No funciona si tiene str, sort Podemos pasarle criterios para ordenar, si no le damos criterios por defecto oedenara de menor a mayor
print(my_new_list)

print(my_new_list[1:2])