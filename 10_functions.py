# Functions
# Intenta resolver un problema concreto y evita errores
# Se puede crear funciones o usar las funciones built in que son las que ya vienen con Python

def my_function():
    print("Esto es una funcion")

my_function()


def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(10, 34)


# Return
def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_resut = sum_two_values_with_return(10,10)

print(my_resut)



# f(formateo) interpola, los transforma en str y deja un espacio en blanco
def print_name(name, surname):
    print(f"{name} {surname}")

# Si nos equivocamos en el orden podemos rectificarlo
print_name(surname = "Rodriguez", name = "Leo")



# Valor por defecto y cambiando el valor por defecto
def print_name_with_defaul(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_defaul("Leo", "Rodriguez", "Antares")



# Funcion con parametros arbitrarios
# * sirve para pasar la cantidad de datos x que queramos
# Es como una "Lista" infinita
def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("hola", "juan", "como", "estas")
print_texts("hola")


# Funciones Build in

num = [4,7,43,12]

# numero mayor de una lista
num_mas_alto = max(num)
print(num_mas_alto)

# numero menor de una lista
num_mas_alto = min(num)
print(num_mas_alto)

# redondeando a 6 decimales
numero = round(12.3123124,2)
print(numero)

# Retorna False -> 0, vacio, False, ninguno \ True -> distinto a 0, true, str
resultado_bool = bool(None)
print(resultado_bool)

# retorna True si todos los valores son verdaderos
resultado_all = all([234,"asd",[344,32]]) # 0 es falso
print(resultado_all)

# suma todos los valores de un iterable
suma_total = sum(num)
print(suma_total)


# Funciones Propias

# Simple
def saludar():
    print("Hola como estas?")

saludar()


# Con parametros
def hi(nombre, sexo):
    sexo = sexo.lower() # permite que el sexo se pueda escribir con mayus sin error
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
        
    print(f"Hola {nombre}, mi {adjetivo}, como andas?")

hi("Camila","MuJEr")
hi("Rodolfo", "hombre")
hi("Fran","no binario")


# funcion que retorna valores
def password_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return password # rerturn se usa para almacenar y luego poder utilizar ese dato, no la muestra en consola pero queda almacenado

password = password_random(5) 
frase = f"Su nueva contraseña es: {password}"
print(frase)

# utilizando el parametro args (*) 
def suma(nombre,*numeros):  #  (*) permite poner parametros infinitos (si lo usamos se USA AL FINAL)
    return f"{nombre}, la suma total es: {sum(numeros)}"

resultado = suma("Juan",1,2,3,4,5,3,2)
print(resultado)


# Funciones LAMBDA
# Simplifica y acorta codigo, se usa para una instruccion
# Crea una funcion anonima
# Retorna automaticamente

# lambda multiplicando x2
multplicar_por_2 = lambda x : x*2

print(multplicar_por_2(57))


# usando filter y lambda para funcion  que dice si es par
numeros = [1,23,435,6,78,876,5,7,2]

numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))
