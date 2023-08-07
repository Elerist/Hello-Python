# Operadores Aritmeticos
"""
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4) # float
print(10 % 2) # Modulo resto de la division 
print(10 // 3) # Divisionbaja, redondea para abajo, resultado acaba terminando en un numero ENTERO
print(2 ** 3) # Elevado
"""

# No se puede usar otra operacion mat en string, solo sumar
# No se puede operar numeros con string

#print("Hola" + " " + "Python")

# Pero hay exepciones por ej:

#print("Hola " * 5)


# Operadores Comparativos

"""
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
"""


# Compara en orden alfabetico, no cuenta caracteres 
"""
print("hola" > "python")
print("hola" < "python")
print("hola" >= "python")
print("hola" <= "python")
print("hola" == "python")
print("hola" == "hola")
print("hola" == "zola")
print("aaaa" == "abaa")
print("hola" != "python")
print(len("aaaa") >= len("aaaa")) # Si queremos contar caracteres (len cuenta caracteres)
print("aaaa" > "AAAA")
print("AAAA" > "aaaa")
"""



# Operadores Logicos

# and   &

resultado = True & True #Devolver True
resultado2 = False & True #Devolver Falso
resultado3 = True & False #Devolver Falso
resultado4 = False & False #Devolver Falso

#print(3 > 4 and "hola" > "python") # false + false = false


# or  |

resultado5 = True | True #Devolver True
resultado6 = False | True #Devolver True
resultado7 = True | False #Devolver True
resultado8 = False | False #Devolver False

#print(3 > 4 or "hola" > "python")

#print(3 < 4 and "hola" < "python")
#print(3 < 4 or "hola" < "python") # True + True = True
#print(3 < 4 or "hola" > "python") # True + False = True (en or)


# not

resultado9 = not True #Devolver False
resultado10 = not 2 == 2 #Devolver False
resultado11 = not False #Devolver True
resultado12 = not 3 > 34 #Devolver True

#print(not (3 > 4 )) # No falso es Verdadero, not nos devuelve el opuesto del resultado

print(resultado12)



