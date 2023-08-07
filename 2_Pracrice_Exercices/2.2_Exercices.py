# Crear una funcion que nos devuelva los numeros primos
# entre 0 y el argumento que pasamos

# Funcion  que nos dice si es primo
def es_primo(num):
    # Verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese numero -1
    for i in range(2,num-1):
        # Si es divisible, retornamos false y termina el bucle
        if num%i==0: return False
    # Si termina el bucle, significa que no fue divisible entonces es primo
    return True


# Funcion que retorna una lista con todos los primos
def primos_hasta(num):
    # Creamos la lista
    primos = []
    for i in range(3, num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos

# Creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(13)
print(resultado)


# Forma rapida
primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2,int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta(15))