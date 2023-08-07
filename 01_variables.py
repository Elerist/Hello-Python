# Variables en Python  por buena regla se escribe en snakecase

my_str_variable = "My String variable"
print(my_str_variable)

my_int_var = 5
my_int_var += 10 # += suma a la var original
print(my_int_var)

my_bool_var = False
print(my_bool_var)

'''
llamar  multiples variables (,)  (concatenar)
'''

print(my_str_variable, my_int_var, my_bool_var)
#

# convertir int en str

my_int_to_str_var = str(my_int_var)
print(my_int_to_str_var)
print(type(my_int_to_str_var))

print(my_str_variable, my_int_to_str_var, my_bool_var)
print("Este es el valor de:", my_bool_var)



# some System Functions

# len (cuenta)
print(len(my_str_variable))


# Variables en una sola linea. 
# Se puede hacer pero hay que tener cuidado y no usar sin que sea necesario


name, subname, alias, age = "Brais", "Moure", "MoureDev", 35

print (name,subname,alias,"Mi edad es:", age)



# Inputs (nteraccion por consola con el usuario)

#first_name = input("What´s your name: ")
#age = input("How old are you? ")

##print("Your name is",first_name)
#print("Your age is",age)



# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type("Asabeneh"))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

# Practice

# Most common built-in functions

print("Hello")

print(len("Hello"))

print(type("Hello"))

print(str(10)) # 10 becomes str

print(int("10")) # "10" becomes int

print(float(10))


#name = input("Enter your name: ")
#print( "Your name is:",name)


#print(help(str))

print(min(10,2,3,88,1232))

print(max(213,455454,888888,3,4))

print(sum([12,10,3]))


# f str (transforma todo a str)

nombre = "Leo"
hi = f"Holaa {nombre}, como estas?"
print(hi)

# Operadores de pertenecia (duvuelven true o false)

print("Leo" in hi) # true
print("Leo" not in hi) # false




# Unpacked

data_list = ("Leo", "Rodriguez", 98)
data_tuple= ["Leo", "Rodriguez", 98]

# Desempaquetado (Unpacked)
nombre,apellido,año = data_tuple # Funciona solamente cuando la cantidad de variables es igual a la cantidad de datos que tiene el arry

print(nombre)

