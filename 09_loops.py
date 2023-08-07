# Loops, Ciclos o Bucles
# Repetir codigo hasta cumplir la condicion, elementos, etc
# Solo los elementos iterables se puden repetir
# Se puede utilizar en listas, tuplas
# los diccionarios se hacen de una forma particular

# While
# A diferencia del For que recorre elementos, el While se va a repetir mientras la condicion sea True

my_condition = 0

while my_condition <= 10:
    print(my_condition)
    my_condition += 1
else: # opcional
    print("Mi condicion es mayor que 10")


# Detener bucle  break (lo detiene por completo no ejecuta ni siquiera el else)
while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Mi condicion es 15, se detiene la ejecucion")
        break

    print(my_condition)


# For  (Sirve para iterar un listado de x elementos)

my_list = [24, "Leonel", 61, 27, 39]

for element in my_list:
    print (element)


my_tuple = (35, 1.77, "Leonel", "Rodriguez", "Leonel")

for element in my_tuple:
    print (element)

my_set = {"Leonel", "Rodriguez", 24}

for element in my_set:
    print (element)

# Recorriendo DiccionarioiImprimiedo las Claves
my_dict = {"Nombre":"Leonel", "Apellido": "Rodriguez", "Edad":24, 1:"Python"}

for element in my_dict:
    print (element) 

# Recorriendo Diccionario Imprimiedo clave-valor

diccionario = {"nombre": "Leo", "apellido": "Rodriguez", "año": 1998}

for values in diccionario.items():
    print(values)

# otra forma si quisieramos imprimir los valores tendriamos que transformarlo en una lista

for element in list(my_dict.values()):
    print(element)


# Como en while en el for tambien tenemos else y break

for element in my_dict:
    print (element) 
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para mi dic ah finalizado")



# Continue vuelve al for sin ejecutar esa parte 

frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una {fruta}")


# zip
# Recorrer 2 o mas listas al mismo tiempo (solo se puede hacer si tienen la misma cantidad de valores)
# Se itera al mismo tiempo 1 y 2, 1 y 2 etc

animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52,16,14,72]

for animal,numero in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")


# Forma correcta de recorrer una lista con su INDICE

for num in enumerate(numeros):
    indice = num[0] # 0 es indice
    valor = num[1] # 1 es valor 
    print(f"indice: {indice} valor: {valor}")


diccionario = {"nombre": "Leo", "apellido": "Rodriguez", "año": 1998}


# for en una sola linea de codigo
# Se puede aplicar cualquier operacion matematica

numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
