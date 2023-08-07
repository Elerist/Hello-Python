# Modules
# Sirven para traer librerias, funciones, etc, Externas y reutilizarla sin necesidad de duplicarlo
# Opereciones en concreto ej: system_module
# Todo lo que tenga la extencion .py es un MODULO
# Desde un modulo podemos llamar a otro, crear rutas, armar paquetes, etc
# Tenemos 3 tipos de Modulos:
#                           - Modulos de Python (son los que ya vienen incorporados), creados con C
#                           - Modulos de Terceros(third party modules) (hechos por personas-empresa y subidos a internet)
#                           - Modulos Propios



"""

# Importar la carpeta completa

#import module

# Usar la funcion deseada

# module.sum_three_num(10,10,2)

# Importar SOLO una funcion especifica 

# from 10_functions import sum_two_values  (no puedo llamar carpetas que comienze con numero)

from module import mult

mult(10,10)



# Importar varias func

from module import mult, sum_three_num

sum_three_num(2,2,2)
mult(10,11)


# Se puede importar funciones del sistema en si 

import math

print(math.pi)

print(math.pow(2, 8))


# Alias a func ya existentes
# Ojo! Por que pi deja de existir como tal y queda renombrada

from math import pi as PI_VALUE

print(PI_VALUE)
"""


# Enrutamientos de MODULOS

# una vez importado paso de ser una funcion a ser un metodo. Por ende se puede usar como tal

import modulos_saludar as m_saludar # nos permite renombrarlo con as

saludo = m_saludar.saludar("Juanito")

print(saludo)


# Imoportar solo las funciones que queremos


from modulos_saludar import saludar, saludar_raro

saludo = saludar("Leo")
saludo_raro = saludar_raro("Fran")

print(saludo)
print(saludo_raro)


# Llamar modulos desde otras carpetas en la misma ruta

# Ejemplo ilustrativo
# import Exercice_practice.obtener_copañero



# Llamar modulos por fuera

# Ejemplo ilustrativo

# import sys
# print(sys.path) # path tiene la ruta para copiar, es la primer ruta
# sys.path.append("/Users/leonelrodriguez/Desktop/PC/Proyectos Programacion/Landding Page/Hello-Python/Hello-Python/ ACA SE PONDRIA EL NOMBRE DE LA CARPETA DONDE QUEREMOS AGREGAR LA FUNCION")

# import x as x   # y ya se puede usar

