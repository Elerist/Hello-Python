# Exercise 2

"""
a. Pedirle al usuario que diga cualquier texto real y:
    calcular cuanto tardaria en decir esa frase
    Cuantas palabras dijo?

b. Si tarda mas de 1 minuto
    decirle: "para flaco tampoco pedi un testamento"

c. El profe habla un 30% mas rapido:
    Cuanto tardaria el en decirlo?

"""
# Pedir al usuario que nos diga una frase
frase = input("Decir un frase y te calculo cuanto tardarias si tuvieraas que decirla: ")

# Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

# Usamos len() para ver la cantidad de elementos que hay en la lista
cant_de_palabras = len(palabras_separadas)

# En caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cant_de_palabras > 120: # 120 es un minuto, 0.5 por palabra
    print("para flaco tampoco pedi un testamento")

# Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"Dijiste {cant_de_palabras} palabras, y tardarias {cant_de_palabras/2} segundos en decirlo")
print(f"El profe tardaria {cant_de_palabras * 100 //2 * 1.3 / 100} segundos decirlo") # 1.3 es el 30%
