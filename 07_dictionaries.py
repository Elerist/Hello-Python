# Dictionaries
# Estructura donde podemos almasenar datos de tipo clave-valor
# No tiene orden

my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre":"Leonel", "Apellido": "Rodriguez", "Edad":24, 1:"Python"}

my_dict = {
    "Nombre":"Leonel",
    "Apellido": "Rodriguez",
    "Edad":24,
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # str de clave y set de valor
    1:1.80
    }  

print(my_other_dict)
print(my_dict)


print(len(my_other_dict))
print(len(my_dict))

# Llamar a una clave
print(my_dict["Nombre"])

# Actualizar el valor
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])


# Agregar clave-valor

my_dict["Calle"] = "Calle Rodriguez"
print(my_dict)


# Eliminar 1 elemento

del my_dict["Calle"]
print(my_dict)


# Comprobar si tenemos una clave

print("Apellido" in my_dict) # True
print("Pedro" in my_dict)   # False




print(my_dict.items()) # Todos los items
print(my_dict.keys()) # Todas las llaver
print(my_dict.values()) # Todos los valores


# Crea un diccionario nuevo sin valores, solo claves 
print(my_dict.fromkeys(("Apellido",1)))


# Otra forma de hacerlo (Se usa para reutilizar las claves y posteriormente ponerle datos nuevos)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)


# Meter a todas las claves el valor pasado "leo"
my_new_dict = dict.fromkeys(my_dict, "Leo" )
print((my_new_dict))