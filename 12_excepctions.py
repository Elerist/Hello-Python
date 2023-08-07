# Excepction Handling

number_one = 5
number_two = 1
#number_two = "1"

# try except es igual a triy catch
try:
    print(number_one + number_two)
    print("No se ah producido un error")
# Se ejecuta si se produce una excepcion
except:
    print("Se ah producido un error")


# try except else finally
try:
    print(number_one + number_two)
    print("No se ah producido un error")
except:
    print("Se ah producido un error")
else:
# Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
# Se ejecuta siempre
    print("La ejecucion continua")



# Exceptiones por tipo

try:
    print(number_one + number_two)
    print("No se ah producido un error")
# Se ejecuta solo si hay Error. Hay vario tipos de errores
# Si se quiere capturar todos los Errores hay que poner solo exept
except TypeError:
    print("Se ah producido un TypeError")
except ValueError:
    print("Se ah producido un ValueError")



# Captura de la informacion del error
# Informarle al usuario del error
try:
    print(number_one + number_two)
    print("No se ah producido un error")
except ValueError as error:
    print(error) # Tenemos un objeto error con informacion
except Exception as Exceptionerror: # Exception (sea el error que sea) el mismo se controle
    print(Exceptionerror)


#----------------------------

def sumar_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            print("Ingresar un numero entero")
            print(f"ERROR: {type(e).__name__}") # Te dice el tipo de error
        else:
            break 
    return resultado

print(sumar_dos())


#-----------------------------------

# Creando una Exception

class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Error: {err}")

# Lanzando mi propia exepcion
#raise  MiExcepcion("Cometiste un error")  # raise es la palabra clave para lanzar excepciones

# Manejandola
try:
    raise MiExcepcion("Cometiste un error")
except:
    print("Como vas a cometer un error?")