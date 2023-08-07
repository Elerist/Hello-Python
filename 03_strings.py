# Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)


my_tab_string = "\t Este es un String con tabulacion"
print(my_tab_string)    


my_scape_string = "\t Este es un String escapado \n escapado"
print(my_scape_string) 


# Formateo
# Forma correcta de concatenar, no usar mucho el + 

name, surname, age = "Leo", "Rodriguez", 24
# Esta formar si estamos imprimiendo tal cual los datos 
print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) 

# Esta si estamos Formateando los datos
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Formatea un string %s pero para entero %d


# Inferencia de Datos (f)

print (f"Mi nombre es {name} {surname} y mi edad es {age}") 


# Strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2

formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

# %f - Floating point numbers
print(formated_string)



python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)


print(formated_string)


# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = "Python"
print(a)
print(b)


# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-1]
print(language_slice)

language_slice = language[0:6:2] # Forma rebuscada busca el medio de 6 y 2
print(language_slice)


# Reverse

reverse_language = language[::-1]
print(reverse_language)


# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper()) # Comprueba si la funcion aterior es correcta
print(language.startswith("py")) # Empieza con ...  Diferencia mayus de minus


