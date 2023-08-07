# List Method

lista = ["hola", "Leo", 34]

# Funcion, devuelve la cantidad de elementos 
resultado = len(lista)
print(resultado)

# Agregando elementos a la lista
lista.append("jajaja")
print(lista)

# Agregando elementos a la lista en un indice especifo
lista.insert(2, "Toma mama")
print(lista)

# Concatena una lista a otra lista
lista.extend([False,2023])
print(lista)


# Verificando si un elemento se encuentra en la lista
elemet_encontrado = lista.index(34)
print(elemet_encontrado)



