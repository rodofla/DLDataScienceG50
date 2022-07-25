from sys import argv # Importamos la librería argv

precios = {
            'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000
            }

umbral = int(argv[1]) # Obtenemos el umbral
filtro = {} # Creamos un diccionario vacío
error_msj = "Lo sentimos, no es una operación válida" # Mensaje de error

try:
    condicion = argv[2]
except IndexError:
    condicion = 'mayor'

    
if condicion != None:
    if condicion == 'mayor':
        filtro = {key:value for (key, value) in precios.items() if value > umbral}
    elif condicion == 'menor':
        filtro = {key:value for (key, value) in precios.items() if value < umbral}




if condicion == "mayor" or condicion == "menor":
    print(f'Los productos {condicion}es al umbral son: {", ".join(filtro.keys())}')
else:
    print(error_msj)