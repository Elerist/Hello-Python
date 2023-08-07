# Classes
#  Todo lo que este dentro de una misma clase debe responder a una misma logica
# Las clases se escriben camel case

# Evita errores
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


# Constructor de Clase. def __init__(self): , permite dar la capidad de parametros
class Person:
    def __init__(self, name, surname): # Constructor de Clase
        self.name = name
        self.surname = surname


my_person = Person("juan", "carlos")
print(f"{my_person.name} {my_person.surname}")


# Con parametros ya definidos
class Person:
    def __init__(self): # Constructor de Clase
        self.name = "Leo"
        self.surname = "Rodriguez"


my_person = Person()
print(f"{my_person.name} {my_person.surname}")


# Mejorado
class Person:
    def __init__(self, name, surname, alias = "Sin Alias"): # Constructor de Clase
        self.full_name = f"{name} {surname} ({alias})"

    # Funciones
    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("Leonel", "Rodriguez")
print(my_person.full_name)
my_person.walk()


my_other_person = Person("Leo", "Rodriguez", "Elerist")
print(my_other_person.full_name)
my_other_person.walk()


