"""
Hoy falto el profesor de clases y los chicos organizaron para armar la suya propia. Uno de los alumnos 
va a ser el Profesor y el otro su asistente.

1 Alumno Profe
1 Alumno Asistente

b. El mayor es el profesor y el menor es el asistente. Quien es quien?
"""

# funcion para obtener al Profesor y al asistente segun su edad
def obtener_compañero(cantidad_de_compañeros):
    # creando lista vacia de compañeros
    compañeros = []
    
    # Pedir informacion a cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        # Agrega dicha informacion a la lista
        compañeros.append(compañero)
        
    # ordena de menor a mayo segun su edad    
    compañeros.sort(key=lambda x:x[1])
    
    # compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir
    # al asistente y al profesor
    asistente = compañeros [0][0]
    profesor = compañeros [-1][0]
    
    # retornamos la tupla
    return asistente,profesor

# desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañero(5)

# Mostrar resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")



