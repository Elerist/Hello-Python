import re 

texto = """__Hola como estas?, esta es la cadena 1  de texto
Esta es la 2 linea
y esta es la  3 y final mi Capitan__"""

# Ejemplos mas usados
#resultado = re.search("Hola", texto)

# Haciendo una busqueda simple
#resultado = re.findall("Esta", texto, flags=re.IGNORECASE)# Tenemos un tercer parametro opcional como IGNORECASE (ignora mayusculas)

# \d --> busca digitos numericos del 0 al 9
#resultado = re.findall(r"\d",texto)  # con la r estoy avisando que voy a usar expresiones regulares

# \D --> busca TODO menos digitos numericos del 0 al 9
#resultado = re.findall(r"\D",texto)  # con la r estoy avisando que voy a usar expresiones regulares

# \w --> busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto) 

# \W --> busca TODO menos caracteres alfanumericos [a-z A-Z 0-9 _]resultado = re.findall(r"\W",texto) 

# \s --> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s",texto) 

# \S --> busca TODO menos espacios en blanco
#resultado = re.findall(r"\S",texto) 

# . --> Busca TODO menos saltos de linea
#resultado = re.findall(r".",texto) 


# \n --> Busca saltos de linea
#resultado = re.findall(r"\n",texto) 

# \ --> Cancela caracteres especiales
# resultado = re.findall(r"",texto) 

#print(resultado)