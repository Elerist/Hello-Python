# Sets {}
# No es ordenado
# No admite repetidos
# No se duplican
# No se pueden llamar elementos por su indice

my_set = set()
my_other_set = {} # Inicialmete es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Leonel", "Rodriguez", 24} # Pero cuando se completa vuelve a ser set
print(type(my_other_set))


print(len(my_other_set))

# Formas de ver que hay dentro y como agregar
my_other_set.add("Elerist")
print(my_other_set)


my_other_set.add("Elerist")
print(my_other_set)


# Sintaxis para ver que elementos hay dentro de un set

print("Leonel" in my_other_set)
print("Leo" in my_other_set)


# Quitar datos

my_other_set.remove("Elerist")
print(my_other_set)


my_other_set.clear()  # limpia el set y lo deja en 0
print(my_other_set)


del my_other_set # borra la variable completamente, deja de existir
#print(my_other_set) # Error por que no esta definido




my_set = {"Leonel", "Rodriguez", 24}
my_list = list(my_set)
print(my_list)
print(my_list[0])# No! ya que al ser desordenados el orden especifico va a variar



# Unir set

my_other_set =  {"Ktlin", "Swift", "Python"}

my_mew_set = my_set.union(my_other_set)
print(my_mew_set) 

# Agregar elementos de otra forma
my_mew_set = my_mew_set.union({"Js","C#"})
print(my_mew_set)


print(my_mew_set.difference(my_set))


# Metiendo un set dentro de otro set

set1 = frozenset(["data 1", "data 2"])
set2 = {set1, "dato 3"}
print(set2)


# Teoria de sets

conjunto1 = {1,3,5,7,"leo"}
conjunto2 = {1,3,7,"leo"}

# Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1) # issubset, significa si es subconjunto de..
print(resultado) # es true ya que conjunto2 tiene todos los datos que hay en conjunto1


# Verificando si es un superconjunto
resultado2 = conjunto2.issuperset(conjunto1)
print(resultado2)

# Verificando si hay algun elemento coincide

resultado3 = conjunto2.isdisjoint(conjunto1)
print(resultado3) # Solo es true cuando ningun elemento coincide