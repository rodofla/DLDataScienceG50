# módulo que permite la ejecución de un programa con argumentos
from sys import argv

# variables que reciben los argumentos
nombre = argv[1]
apellido = argv[2]

# imprime el nombre y apellido
print(f"Mi nombre es {nombre}")
print(f"Mi apellido es {apellido}\n")
print(f"El nombre del archivo es {argv[0]}")
