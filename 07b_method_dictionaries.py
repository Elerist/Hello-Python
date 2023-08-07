# Method Dictionaries

"""
Keys() --> devuelve las claves (tambien sirve para iterar)
get() --> devuelve el valor de una clave
clear() --> elimina todos los elementos
pop() --> elimina un elemento
items() --> para iterar el dict

"""

diccionario = {
    "nombre" : "leo",
    "apellido" : "rodriguez",
    "subs" : 10000
}

# devuelve un elemento dict_item 
claves = diccionario.keys()
print(diccionario)

# obteniendo un elemento con get() y si no encuentra nada el programa continua
valor_de_nombre = diccionario.get("nombre")
print(claves)

# clear elimina todos los elementos del diccionario
#diccionario.clear()
#print(diccionario)

# eliminando un elemento del dict
diccionario.pop("nombre")
print(diccionario)

# obteniendo un elemento dict_items interable: significa que se puede recorrer el elemento
diccionario_iterable = diccionario.items()
print(diccionario_iterable)



