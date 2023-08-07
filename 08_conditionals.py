# Conditionals
# Formas de establecer flujos de ejecucion de codigo

my_condition = False


if my_condition: 
    print("Se ejecuta la condicion del if")

print("La ejecucion continua")



my_condition = 1

if my_condition == 10: 
    print("Se ejecuta la condicion del segundo if")

print("La ejecucion continua")



if my_condition > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1: # elif al igual que if necesitan una condicion
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecucion continua")



my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de texto": 
    print("Las cadenas de texto coinciden")



# if anidados y elif

ingreso_mensual = 91000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("Estas gastando mucho")