# Crear una funcion que nos devuelva los numeros Fibonacci
# entre 0 y el argumento que pasamos


def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        for i in range(num):
            if b > num: return fibonacci_lista
            else: 
                fibonacci_lista.append(b)
                a,b = b,a+b

resultado = fibonacci(20)

print(resultado)

