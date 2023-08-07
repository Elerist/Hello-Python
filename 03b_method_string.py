# String Method
# Metodos son Funciones especificas de objetos

string1 = "hola,soy,Leo"
string2 = "Welcome to my creative world"

# print(dir(string1))
# print(dir(4)) # devuelve otro tipo de posibilidades
# print(dir(["juan","leo", 123])) # devueve ootra cosa ya que con listas se pueden hacer otras opereaciones y asi con cada diferente operador, tipo de dato

"""
resutado = dir(string1) # dir es una Funcion
print(resutado)
"""

# Convierten
mayus = string1.upper() 
print(mayus)
minus = string1.lower() 
print(minus)
primer_letra_mayus = string1.capitalize() 
print(primer_letra_mayus)


# Buscan 
# buscar cadena en otra cadena, (si retorna -1 no se encuentra valor)
buscar_find = string1.find("o") # posicion 
print(buscar_find)

# buscar cadena en otra cadena, si no encuentra nada nos devuelve una exepcion
"""
buscar_find = string1.index("x") # posicion 
print(buscar_find) 
"""


# Consultan si son num o alfanun

# Si es numerico, devuelve true, sino false
es_numerico = string1.isnumeric()
print(es_numerico)

# Es alfanumerico
es_alfa_numerico = string1.isalpha()# como el espacio no es alfanumerico tira false, la unica forma de que sea True es que sean letras de la a-z y no tenga espacio
print(es_alfa_numerico) 


# contamos las coincidencias de una cadena dentro de una cadena
# Devuelve la cantidad de coincidencias
# Si no se encuentra tira 0
contar_coincidencias = string1.count("e")
print(contar_coincidencias)


# contamos cuantos caracteres tiene una cadena
# len es una Funcion
contar_caracteres = len(string1)
print(contar_caracteres)


# Verifica si una cadena empieza con otra cadena dada, si es asi tira True
empieza_con = string1.startswith("hio")
print(empieza_con)


# Verifica si una cadena termina con otra cadena dada, si es asi tira True
termina_con = string1.endswith(" Leo")
print(termina_con)


# Si el valor 1, se encuntra en la cadena orinal, se remplaza el valor 1 por el valor 2
strin_new = string1.replace(",", " ") # cambia "la" por "lu"
print(strin_new)


# Devuelve una matris (Lista)
# Separar cadenas con la cadena que le pasemos
cadena_separada = string1.split(",")
print(cadena_separada)







